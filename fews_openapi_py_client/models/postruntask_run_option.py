from enum import Enum


class PostruntaskRunOption(str, Enum):
    ALL = "all"
    ALLMOSTRECENTONLY = "allmostrecentonly"
    ALLONEATATIME = "alloneatatime"

    def __str__(self) -> str:
        return str(self.value)
