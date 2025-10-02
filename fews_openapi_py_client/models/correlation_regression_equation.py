from enum import Enum


class CorrelationRegressionEquation(str, Enum):
    EXPONENTIAL_MULTIPLY = "exponential multiply"
    HYPERBOLIC = "hyperbolic"
    LOGARITHMIC = "logarithmic"
    MULTIPLE_LINEAR = "multiple linear"
    POWER = "power"
    SIMPLE_LINEAR = "simple linear"

    def __str__(self) -> str:
        return str(self.value)
