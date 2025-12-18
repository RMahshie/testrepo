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
