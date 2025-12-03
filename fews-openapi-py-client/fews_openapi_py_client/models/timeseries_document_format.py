from enum import Enum


class TimeseriesDocumentFormat(str, Enum):
    BINARY = "BINARY"
    DD_JSON = "DD_JSON"
    NOOS_TEXT = "NOOS_TEXT"
    PI_CSV = "PI_CSV"
    PI_JSON = "PI_JSON"
    PI_NETCDF = "PI_NETCDF"
    PI_XML = "PI_XML"

    def __str__(self) -> str:
        return str(self.value)
