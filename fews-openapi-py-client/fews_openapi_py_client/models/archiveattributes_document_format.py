from enum import Enum


class ArchiveattributesDocumentFormat(str, Enum):
    PI_JSON = "PI_JSON"
    PI_XML = "PI_XML"

    def __str__(self) -> str:
        return str(self.value)
