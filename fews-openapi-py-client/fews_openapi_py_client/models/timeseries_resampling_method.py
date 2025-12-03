from enum import Enum


class TimeseriesResamplingMethod(str, Enum):
    INSTANTANEOUS = "instantaneous"
    MAXIMUM = "maximum"
    MEAN = "mean"
    MEAN_OVER_TIME = "mean_over_time"
    MINIMUM = "minimum"
    PERCENTILE = "percentile"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
