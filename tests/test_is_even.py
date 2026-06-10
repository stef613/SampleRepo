import unittest

from scripts.is_even import is_even


class TestIsEven(unittest.TestCase):
    def test_even_number(self) -> None:
        self.assertTrue(is_even(4))

    def test_odd_number(self) -> None:
        self.assertFalse(is_even(5))

    def test_zero_is_even(self) -> None:
        self.assertTrue(is_even(0))


if __name__ == "__main__":
    unittest.main()
