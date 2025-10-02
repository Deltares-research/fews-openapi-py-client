from enum import Enum


class TimeseriesdisplaygroupsOmitMissing(str, Enum):
    FALSE = "false"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
