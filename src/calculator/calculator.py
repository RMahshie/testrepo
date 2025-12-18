"""Calculator class that maintains state and history."""

from .operations import add, subtract, multiply, divide, power, modulo


class Calculator:
    """A calculator that can perform operations and track history."""
    
    def __init__(self):
        """Initialize calculator with empty history and result."""
        self.result = 0
        self.history = []
    
    def add(self, value):
        """Add value to current result."""
        self.result = add(self.result, value)
        self.history.append(f"Added {value}, result: {self.result}")
        return self.result
    
    def subtract(self, value):
        """Subtract value from current result."""
        self.result = subtract(self.result, value)
        self.history.append(f"Subtracted {value}, result: {self.result}")
        return self.result
    
    def multiply(self, value):
        """Multiply current result by value."""
        self.result = multiply(self.result, value)
        self.history.append(f"Multiplied by {value}, result: {self.result}")
        return self.result
    
    def divide(self, value):
        """Divide current result by value."""
        self.result = divide(self.result, value)
        self.history.append(f"Divided by {value}, result: {self.result}")
        return self.result
    
    def power(self, value):
        """Raise current result to the power of value."""
        self.result = power(self.result, value)
        self.history.append(f"Raised to power {value}, result: {self.result}")
        return self.result
    
    def modulo(self, value):
        """Get remainder of current result divided by value."""
        self.result = modulo(self.result, value)
        self.history.append(f"Modulo {value}, result: {self.result}")
        return self.result
    
    def clear(self):
        """Clear current result and history."""
        self.result = 0
        self.history = []
    
    def get_history(self):
        """Get calculation history."""
        return self.history
    
    def get_result(self):
        """Get current result."""
        return self.result
