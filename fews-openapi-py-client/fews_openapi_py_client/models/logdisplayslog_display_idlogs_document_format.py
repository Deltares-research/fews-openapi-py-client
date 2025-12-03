from enum import Enum


class LogdisplayslogDisplayIdlogsDocumentFormat(str, Enum):
    PI_JSON = "PI_JSON"

    def __str__(self) -> str:
        return str(self.value)
