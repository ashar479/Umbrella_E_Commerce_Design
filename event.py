from datetime import datetime
from typing import Optional

class Event:
    def __init__(self, event_id: int, event_type: str, customer_id: int, order_id: Optional[int], created_by: int, metadata: dict):
        self.event_id = event_id
        self.event_type = event_type
        self.customer_id = customer_id
        self.order_id = order_id
        self.created_by = created_by
        self.created_at = datetime.now()
        self.metadata = metadata

    @staticmethod
    def create_event(event_type: str, customer_id: int, order_id: Optional[int], created_by: int, metadata: dict):
        event_id = int(datetime.utcnow().timestamp() * 1000)
        return Event(event_id, event_type, customer_id, order_id, created_by, metadata)

    def get_summary(self) -> str:
        return f"Event[{self.event_id}]: {self.event_type} for Customer {self.customer_id} on Order {self.order_id} - {self.metadata}"