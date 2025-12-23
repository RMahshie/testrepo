"""Test suite for scientific calculator operations."""

import unittest
import math
from src.calculator.scientific import sqrt, sin, cos, tan, log10, ln, factorial
from src.calculator.calculator import Calculator


class TestScientificOperations(unittest.TestCase):
    """Test scientific operation functions."""
    
    def test_sqrt_positive(self):
        """Test square root of positive numbers."""
        self.assertAlmostEqual(sqrt(4), 2.0)
        self.assertAlmostEqual(sqrt(9), 3.0)
        self.assertAlmostEqual(sqrt(2), 1.414213562, places=5)
    
    def test_sqrt_zero(self):
        """Test square root of zero."""
        self.assertEqual(sqrt(0), 0.0)
    
    def test_sqrt_negative_raises_error(self):
        """Test square root of negative number raises ValueError."""
        with self.assertRaises(ValueError):
            sqrt(-1)
    
    def test_sin_basic_angles(self):
        """Test sine of basic angles."""
        self.assertAlmostEqual(sin(0), 0.0)
        self.assertAlmostEqual(sin(30), 0.5)
        self.assertAlmostEqual(sin(90), 1.0)
    
    def test_cos_basic_angles(self):
        """Test cosine of basic angles."""
        self.assertAlmostEqual(cos(0), 1.0)
        self.assertAlmostEqual(cos(60), 0.5)
        self.assertAlmostEqual(cos(90), 0.0, places=5)
    
    def test_tan_basic_angles(self):
        """Test tangent of basic angles."""
        self.assertAlmostEqual(tan(0), 0.0)
        self.assertAlmostEqual(tan(45), 1.0)
    
    def test_log10_positive(self):
        """Test base-10 logarithm of positive numbers."""
        self.assertAlmostEqual(log10(1), 0.0)
        self.assertAlmostEqual(log10(10), 1.0)
        self.assertAlmostEqual(log10(100), 2.0)
        self.assertAlmostEqual(log10(1000), 3.0)
    
    def test_log10_zero_raises_error(self):
        """Test log10 of zero raises ValueError."""
        with self.assertRaises(ValueError):
            log10(0)
    
    def test_log10_negative_raises_error(self):
        """Test log10 of negative number raises ValueError."""
        with self.assertRaises(ValueError):
            log10(-1)
    
    def test_ln_positive(self):
        """Test natural logarithm of positive numbers."""
        self.assertAlmostEqual(ln(1), 0.0)
        self.assertAlmostEqual(ln(math.e), 1.0)
        self.assertAlmostEqual(ln(math.e ** 2), 2.0)
    
    def test_ln_zero_raises_error(self):
        """Test ln of zero raises ValueError."""
        with self.assertRaises(ValueError):
            ln(0)
    
    def test_ln_negative_raises_error(self):
        """Test ln of negative number raises ValueError."""
        with self.assertRaises(ValueError):
            ln(-1)
    
    def test_factorial_small_numbers(self):
        """Test factorial of small numbers."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
    
    def test_factorial_float_integer(self):
        """Test factorial of float that represents an integer."""
        self.assertEqual(factorial(5.0), 120)
    
    def test_factorial_negative_raises_error(self):
        """Test factorial of negative number raises ValueError."""
        with self.assertRaises(ValueError):
            factorial(-1)
    
    def test_factorial_non_integer_raises_error(self):
        """Test factorial of non-integer raises ValueError."""
        with self.assertRaises(ValueError):
            factorial(5.5)


class TestCalculatorScientific(unittest.TestCase):
    """Test Calculator class with scientific operations."""
    
    def setUp(self):
        """Create a new calculator for each test."""
        self.calc = Calculator()
    
    def test_sqrt_method(self):
        """Test Calculator sqrt method."""
        self.calc.add(16)
        result = self.calc.sqrt()
        self.assertAlmostEqual(result, 4.0)
    
    def test_sin_method(self):
        """Test Calculator sin method."""
        self.calc.add(30)
        result = self.calc.sin()
        self.assertAlmostEqual(result, 0.5)
    
    def test_cos_method(self):
        """Test Calculator cos method."""
        self.calc.add(60)
        result = self.calc.cos()
        self.assertAlmostEqual(result, 0.5)
    
    def test_tan_method(self):
        """Test Calculator tan method."""
        self.calc.add(45)
        result = self.calc.tan()
        self.assertAlmostEqual(result, 1.0)
    
    def test_log10_method(self):
        """Test Calculator log10 method."""
        self.calc.add(100)
        result = self.calc.log10()
        self.assertAlmostEqual(result, 2.0)
    
    def test_ln_method(self):
        """Test Calculator ln method."""
        self.calc.add(math.e)
        result = self.calc.ln()
        self.assertAlmostEqual(result, 1.0)
    
    def test_factorial_method(self):
        """Test Calculator factorial method."""
        self.calc.add(5)
        result = self.calc.factorial()
        self.assertEqual(result, 120)


class TestCalculatorMemory(unittest.TestCase):
    """Test Calculator memory functions."""
    
    def setUp(self):
        """Create a new calculator for each test."""
        self.calc = Calculator()
    
    def test_memory_store(self):
        """Test storing value in memory."""
        self.calc.add(42)
        self.calc.memory_store()
        self.assertEqual(self.calc.get_memory(), 42)
    
    def test_memory_recall(self):
        """Test recalling value from memory."""
        self.calc.add(42)
        self.calc.memory_store()
        self.calc.clear()
        self.assertEqual(self.calc.get_result(), 0)
        self.calc.memory_recall()
        self.assertEqual(self.calc.get_result(), 42)
    
    def test_memory_clear(self):
        """Test clearing memory."""
        self.calc.add(42)
        self.calc.memory_store()
        self.calc.memory_clear()
        self.assertEqual(self.calc.get_memory(), 0)
    
    def test_memory_add(self):
        """Test adding to memory."""
        self.calc.add(10)
        self.calc.memory_store()
        self.calc.add(5)
        self.calc.memory_add()
        self.assertEqual(self.calc.get_memory(), 25)
    
    def test_memory_persists_after_clear(self):
        """Test that memory persists after clearing result."""
        self.calc.add(100)
        self.calc.memory_store()
        self.calc.clear()
        self.assertEqual(self.calc.get_memory(), 100)


if __name__ == '__main__':
    unittest.main()

