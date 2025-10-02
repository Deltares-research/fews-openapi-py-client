from enum import Enum


class ParametersselectedDocumentFormat(str, Enum):
    PI_JSON = "PI_JSON"

    def __str__(self) -> str:
        return str(self.value)
