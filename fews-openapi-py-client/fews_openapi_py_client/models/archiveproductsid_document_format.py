from enum import Enum


class ArchiveproductsidDocumentFormat(str, Enum):
    BINARY = "BINARY"

    def __str__(self) -> str:
        return str(self.value)
