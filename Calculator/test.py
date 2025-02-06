import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a Calculator instance for each test."""
        self.calculator = Calculator()
    
    def tearDown(self):
        """Clean up after each test."""
        del self.calculator

    def test_add(self):
        """Test the add method with various inputs."""
        test_cases = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
            (100, -100, 0),
            (0.1, 0.2, 0.3)
        ]
        for a, b, expected in test_cases:
            with self.subTest(f"{a} + {b}"):
                self.assertAlmostEqual(self.calculator.add(a, b), expected)