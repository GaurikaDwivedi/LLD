from enum import Enum
from indexes.index import Index, FuzzyIndex


class IndexType(Enum):
    REVERSE = Index
    FUZZY = FuzzyIndex
