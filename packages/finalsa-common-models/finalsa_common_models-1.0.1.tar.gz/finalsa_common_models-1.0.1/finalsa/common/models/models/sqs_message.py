from datetime import datetime, timezone
from typing import Optional, Union, Dict
from uuid import UUID
from pydantic import BaseModel
from json import loads


class SqsMessage(BaseModel):
    id: UUID
    topic: str
    payload: Union[str, Dict]
    correlation_id: str
    timestamp: Optional[datetime] = datetime.now(timezone.utc)

    def get_payload(self) -> Dict:
        if isinstance(self.payload, str):
            self.payload = loads(self.payload)
        return self.payload

    def to_dict(self):
        return {
            'id': str(self.id),
            'topic': self.topic,
            'payload': self.payload,
            'correlation_id': self.correlation_id,
            'timestamp': self.timestamp.isoformat()
        }
