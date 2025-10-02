from enum import Enum


class FlagsDocumentFormat(str, Enum):
    PI_JSON = "PI_JSON"

    def __str__(self) -> str:
        return str(self.value)
