from enum import Enum


class TimeseriesintervalstatisticsInterval(str, Enum):
    CALENDAR_DAY = "CALENDAR_DAY"
    CALENDAR_MONTH = "CALENDAR_MONTH"
    MONTH = "MONTH"
    WEEK_DAY = "WEEK_DAY"
    YEAR = "YEAR"

    def __str__(self) -> str:
        return str(self.value)
