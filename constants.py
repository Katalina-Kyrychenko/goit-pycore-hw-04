from enum import Enum

class FileStatus(Enum):
    NOT_FOUND = "NOT_FOUND"
    NOT_A_FILE = "NOT_A_FILE"
    EMPTY = "EMPTY"
    ERROR = "ERROR",
    OK = "OK",
    CORRUPTED = "CORRUPTED"