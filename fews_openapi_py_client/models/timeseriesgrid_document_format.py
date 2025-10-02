from enum import Enum


class TimeseriesgridDocumentFormat(str, Enum):
    DD_JSON = "DD_JSON"
    NOOS_TEXT = "NOOS_TEXT"
    PI_CSV = "PI_CSV"
    PI_JSON = "PI_JSON"
    PI_XML = "PI_XML"

    def __str__(self) -> str:
        return str(self.value)
