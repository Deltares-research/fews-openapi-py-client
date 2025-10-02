from enum import Enum


class ArchiveproductsDocumentFormat(str, Enum):
    BINARY = "BINARY"
    BINARY_ZIP = "BINARY_ZIP"

    def __str__(self) -> str:
        return str(self.value)
