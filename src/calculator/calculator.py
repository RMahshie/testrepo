"""Calculator class that maintains state and history."""

from .operations import add, subtract, multiply, divide, power, modulo
from .scientific import sqrt, sin, cos, tan, log10, ln, factorial


class Calculator:
    """A calculator that can perform operations and track history."""
    
    def __init__(self):
        """Initialize calculator with empty history and result."""
        self.result = 0
        self.history = []
        self.memory = 0
    
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
    
    # Scientific operations
    def sqrt(self):
        """Calculate square root of current result."""
        self.result = sqrt(self.result)
        self.history.append(f"Square root, result: {self.result}")
        return self.result
    
    def sin(self):
        """Calculate sine of current result (in degrees)."""
        self.result = sin(self.result)
        self.history.append(f"Sine, result: {self.result}")
        return self.result
    
    def cos(self):
        """Calculate cosine of current result (in degrees)."""
        self.result = cos(self.result)
        self.history.append(f"Cosine, result: {self.result}")
        return self.result
    
    def tan(self):
        """Calculate tangent of current result (in degrees)."""
        self.result = tan(self.result)
        self.history.append(f"Tangent, result: {self.result}")
        return self.result
    
    def log10(self):
        """Calculate base-10 logarithm of current result."""
        self.result = log10(self.result)
        self.history.append(f"Log10, result: {self.result}")
        return self.result
    
    def ln(self):
        """Calculate natural logarithm of current result."""
        self.result = ln(self.result)
        self.history.append(f"Natural log, result: {self.result}")
        return self.result
    
    def factorial(self):
        """Calculate factorial of current result."""
        self.result = factorial(self.result)
        self.history.append(f"Factorial, result: {self.result}")
        return self.result
    
    # Memory operations
    def memory_store(self):
        """Store current result in memory."""
        self.memory = self.result
        self.history.append(f"Stored {self.result} in memory")
    
    def memory_recall(self):
        """Recall value from memory and set as current result."""
        self.result = self.memory
        self.history.append(f"Recalled {self.memory} from memory")
        return self.result
    
    def memory_clear(self):
        """Clear memory."""
        self.memory = 0
        self.history.append("Memory cleared")
    
    def memory_add(self):
        """Add current result to memory."""
        self.memory += self.result
        self.history.append(f"Added {self.result} to memory, memory now: {self.memory}")
    
    def get_memory(self):
        """Get current memory value."""
        return self.memory
