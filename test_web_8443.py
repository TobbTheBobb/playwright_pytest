""" 
wabue test-collection for docker-container hosted as web on port 8443 locally/in local network.
requires: 
- python3 installed
- pip install playwright
- pip install pytest 
- "playwright install" to be run once before executed.

cd into playwright_python
run pytest-command

pytest-command syntax:
pytest <optional parameters> <optional filename containing tests> (runs all test functions with naming convention "test_*" in every "test_*.py" file by default.)

relevant optional parameters:
-v (verbose output)
-m <markname> (run only tests with <markname>-keyword markers have to be "registered" in the pytest.ini file) e.g. pytest -m login
--lf (run only last failed tests)
-x (abort testing after first fail)

###
###additional info:
###
conftest.py contains fixtures which can be referenced by tests e.g. login_logout_sample_user

Generate test-code via:
playwright codegen --ignore-https-errors https://web:8443

"""
###
###Imports
###

from playwright.sync_api import expect
import pytest
from basic_functions import *


#login is working
@pytest.mark.login
def test_login(login_logout_sample_user) -> None:
    page=login_logout_sample_user
    activity_heading=page.locator("//h2[text()='Alle Aktivitäten']")
    assert activity_heading.is_visible(), "Fehler bei Login - \"Alle Aktivitäten\" wird nicht angezeigt"

#basic navigation and search is working
@pytest.mark.login
@pytest.mark.basic
def test_basic_navigation_and_search(login_logout_sample_user) -> None:
    page=login_logout_sample_user
    b_nav_all(page)
    b_search_test(page)


###
###dummy tests
###

#dummy to skip
@pytest.mark.skip(reason="Skippady-skabbady")
def test_login_skip(login_logout_sample_user) -> None:
    page=login_logout_sample_user
    expect(page).to_have_url("https://web:8443/gibtesNICHTERRORSKIP")

#dummy to fail
# @pytest.mark.xfail(reason="Das ist ein gewollter fail")
# def test_login_fail(login_logout_sample_user) -> None:
#     page=login_logout_sample_user
#     expect(page).to_have_url("https://web:8443/gibtesNICHTERRORSKIP")