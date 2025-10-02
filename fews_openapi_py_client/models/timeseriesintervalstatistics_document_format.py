from enum import Enum


class TimeseriesintervalstatisticsDocumentFormat(str, Enum):
    PI_JSON = "PI_JSON"

    def __str__(self) -> str:
        return str(self.value)
