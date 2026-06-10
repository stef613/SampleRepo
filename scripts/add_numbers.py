"""Add two numbers from the command line."""

import argparse


def add_numbers(a: float, b: float) -> float:
    return a + b


def main() -> None:
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()
    print(add_numbers(args.a, args.b))


if __name__ == "__main__":
    main()
