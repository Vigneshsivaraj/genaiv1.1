from src_code.unit_test.calculation import calculator
import unittest

class TestCalculation(unittest.TestCase):
    def test_calculator(self):
        self.assertEqual(calculator('+', [99, 3, 3]), 105)

if (__name__ == '__main__'):
    unittest.main()
