from enums import OrderType, Status

class Order:
    def __init__(self, order_id: int, order_type: OrderType, customer_id: int, order_content: dict):
        self.order_id = order_id
        self.order_type = order_type
        self.customer_id = customer_id
        self.order_content = order_content
        self._status = Status.PENDING

    def mark_delivered(self) -> bool:
        self._status = Status.DELIVERED
        return True

    def resolve_complaint(self) -> bool:
        self._status = Status.RESOLVED
        return True

    def complete_return(self) -> bool:
        self._status = Status.RETURNED
        return True

    def get_status(self) -> Status:
        return self._status