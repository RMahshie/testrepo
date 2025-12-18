"""Tests for Calculator class."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator.calculator import Calculator


def test_calculator_initialization():
    """Test calculator initializes with zero result."""
    calc = Calculator()
    assert calc.get_result() == 0
    assert calc.get_history() == []


def test_calculator_add():
    """Test calculator add method."""
    calc = Calculator()
    calc.add(5)
    assert calc.get_result() == 5
    calc.add(3)
    assert calc.get_result() == 8


def test_calculator_subtract():
    """Test calculator subtract method."""
    calc = Calculator()
    calc.add(10)
    calc.subtract(3)
    assert calc.get_result() == 7


def test_calculator_multiply():
    """Test calculator multiply method."""
    calc = Calculator()
    calc.add(5)
    calc.multiply(3)
    assert calc.get_result() == 15


def test_calculator_divide():
    """Test calculator divide method."""
    calc = Calculator()
    calc.add(10)
    calc.divide(2)
    assert calc.get_result() == 5


def test_calculator_history():
    """Test calculator tracks history."""
    calc = Calculator()
    calc.add(5)
    calc.multiply(2)
    calc.subtract(3)
    
    history = calc.get_history()
    assert len(history) == 3
    assert "Added 5" in history[0]
    assert "Multiplied by 2" in history[1]
    assert "Subtracted 3" in history[2]


def test_calculator_clear():
    """Test calculator clear method."""
    calc = Calculator()
    calc.add(10)
    calc.multiply(5)
    calc.clear()
    
    assert calc.get_result() == 0
    assert calc.get_history() == []


def test_calculator_divide_by_zero():
    """Test that dividing by zero raises ValueError."""
    calc = Calculator()
    calc.add(10)
    
    try:
        calc.divide(0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_calculator_power():
    """Test calculator power method."""
    calc = Calculator()
    calc.add(2)
    calc.power(3)
    assert calc.get_result() == 8
    
    calc.clear()
    calc.add(5)
    calc.power(2)
    assert calc.get_result() == 25


if __name__ == "__main__":
    test_calculator_initialization()
    test_calculator_add()
    test_calculator_subtract()
    test_calculator_multiply()
    test_calculator_divide()
    test_calculator_history()
    test_calculator_clear()
    test_calculator_divide_by_zero()
    test_calculator_power()
    print("All tests passed!")
