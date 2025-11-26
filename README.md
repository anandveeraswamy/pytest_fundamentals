# Fundamentals of Unit Testing with Pytest

## Overview
This repository introduces the basics of unit testing in Python using **pytest**. The examples included illustrate how to test simple functions, handle floating-point comparison, validate inputs, and write tests for normal behaviour as well as edge cases.

---

## Learning Outcomes
By the end of this exercise you will be able to:

- Understand how to test simple functions using unit tests.
- Learn why floating-point values need approximate comparisons.
- Recognise the importance of input validation and error handling.
- Write tests that check both normal behaviour and edge cases.
- Learn about pytest standard discovery.

---

## Setup Instructions

### 1. Create and activate a virtual environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Install the required dependencies
```bash
pip install -r requirements.txt
```

---

### 3. Run the tests
```bash
pytest
```

---

## Notes
- Make sure you are inside the virtual environment before running any commands.
- Pytest will automatically discover test files named in the format `test_*.py` or `*_test.py`.
- For more information go to https://docs.pytest.org/en/stable/getting-started.html
