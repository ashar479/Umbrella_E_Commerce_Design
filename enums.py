from enum import Enum

class OrderType(Enum):
    STANDARD = 1
    RETURN = 2
    COMPLAINT = 3

class Status(Enum):
    PENDING = 0
    DELIVERED = 1
    RESOLVED = 2
    RETURNED = 3
    COMPLETED = 4