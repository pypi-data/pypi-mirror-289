from finalsa.common.models import (
    SqsMessage, SqsReponse, parse_message_attributes,
    to_message_attributes, __version__)
import os
import sys
import uuid
import datetime
import decimal

from json import dumps
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


def test_version():
    assert __version__ is not None


def test_parse_message_attributes():
    attributes = {
        'string': {'Type': 'String', 'Value': 'test'},
        'number': {'Type': 'Number', 'Value': '1'},
        'binary': {'Type': 'Binary', 'Value': 'test'}
    }
    result = parse_message_attributes(attributes)
    assert result['string'] == 'test'
    assert result['number'] == 1
    assert result['binary'] == b'test'


def test_sqs_message():
    message = SqsMessage(
        id='123e4567-e89b-12d3-a456-426614174000',
        topic='test',
        payload='{"test": "test"}',
        correlation_id='123e4567-e89b-12d3-a456-426614174000'
    )
    assert str(message.id) == '123e4567-e89b-12d3-a456-426614174000'
    assert message.topic == 'test'
    assert message.get_payload() == {'test': 'test'}
    assert message.correlation_id == '123e4567-e89b-12d3-a456-426614174000'
    assert message.timestamp is not None
    assert message.to_dict() == {
        'id': '123e4567-e89b-12d3-a456-426614174000',
        'topic': 'test',
        'payload': {'test': 'test'},
        'correlation_id': '123e4567-e89b-12d3-a456-426614174000',
        'timestamp': message.timestamp.isoformat()
    }


def test_sqs_message_str():
    message = SqsMessage(
        id='123e4567-e89b-12d3-a456-426614174000',
        topic='test',
        payload='{"test: "test"}',
        correlation_id='123e4567-e89b-12d3-a456-426614174000'
    )
    assert str(message.id) == '123e4567-e89b-12d3-a456-426614174000'
    assert message.topic == 'test'
    assert message.correlation_id == '123e4567-e89b-12d3-a456-426614174000'
    assert message.timestamp is not None
    assert message.to_dict() == {
        'id': '123e4567-e89b-12d3-a456-426614174000',
        'topic': 'test',
        'payload': '{"test: "test"}',
        'correlation_id': '123e4567-e89b-12d3-a456-426614174000',
        'timestamp': message.timestamp.isoformat()
    }


def test_sqs_response():
    response = SqsReponse(
        message_id='test',
        receipt_handle='test',
        md5_of_body='test',
        body='test',
        attributes={'test': 'test',
                    'correlation_id': '123e4567-e89b-12d3-a456-426614174000'},
        topic='test',
        md5_of_message_attributes='test',
        message_attributes={'correlation_id': {'Type': 'String',
                                               'Value': '123e4567-e89b-12d3-a456-426614174000'}}

    )
    assert response.body == 'test'
    assert str(response.get_correlation_id()) == '123e4567-e89b-12d3-a456-426614174000'
    assert response.topic == 'test'


def test_sqs_response_from_boto_response():
    boto_response = {
        'MessageId': 'test',
        'ReceiptHandle': 'test',
        'MD5OfBody': 'test',
        'Body': 'test',
        'Attributes': {'test': 'test', 'correlation_id': '123e4567-e89b-12d3-a456-426614174000'},
        'MessageAttributes': {'correlation_id': {'Type': 'String', 'Value': '123e4567-e89b-12d3-a456-426614174000'}}

    }

    response = SqsReponse.from_boto_response(boto_response)
    assert response.body == 'test'
    assert str(response.get_correlation_id()) == '123e4567-e89b-12d3-a456-426614174000'
    assert response.topic == ''
    assert response.message_attributes == {
        'correlation_id': "123e4567-e89b-12d3-a456-426614174000"}
    assert response.attributes == {
        'test': 'test', 'correlation_id': '123e4567-e89b-12d3-a456-426614174000'}


def test_sqs_response_no_correlation_id():
    response = SqsReponse(
        message_id='test',
        receipt_handle='test',
        md5_of_body='test',
        body='test',
        attributes={'test': 'test'},
        topic='test',
        md5_of_message_attributes='test',
    )
    assert response.body == 'test'
    assert response.get_correlation_id() is not None
    assert response.topic == 'test'


def test_sqs_message_from_dict():

    message = SqsMessage(
        id='123e4567-e89b-12d3-a456-426614174000',
        topic='test',
        payload='{"test": "test"}',
        correlation_id='123e4567-e89b-12d3-a456-426614174000'
    )
    message_dict = message.to_dict()
    assert str(message.id) == message_dict['id']
    assert message.topic == message_dict['topic']
    assert message.get_payload() == {'test': 'test'}
    assert message.correlation_id == message_dict['correlation_id']


def test_to_message_attributes():
    attributes = {
        'string': 'test',
        'number': 1,
        'binary': b'test',
        'uuid': uuid.uuid4(),
        'datetime': datetime.datetime.now(),
        'decimal': decimal.Decimal('1.0')
    }
    result = to_message_attributes(attributes)
    assert result['string']['DataType'] == 'String'
    assert result['string']['StringValue'] == 'test'
    assert result['number']['DataType'] == 'Number'
    assert result['number']['StringValue'] == '1'
    assert result['binary']['DataType'] == 'Binary'
    assert result['binary']['BinaryValue'] == b'test'
    assert result['uuid']['DataType'] == 'String'
    assert result['uuid']['StringValue'] == str(attributes['uuid'])
    assert result['datetime']['DataType'] == 'String'
    assert result['datetime']['StringValue'] == attributes['datetime'].isoformat()
    assert result['decimal']['DataType'] == 'Number'
    assert result['decimal']['StringValue'] == '1.0'


def test_parse_from_sns_response():
    real_message_body = {
        "test": "test"
    }
    body = dumps({
        'Type': 'Notification',
        'TopicArn': 'mytopic',
        'Message': dumps(real_message_body),
        'MessageAttributes': {'correlation_id': {
            'Type': 'String', 'Value': '123e4567-e89b-12d3-a456-426614174000'
        }}
    })

    boto_response = {
        'MessageId': 'test',
        'ReceiptHandle': 'test',
        'MD5OfBody': 'test',
        'Body': body,
        'Attributes': {'test': 'test', 'correlation_id': '123e4567-e89b-12d3-a456-426614174000'},
        'MessageAttributes': {'correlation_id': {'Type': 'String', 'Value': '123e4567-e89b-12d3-a456-426614174000'}}

    }

    response = SqsReponse.from_boto_response(boto_response)
    assert response.body == body
    assert response.get_correlation_id() == '123e4567-e89b-12d3-a456-426614174000'
    assert response.topic == ''
    assert response.message_attributes == {
        'correlation_id': "123e4567-e89b-12d3-a456-426614174000"}
    assert response.attributes == {
        'test': 'test', 'correlation_id': '123e4567-e89b-12d3-a456-426614174000'}
    assert response.parse_from_sns() == real_message_body
    assert response.parse() == real_message_body


def test_parse_from_sns_response_sqs_message():
    real_message_body = {
        "id": "123e4567-e89b-12d3-a456-426614174000",
    }
    sqs_message_payload = {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "topic": "test",
        "payload": dumps(real_message_body),
        "correlation_id": "123e4567-e89b-12d3-a456-426614174000",
        "timestamp": datetime.datetime.now().isoformat()
    }
    body = dumps({
        'Type': 'Notification',
        'TopicArn': 'mytopic',
        'Message': dumps(sqs_message_payload),
        'MessageAttributes': {'correlation_id': {
            'Type': 'String', 'Value': '123e4567-e89b-12d3-a456-426614174000'
        }}
    })

    boto_response = {
        'MessageId': 'test',
        'ReceiptHandle': 'test',
        'MD5OfBody': 'test',
        'Body': body,
        'Attributes': {'test': 'test', 'correlation_id': '123e4567-e89b-12d3-a456-426614174000'},
        'MessageAttributes': {'correlation_id': {'Type': 'String', 'Value': '123e4567-e89b-12d3-a456-426614174000'}}
    }

    response = SqsReponse.from_boto_response(boto_response)
    assert response.body == body
    assert response.get_correlation_id() == '123e4567-e89b-12d3-a456-426614174000'
    assert response.topic == ''
    assert response.message_attributes == {
        'correlation_id': "123e4567-e89b-12d3-a456-426614174000"}
    assert response.attributes == {
        'test': 'test', 'correlation_id': '123e4567-e89b-12d3-a456-426614174000'}
    sqs_message = response.get_sqs_message()
    assert sqs_message.id == uuid.UUID(sqs_message_payload['id'])
    assert sqs_message.topic == sqs_message_payload['topic']
    assert sqs_message.get_payload() == real_message_body
    assert sqs_message.correlation_id == sqs_message_payload['correlation_id']
    assert sqs_message.timestamp.isoformat() == sqs_message_payload['timestamp']


def test_parse_from_sqs_response_sqs_message():
    real_message_body = {
        "id": "123e4567-e89b-12d3-a456-426614174000",
    }
    sqs_message_payload = {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "topic": "test",
        "payload": dumps(real_message_body),
        "correlation_id": "123e4567-e89b-12d3-a456-426614174000",
        "timestamp": datetime.datetime.now().isoformat()
    }
    body = dumps(sqs_message_payload)
    boto_response = {
        'MessageId': 'test',
        'ReceiptHandle': 'test',
        'MD5OfBody': 'test',
        'Body': body,
        'Attributes': {'test': 'test', 'correlation_id': '123e4567-e89b-12d3-a456-426614174000'},
        'MessageAttributes': {'correlation_id': {'Type': 'String', 'Value': '123e4567-e89b-12d3-a456-426614174000'}}
    }

    response = SqsReponse.from_boto_response(boto_response)
    assert response.body == body
    assert response.get_correlation_id() == '123e4567-e89b-12d3-a456-426614174000'
    assert response.topic == ''
    assert response.message_attributes == {
        'correlation_id': "123e4567-e89b-12d3-a456-426614174000"}
    assert response.attributes == {
        'test': 'test', 'correlation_id': '123e4567-e89b-12d3-a456-426614174000'}
    sqs_message = response.get_sqs_message()
    assert sqs_message.id == uuid.UUID(sqs_message_payload['id'])
    assert sqs_message.topic == sqs_message_payload['topic']
    assert sqs_message.get_payload() == real_message_body
    assert sqs_message.correlation_id == sqs_message_payload['correlation_id']
    assert sqs_message.timestamp.isoformat() == sqs_message_payload['timestamp']


def test_parse_from_sns_response_non_valid_sqs_message():
    real_message_body = {
        "id": "123e4567-e89b-12d3-a456-426614174000",
    }

    body = dumps({
        'Type': 'Notification',
        'TopicArn': 'mytopic',
        'Message': dumps(real_message_body),
        'MessageAttributes': {'correlation_id': {
            'Type': 'String', 'Value': '123e4567-e89b-12d3-a456-426614174000'
        }}
    })

    boto_response = {
        'MessageId': 'test',
        'ReceiptHandle': 'test',
        'MD5OfBody': 'test',
        'Body': body,
        'Attributes': {'test': 'test', 'correlation_id': '123e4567-e89b-12d3-a456-426614174000'},
        'MessageAttributes': {'correlation_id': {'Type': 'String', 'Value': '123e4567-e89b-12d3-a456-426614174000'}}
    }

    response = SqsReponse.from_boto_response(boto_response)
    assert response.body == body
    assert response.get_correlation_id() == '123e4567-e89b-12d3-a456-426614174000'
    assert response.topic == ''
    assert response.message_attributes == {
        'correlation_id': "123e4567-e89b-12d3-a456-426614174000"}
    assert response.attributes == {
        'test': 'test', 'correlation_id': '123e4567-e89b-12d3-a456-426614174000'}
    sqs_message = response.get_sqs_message()
    assert sqs_message.id is not None
    assert sqs_message.get_payload() == real_message_body
    assert sqs_message.correlation_id == '123e4567-e89b-12d3-a456-426614174000'
    assert sqs_message.timestamp is not None
    assert sqs_message.topic == 'mytopic'



def test_parse_from_sns_response_non_valid_str_sqs_message():
    real_message_body = "a"
    body = dumps({
        'Type': 'Notification',
        'TopicArn': 'mytopic',
        'Message': real_message_body,
        'MessageAttributes': {'correlation_id': {
            'Type': 'String', 'Value': '123e4567-e89b-12d3-a456-426614174000'
        }}
    })

    boto_response = {
        'MessageId': 'test',
        'ReceiptHandle': 'test',
        'MD5OfBody': 'test',
        'Body': body,
        'Attributes': {'test': 'test', 'correlation_id': '123e4567-e89b-12d3-a456-426614174000'},
        'MessageAttributes': {'correlation_id': {'Type': 'String', 'Value': '123e4567-e89b-12d3-a456-426614174000'}}
    }

    response = SqsReponse.from_boto_response(boto_response)
    assert response.body == body
    assert response.get_correlation_id() == '123e4567-e89b-12d3-a456-426614174000'
    assert response.topic == ''
    assert response.message_attributes == {
        'correlation_id': "123e4567-e89b-12d3-a456-426614174000"}
    assert response.attributes == {
        'test': 'test', 'correlation_id': '123e4567-e89b-12d3-a456-426614174000'}
    sqs_message = response.get_sqs_message()
    assert sqs_message.id is not None
    assert sqs_message.payload == real_message_body
    assert sqs_message.correlation_id == '123e4567-e89b-12d3-a456-426614174000'
    assert sqs_message.timestamp is not None
    assert sqs_message.topic == 'mytopic'
