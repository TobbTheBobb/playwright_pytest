# playwright_python
Playwright Testing in Python

wabue test-collection for docker-container hosted as web on port 8443 locally/in local network.
requires: 
- python3 installed
- pip install playwright
- pip install pytest 
- "playwright install" to be run once before executed.
cd into playwright_python
run pytest-command

# pytest-command syntax

pytest [optional parameters] [optional filename containing tests]

runs all test functions with naming convention "test_*" in every "test_*.py" file by default.

# relevant optional parameters
  -v (verbose output)
  
  -m [markname] (run only tests with [markname]-keyword markers have to be "registered" in the pytest.ini file) e.g. pytest -m login
  
  --lf (run only last failed tests)
  
  -x (abort testing after first fail)

# additional info:
- conftest.py contains fixtures which can be referenced by tests e.g. login_logout_sample_user
- Generate test-code via: playwright codegen --ignore-https-errors https://web:8443
