import unittest

class TestCalculation(unittest.TestCase):
    def test_calculator(self):
        from calculation import calculator
        self.assertEqual(calculator('+',[99,3,3]),105)

if(__name__ == '__main__'):
    unittest.main()