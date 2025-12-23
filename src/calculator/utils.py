"""Utility functions for the calculator application."""


def format_result(value, precision=2):
    """
    Format a numeric result for display.
    
    Args:
        value: Numeric value to format
        precision: Number of decimal places (default: 2)
    
    Returns:
        Formatted string representation of the value
    """
    if isinstance(value, float):
        return f"{value:.{precision}f}"
    return str(value)


def validate_number(value):
    """
    Validate that a value can be used in calculations.
    
    Args:
        value: Value to validate
    
    Returns:
        True if valid, False otherwise
    """
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def parse_input(user_input):
    """
    Parse user input string to extract operation and operands.
    
    Args:
        user_input: String input from user (e.g., "5 + 3")
    
    Returns:
        Tuple of (operand1, operator, operand2) or None if invalid
    """
    parts = user_input.strip().split()
    if len(parts) != 3:
        return None
    
    try:
        operand1 = float(parts[0])
        operator = parts[1]
        operand2 = float(parts[2])
        return (operand1, operator, operand2)
    except (ValueError, IndexError):
        return None


def format_scientific(value, threshold=1e6):
    """
    Format number in scientific notation if it's very large or very small.
    
    Args:
        value: Numeric value to format
        threshold: Threshold for using scientific notation (default: 1,000,000)
    
    Returns:
        Formatted string in scientific notation if needed, regular format otherwise
    """
    if not isinstance(value, (int, float)):
        return str(value)
    
    abs_value = abs(value)
    
    # Use scientific notation for very large or very small numbers
    if abs_value >= threshold or (abs_value < 1e-4 and abs_value != 0):
        return f"{value:.4e}"
    
    return format_result(value)
