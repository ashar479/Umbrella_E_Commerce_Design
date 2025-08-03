from typing import List, Dict
from customer import Customer
from order import Order
from event import Event

class Administrator:
    def __init__(self, admin_id: int):
        self.admin_id = admin_id
        self._customers: Dict[int, Customer] = {}
        self._orders: Dict[int, Order] = {}
        self._events: List[Event] = []

    def add_customer(self, customer: Customer):
        self._customers[customer.cust_id] = customer

    def add_order(self, order: Order):
        self._orders[order.order_id] = order

    def log_custom_event(self, event_type: str, customer_id: int, metadata: dict) -> Event:
        event = Event.create_event(event_type, customer_id, None, created_by=self.admin_id, metadata=metadata)
        self._events.append(event)
        return event

    def view_customer_events(self, customer_id: int) -> List[Event]:
        customer = self._customers.get(customer_id)
        return customer.get_event_history() if customer else []

    def get_dashboard_metrics(self) -> dict:
        return {
            "total_customers": len(self._customers),
            "total_orders": len(self._orders),
            "total_events": len(self._events)
        }