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

###
###login tests
###

#login is working
@pytest.mark.login
def test_login(login_logout_sample_user) -> None:
    page=login_logout_sample_user
    activity_heading=page.locator("//h2[text()='Alle Aktivitäten']")
    assert activity_heading.is_visible(), "Fehler bei Login - \"Alle Aktivitäten\" wird nicht angezeigt"

#login as normal user is working - no privilege on "Verwaltung"
@pytest.mark.login
def test_login_verwaltung(login_logout_sample_user) -> None:
    page=login_logout_sample_user
    page.get_by_role("link", name="Verwaltung").click()
    expect(page).to_have_url("https://web:8443/membership")
    error_kein_zugriff= page.locator("//h2[text()='Unzureichende Zugriffsberechtigung.']")
    assert error_kein_zugriff.is_visible(), "Fehler - \"Kein Zugriff\"-Meldung wird nicht angezeigt"
    page.screenshot(path="./screenshots/screen_verwaltung.png")

###
###dummy tests
###

#dummy to skip
@pytest.mark.skip(reason="Skippady-skabbady")
def test_login_skip(login_logout_sample_user) -> None:
    page=login_logout_sample_user
    expect(page).to_have_url("https://web:8443/gibtesNICHTERRORSKIP")

#dummy to fail
@pytest.mark.xfail(reason="Das ist ein gewollter fail")
def test_login_fail(login_logout_sample_user) -> None:
    page=login_logout_sample_user
    expect(page).to_have_url("https://web:8443/gibtesNICHTERRORSKIP")