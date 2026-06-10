import unittest

from scripts.string_reverse import reverse_text


class TestReverseText(unittest.TestCase):
    def test_reverse_basic_text(self) -> None:
        self.assertEqual(reverse_text("hello"), "olleh")

    def test_reverse_empty_text(self) -> None:
        self.assertEqual(reverse_text(""), "")


if __name__ == "__main__":
    unittest.main()
