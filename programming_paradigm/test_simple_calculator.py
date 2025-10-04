import unittest
from simple_calculator import SimpleCalculator

class TestCalculate(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(4,6), 10)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,5), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4,2), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(18, 6), 3)

if __name__ == "__main__":
    unittest.main()