from enum import Enum


class TimeseriesgridactionsDocumentFormat(str, Enum):
    PI_CSV = "PI_CSV"
    PI_JSON = "PI_JSON"

    def __str__(self) -> str:
        return str(self.value)
