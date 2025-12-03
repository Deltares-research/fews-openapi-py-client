from enum import Enum


class TimeseriesintervalstatisticsTimeSeriesType(str, Enum):
    EXTERNAL_FORECASTING = "EXTERNAL_FORECASTING"
    EXTERNAL_HISTORICAL = "EXTERNAL_HISTORICAL"
    SIMULATED_FORECASTING = "SIMULATED_FORECASTING"
    SIMULATED_HISTORICAL = "SIMULATED_HISTORICAL"

    def __str__(self) -> str:
        return str(self.value)
