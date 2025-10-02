from enum import Enum


class ArchivelocationsDocumentFormat(str, Enum):
    DD_JSON = "DD_JSON"
    GEO_JSON = "GEO_JSON"
    NAME_LIST = "NAME_LIST"
    PI_JSON = "PI_JSON"
    PI_XML = "PI_XML"

    def __str__(self) -> str:
        return str(self.value)
