"""Tests for basic arithmetic operations."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator.operations import add, subtract, multiply, divide, power, modulo


def test_add():
    """Test addition operation."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0


def test_subtract():
    """Test subtraction operation."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-1, -1) == 0
    assert subtract(10.5, 5.5) == 5.0


def test_multiply():
    """Test multiplication operation."""
    assert multiply(3, 4) == 12
    assert multiply(0, 10) == 0
    assert multiply(-2, 3) == -6
    assert multiply(2.5, 2) == 5.0


def test_divide():
    """Test division operation."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5


def test_divide_by_zero():
    """Test that dividing by zero raises ValueError."""
    try:
        divide(5, 0)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Cannot divide by zero" in str(e)


def test_power():
    """Test power operation."""
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1
    assert power(2, -1) == 0.5
    assert power(0.5, 2) == 0.25


def test_modulo():
    """Test modulo operation."""
    assert modulo(10, 3) == 1
    assert modulo(15, 5) == 0
    assert modulo(7, 2) == 1
    assert modulo(-10, 3) == 2


if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
    test_power()
    test_modulo()
    print("All tests passed!")
