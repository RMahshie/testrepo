"""Basic arithmetic operations module."""

#hello
#hello again
#hello again again
#hello again again again
#hello again again again again
#hello again again again again again
#hello again again again again again again
def add(a, b):
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract b from a.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide a by b.
    
    Args:
        a: First number (numerator)
        b: Second number (denominator)
    
    Returns:
        Quotient of a and b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """
    Raise a to the power of b.
    
    Args:
        a: Base number
        b: Exponent
    
    Returns:
        a raised to the power of b (a^b)
    """
    return a ** b


def modulo(a, b):
    """
    Get remainder of a divided by b.
    
    Args:
        a: First number
        b: Second number (divisor)
    
    Returns:
        Remainder of a mod b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
