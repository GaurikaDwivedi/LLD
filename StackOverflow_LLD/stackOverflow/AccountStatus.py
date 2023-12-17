from enum import Enum

class AccountStatus(Enum):
    ACTIVE = 0
    CLOSED = 1
    CANCELED = 2
    BLACKLISTED = 3
    BLOCKED = 4