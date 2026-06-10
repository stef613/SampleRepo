"""Reverse text from the command line."""

import argparse


def reverse_text(text: str) -> str:
    return text[::-1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Reverse text.")
    parser.add_argument("text", help="Text to reverse")
    args = parser.parse_args()
    print(reverse_text(args.text))


if __name__ == "__main__":
    main()
