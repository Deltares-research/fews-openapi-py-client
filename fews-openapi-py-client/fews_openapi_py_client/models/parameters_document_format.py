from enum import Enum


class ParametersDocumentFormat(str, Enum):
    PI_JSON = "PI_JSON"
    PI_XML = "PI_XML"

    def __str__(self) -> str:
        return str(self.value)
