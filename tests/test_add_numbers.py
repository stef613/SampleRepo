import unittest

from scripts.add_numbers import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_add_integers(self) -> None:
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_number(self) -> None:
        self.assertEqual(add_numbers(-2, 3), 1)

    def test_add_floats(self) -> None:
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3, places=7)


if __name__ == "__main__":
    unittest.main()
