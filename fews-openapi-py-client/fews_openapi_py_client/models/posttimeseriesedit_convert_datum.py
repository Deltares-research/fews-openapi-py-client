from enum import Enum


class PosttimeserieseditConvertDatum(str, Enum):
    FALSE = "false"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
