"""Scientific calculator operations module."""

import math


def sqrt(value):
    """
    Calculate the square root of a number.
    
    Args:
        value: Number to calculate square root of
    
    Returns:
        Square root of the value
    
    Raises:
        ValueError: If value is negative
    """
    if value < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(value)


def sin(degrees):
    """
    Calculate sine of an angle in degrees.
    
    Args:
        degrees: Angle in degrees
    
    Returns:
        Sine of the angle
    """
    radians = math.radians(degrees)
    return math.sin(radians)


def cos(degrees):
    """
    Calculate cosine of an angle in degrees.
    
    Args:
        degrees: Angle in degrees
    
    Returns:
        Cosine of the angle
    """
    radians = math.radians(degrees)
    return math.cos(radians)


def tan(degrees):
    """
    Calculate tangent of an angle in degrees.
    
    Args:
        degrees: Angle in degrees
    
    Returns:
        Tangent of the angle
    """
    radians = math.radians(degrees)
    return math.tan(radians)


def log10(value):
    """
    Calculate base-10 logarithm of a number.
    
    Args:
        value: Number to calculate log10 of
    
    Returns:
        Base-10 logarithm of the value
    
    Raises:
        ValueError: If value is zero or negative
    """
    if value <= 0:
        raise ValueError("Cannot calculate logarithm of zero or negative number")
    return math.log10(value)


def ln(value):
    """
    Calculate natural logarithm (base-e) of a number.
    
    Args:
        value: Number to calculate ln of
    
    Returns:
        Natural logarithm of the value
    
    Raises:
        ValueError: If value is zero or negative
    """
    if value <= 0:
        raise ValueError("Cannot calculate logarithm of zero or negative number")
    return math.log(value)


def factorial(n):
    """
    Calculate factorial of a non-negative integer.
    
    Args:
        n: Non-negative integer
    
    Returns:
        Factorial of n (n!)
    
    Raises:
        ValueError: If n is negative or not an integer
    """
    if not isinstance(n, int) and not n.is_integer():
        raise ValueError("Factorial requires an integer value")
    
    n = int(n)
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    
    return math.factorial(n)

