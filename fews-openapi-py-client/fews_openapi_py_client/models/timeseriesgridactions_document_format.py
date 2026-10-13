from enum import Enum


class TimeseriesgridactionsDocumentFormat(str, Enum):
    PI_CSV = "PI_CSV"
    PI_CSV_ID_AND_NAME = "PI_CSV_ID_AND_NAME"
    PI_JSON = "PI_JSON"
    PI_SSV = "PI_SSV"
    PI_SSV_ID_AND_NAME = "PI_SSV_ID_AND_NAME"

    def __str__(self) -> str:
        return str(self.value)
