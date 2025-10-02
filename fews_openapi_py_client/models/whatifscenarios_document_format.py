from enum import Enum


class WhatifscenariosDocumentFormat(str, Enum):
    PI_JSON = "PI_JSON"

    def __str__(self) -> str:
        return str(self.value)
