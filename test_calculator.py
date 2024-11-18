import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    # Method add
    def test_add_1(self):
        self.assertEqual(self.calc.add(1, 0), 1)
    def test_add_2(self):
        self.assertEqual(self.calc.add(-1, 0), -1)

    # Method substract
    def test_substract_1(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
    def test_substract_2(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)
    
    # Method multiply
    def test_multiply_1(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)
    
    # Method divide
    def test_divide_1(self):
        self.assertEqual(self.calc.divide(5, 1), 5)
    def test_divide_2(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    # Method modulo
    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
    def test_modulo_1(self):
        self.assertEqual(self.calc.modulo(5, 1), 0)

if __name__ == '__main__':
    unittest.main()