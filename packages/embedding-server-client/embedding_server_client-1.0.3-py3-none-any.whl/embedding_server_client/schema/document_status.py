from enum import Enum


class DocumentInsertionStatus(Enum):
    """
    Enum that represent the insertion status of the Document.
    """
    SUCCESS = 1
    ERROR = 2


class RetrievalStatus(Enum):
    """
    Enum that represent the retrieval status of the Document.
    """
    SUCCESS = 1
    ERROR = 2
