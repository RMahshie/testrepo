# Simple Calculator Application

A well-structured Python calculator application for testing and demonstration purposes.

## Project Structure

```
testrepo/
├── src/
│   ├── calculator/
│   │   ├── __init__.py       # Package initialization
│   │   ├── operations.py     # Basic arithmetic operations
│   │   ├── calculator.py     # Calculator class with history
│   │   └── utils.py          # Utility functions
│   └── main.py               # Main application entry point
├── tests/
│   ├── __init__.py
│   ├── test_operations.py    # Tests for operations
│   ├── test_calculator.py    # Tests for Calculator class
│   └── test_utils.py         # Tests for utilities
├── setup.py                  # Package setup configuration
├── requirements.txt          # Project dependencies
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Features

- **Basic Operations**: Add, subtract, multiply, divide, and power/exponentiation
- **Calculator Class**: Stateful calculator with history tracking
- **Interactive Mode**: Multiple user interface modes
- **Comprehensive Tests**: Full test coverage for all modules
- **Clean Code**: Well-documented and organized

## Installation

1. Clone the repository:
```bash
git clone https://github.com/RMahshie/testrepo.git
cd testrepo
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package:
```bash
pip install -e .
```

## Usage

### Run the Application

```bash
cd src
python main.py
```

### Using the Calculator Module

```python
from calculator import Calculator, add, subtract, multiply, divide

# Use basic operations
result = add(5, 3)  # Returns 8
result = multiply(4, 7)  # Returns 28

# Use Calculator class with history
calc = Calculator()
calc.add(10)
calc.multiply(2)
calc.subtract(5)
print(calc.get_result())  # 15
print(calc.get_history())  # See operation history
```

## Running Tests

Run all tests:
```bash
cd tests
python test_operations.py
python test_calculator.py
python test_utils.py
```

Or run them all together:
```bash
cd tests
python -m pytest
```

## Module Documentation

### calculator.operations
Basic arithmetic functions:
- `add(a, b)` - Add two numbers
- `subtract(a, b)` - Subtract b from a
- `multiply(a, b)` - Multiply two numbers
- `divide(a, b)` - Divide a by b (raises ValueError if b is 0)
- `power(a, b)` - Raise a to the power of b (a^b)

### calculator.calculator
`Calculator` class for stateful operations:
- `add(value)` - Add to current result
- `subtract(value)` - Subtract from current result
- `multiply(value)` - Multiply current result
- `divide(value)` - Divide current result
- `power(value)` - Raise current result to the power of value
- `clear()` - Reset calculator
- `get_result()` - Get current result
- `get_history()` - Get operation history

### calculator.utils
Utility functions:
- `format_result(value, precision)` - Format numeric output
- `validate_number(value)` - Check if value is valid number
- `parse_input(user_input)` - Parse expression string

## License

This is a test repository for demonstration purposes.