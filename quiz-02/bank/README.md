# Bank Tests

This section focuses on writing clear and maintainable tests for the bank module.

The main objectives are:

Apply the AAA (Arrange, Act, Assert) pattern rigorously.
Make tests independent of each other.
Write test names that clearly document the behavior being tested.

## How to Run

Open the terminal in the `bank` folder and run:

python -m pytest

To run the main bank tests:

python -m pytest test_bank.py

To run the individual test examples:

python -m pytest test_bad_example.py
python -m pytest test_dependent.py
python -m pytest test_independent.py
python -m pytest test_named.py