Testcase Lab: Positive and Negative Testing

1. Project Overview

This project demonstrates positive and negative testing in Python. It focuses on validating email addresses and ages to ensure that the program accepts valid inputs and rejects invalid ones.

The project uses pytest to run automated test cases and verify whether the validation functions behave as expected.

2. Project Structure
testcase-lab/
├── validators.py
├── test_positive.py
├── test_negative.py
└── README.md

3. Files Description

3.1.validators.py

Contains two validation functions:
validate_email(email): Checks whether an email address follows the expected format. Returns True for accepted inputs and raises a ValueError for invalid formats.
validate_age(age): Checks whether the age is an integer between 0 and 150. Raises a TypeError if the input is not an integer and a ValueError if the age is outside the allowed range.

3.2.test_positive.py

Contains positive test cases to verify that valid inputs are accepted.
The tests check:
Valid email addresses.
Email addresses containing subdomains.
Valid ages.
Boundary ages of 0 and 150.

3.3.test_negative.py

Contains negative test cases to verify that invalid inputs are rejected correctly.
The tests check:
Email addresses without an @ symbol.
Email addresses without a valid domain.
Negative ages.
Ages provided as strings.

The tests use pytest.raises() to verify that the expected exceptions are raised.

4. Requirements

Python 3
pytest

Install pytest if it is not already installed:
python -m pip install pytest

5. How to Run the Tests

Step 1: Navigate to the project folder
e.g. cd quiz-03
Step 2: Run test files
pytest test_positive.py -v
pytest test_negative.py -v
Step 4: Run all tests
pytest -v
This automatically discovers and runs the test files whose names begin with test_.

6. Expected Result

If all test cases pass, pytest displays a summary similar to: 5 passed
The actual number of passed tests depends on how many test cases are currently defined in the project.
