"""Calculator package for basic arithmetic operations."""

from .operations import add, subtract, multiply, divide, power, modulo
from .calculator import Calculator

__version__ = "1.0.0"
__all__ = ["add", "subtract", "multiply", "divide", "power", "modulo", "Calculator"]
