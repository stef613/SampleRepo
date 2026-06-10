# SampleRepo

This repository contains a few basic Python scripts and unit tests.

## Scripts

The scripts live in `/home/runner/work/SampleRepo/SampleRepo/katgit/SampleRepo/scripts`:

- `add_numbers.py`: adds two numbers
- `string_reverse.py`: reverses a string
- `is_even.py`: checks if an integer is even

## How to run the scripts

From the repository root (`/home/runner/work/SampleRepo/SampleRepo/katgit/SampleRepo`):

```bash
python scripts/add_numbers.py 2 3
python scripts/string_reverse.py hello
python scripts/is_even.py 8
```

## Run unit tests

```bash
python -m unittest discover -s tests -q
```
