from enum import Enum


class LogdisplayslogDisplayIdlogsLogType(str, Enum):
    MANUAL = "manual"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
