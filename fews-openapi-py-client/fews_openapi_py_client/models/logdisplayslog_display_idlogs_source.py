from enum import Enum


class LogdisplayslogDisplayIdlogsSource(str, Enum):
    AI = "AI"
    FS = "FS"
    MC = "MC"

    def __str__(self) -> str:
        return str(self.value)
