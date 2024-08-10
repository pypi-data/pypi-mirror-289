from datetime import datetime, timezone
from typing import Dict, Optional, Union
from uuid import UUID, uuid4
from pydantic import BaseModel
from json import loads
from .sqs_message import SqsMessage
from .functions import parse_message_attributes


class SqsReponse(BaseModel):
    message_id: str
    receipt_handle: str
    md5_of_body: str
    body: str
    attributes: Optional[Dict] = {}
    topic: Optional[str] = ""
    md5_of_message_attributes: Optional[str] = ""
    message_attributes: Optional[Dict] = {}

    @staticmethod
    def correlation_id_from_attributes(attributes: Dict) -> Optional[str]:
        correlation_id = attributes.get('correlation_id', None)
        if not correlation_id:
            return None
        if isinstance(correlation_id, str):
            return correlation_id
        if isinstance(correlation_id, dict) and 'Type' in correlation_id and 'Value' in correlation_id:
            return correlation_id["Value"]
        return None

    def get_correlation_id(self, payload: Optional[Dict] = {}) -> Union[str, UUID]:
        correlation_id = self.correlation_id_from_attributes(self.message_attributes)
        if correlation_id:
            return correlation_id
        correlation_id = self.correlation_id_from_attributes(self.attributes)
        if correlation_id:
            return correlation_id
        if 'correlation_id' in payload:
            return payload['correlation_id']
        return str(uuid4())

    @staticmethod
    def __is_sns_message__(content: Dict) -> bool:
        return 'Type' in content and content['Type'] == 'Notification'

    @staticmethod
    def __is_sqs_message__(content: Dict) -> bool:
        return ('id' in content and
                'topic' in content and
                'payload' in content)

    def parse_from_sns(self) -> Dict:
        payload = loads(self.body)
        if self.__is_sns_message__(payload):
            return self.__parse_from_sns__(payload)
        raise ValueError('The message is not a SNS message')

    def __parse_from_sns__(self, payload: Dict) -> Union[str, Dict]:
        self.topic = str(payload['TopicArn'].split(':')[-1]).lower()
        self.message_attributes = parse_message_attributes(
            payload.get('MessageAttributes', {}))
        try:
            return loads(payload['Message'])
        except Exception:
            return payload['Message']

    def parse(self) -> Optional[Dict]:
        content = loads(self.body)
        if self.__is_sns_message__(content):
            content = self.__parse_from_sns__(content)
        return content

    def __get_sqs_message__(self, content: Union[str, Dict]) -> SqsMessage:

        if isinstance(content, dict) and self.__is_sqs_message__(content):
            if 'correlation_id' not in content:
                content['correlation_id'] = str(self.get_correlation_id(content))
            return SqsMessage(
                id=UUID(content['id']),
                topic=content['topic'],
                payload=content['payload'],
                correlation_id=content['correlation_id'],
                timestamp=content.get('timestamp', datetime.now(timezone.utc).isoformat())
            )
        return SqsMessage(
            id=uuid4(),
            topic=self.topic,
            payload=content,
            correlation_id=self.get_correlation_id(content),
            timestamp=datetime.now(timezone.utc).isoformat()
        )

    def get_sqs_message(self) -> SqsMessage:
        try:
            content = loads(self.body)
        except Exception:
            return self.__get_sqs_message__(self.body)
        if self.__is_sns_message__(content):
            content = self.__parse_from_sns__(content)
        return self.__get_sqs_message__(content)

    @classmethod
    def from_boto_response(cls, response: Dict):
        return cls(
            message_id=response['MessageId'],
            receipt_handle=response['ReceiptHandle'],
            md5_of_body=response.get('MD5OfBody', ""),
            body=response['Body'],
            attributes=response['Attributes'],
            md5_of_message_attributes=response.get(
                'MD5OfMessageAttributes', ''),
            message_attributes=parse_message_attributes(
                response.get('MessageAttributes', {}))
        )
