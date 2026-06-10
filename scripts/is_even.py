"""Check whether a number is even."""

import argparse


def is_even(number: int) -> bool:
    return number % 2 == 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Check if a number is even.")
    parser.add_argument("number", type=int, help="Number to check")
    args = parser.parse_args()
    print("even" if is_even(args.number) else "odd")


if __name__ == "__main__":
    main()
