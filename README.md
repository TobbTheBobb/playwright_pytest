# playwright_python
Playwright Testing in Python

wabue test-collection for docker-container hosted as web on port 8443 locally/in local network.

## Requirements

- [Python 3](https://python.org)

## Prerequisites

- Create a virtual environment using

      python3 -m venv .env

- Activate the virtual environment as described in https://docs.python.org/3/library/venv.html#how-venvs-work, e.g.:

      source .env/bin/activate

- Install requirements

      pip3 -r requirements.txt

- Install required playwright components

      playwright install

## Usage

Set the environment variables `PYTEST_USER` and `PYTEST_PASSWORD` to a valid login for the membership page. Then run

    pytest [optional parameters] [optional filename containing tests]

to run all test functions with naming convention "test_*" in every "test_*.py" file by default.

Example:

    PYTEST_USER=givenname.name PYTEST_PASSWORD=secret pytest

# relevant optional parameters

- -v (verbose output)  
- -m [markname] (run only tests with [markname]-keyword markers have to be "registered" in the pytest.ini file) e.g. pytest -m login
- --lf (run only last failed tests)
- -x (abort testing after first fail)

# additional info:

- conftest.py contains fixtures which can be referenced by tests e.g. login_logout_sample_user
- Generate test-code via: playwright codegen --ignore-https-errors https://web:8443
