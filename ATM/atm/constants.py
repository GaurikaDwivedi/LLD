from enum import Enum

class CardStatus(Enum):
    ACTIVE = 0
    BLOCKED = 1
    COMPROMISED = 2
    ACCOUNT_CLOSED = 3
    NOT_YET_ACTIVATED = 4