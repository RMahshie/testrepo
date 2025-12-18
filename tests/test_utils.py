"""Tests for utility functions."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator.utils import format_result, validate_number, parse_input


def test_format_result():
    """Test result formatting."""
    assert format_result(3.14159, 2) == "3.14"
    assert format_result(3.14159, 3) == "3.142"
    assert format_result(5, 2) == "5"
    assert format_result(10.0, 1) == "10.0"


def test_validate_number():
    """Test number validation."""
    assert validate_number(5) == True
    assert validate_number("5") == True
    assert validate_number("5.5") == True
    assert validate_number("-3") == True
    assert validate_number("abc") == False
    assert validate_number(None) == False


def test_parse_input():
    """Test input parsing."""
    assert parse_input("5 + 3") == (5.0, '+', 3.0)
    assert parse_input("10 - 2") == (10.0, '-', 2.0)
    assert parse_input("4 * 3") == (4.0, '*', 3.0)
    assert parse_input("8 / 2") == (8.0, '/', 2.0)
    assert parse_input("5.5 + 2.5") == (5.5, '+', 2.5)
    assert parse_input("invalid") == None
    assert parse_input("5 +") == None


if __name__ == "__main__":
    test_format_result()
    test_validate_number()
    test_parse_input()
    print("All tests passed!")
