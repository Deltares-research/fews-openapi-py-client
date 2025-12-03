from enum import Enum


class TimeseriesdisplaygroupsDocumentFormat(str, Enum):
    DD_JSON = "DD_JSON"
    NOOS_TEXT = "NOOS_TEXT"
    PI_JSON = "PI_JSON"
    PI_XML = "PI_XML"

    def __str__(self) -> str:
        return str(self.value)
