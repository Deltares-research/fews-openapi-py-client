from enum import Enum


class TimeseriesgridDocumentFormat(str, Enum):
    DD_JSON = "DD_JSON"
    NOOS_TEXT = "NOOS_TEXT"
    PI_CSV = "PI_CSV"
    PI_CSV_ID_AND_NAME = "PI_CSV_ID_AND_NAME"
    PI_JSON = "PI_JSON"
    PI_NETCDF = "PI_NETCDF"
    PI_SSV = "PI_SSV"
    PI_SSV_ID_AND_NAME = "PI_SSV_ID_AND_NAME"
    PI_XML = "PI_XML"

    def __str__(self) -> str:
        return str(self.value)
