Quiz 04

This quiz contains examples and tests demonstrating several Pytest features, including assertions for different data types, test organization, markers, skipped tests, and expected failures.

Files
test_collections.py — Collection assertions
test_floats.py — Floating-point assertions
shopping.py — Shopping module
test_shopping.py — Shopping module tests
pytest.ini — Pytest marker configuration
test_markers.py — Pytest markers
test_skips.py — Skipped tests
test_xfail.py — Expected failures

Run Tests

From the quiz-04 folder:

python -m pytest

Run a specific test file: python -m pytest test_shopping.py

Run with detailed output: python -m pytest -v

Run tests by marker: python -m pytest -m <marker_name>

Pytest will display the results, including passed, skipped, and expected-failure tests.