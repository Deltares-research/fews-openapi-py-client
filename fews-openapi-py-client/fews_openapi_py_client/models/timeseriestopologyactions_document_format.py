from enum import Enum


class TimeseriestopologyactionsDocumentFormat(str, Enum):
    PI_CSV = "PI_CSV"
    PI_CSV_ID_AND_NAME = "PI_CSV_ID_AND_NAME"
    PI_JSON = "PI_JSON"
    PI_SSV = "PI_SSV"
    PI_SSV_ID_AND_NAME = "PI_SSV_ID_AND_NAME"
    PI_XML = "PI_XML"

    def __str__(self) -> str:
        return str(self.value)
