from enum import Enum


class SamplesDocumentFormat(str, Enum):
    PI_XML = "PI_XML"

    def __str__(self) -> str:
        return str(self.value)
