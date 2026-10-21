from enum import Enum


class TimeseriesgridNetcdfFormat(str, Enum):
    NETCDF3 = "netcdf3"
    NETCDF4 = "netcdf4"

    def __str__(self) -> str:
        return str(self.value)
