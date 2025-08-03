from typing import Dict, List, Optional
from event import Event
from order import Order
from enums import OrderType

class Customer:
    def __init__(self, cust_id: int, name: str, address: str):
        self.cust_id = cust_id
        self.name = name
        self.address = address
        self._order_map: Dict[int, Order] = {}
        self._event_list: List[Event] = []

    def place_order(self, order_content: dict) -> Order:
        order = Order(len(self._order_map) + 1, OrderType.STANDARD, self.cust_id, order_content)
        self._order_map[order.order_id] = order
        return order

    def file_complaint(self, order_id: int, reason: str) -> Event:
        event = Event.create_event("Complaint Filed", self.cust_id, order_id, created_by=self.cust_id, metadata={"reason": reason})
        self._event_list.append(event)
        return event

    def initiate_return(self, order_id: int, reason: str) -> Event:
        event = Event.create_event("Return Initiated", self.cust_id, order_id, created_by=self.cust_id, metadata={"reason": reason})
        self._event_list.append(event)
        return event

    def receive_gift(self, description: str) -> Event:
        event = Event.create_event("Gift Received", self.cust_id, None, created_by=self.cust_id, metadata={"description": description})
        self._event_list.append(event)
        return event

    def get_event_history(self) -> List[Event]:
        return self._event_list