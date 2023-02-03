from playwright.sync_api import Playwright, expect
import pytest
import os


#Fixture for login and logout a given user defined in the function
@pytest.fixture(scope="function")
def login_logout_sample_user(playwright: Playwright) -> None:
    #open browser, context for https ignore in docker and page
    # slow_mo=500 --> usefull for tests over unstable wifi but slows down tests
    browser=playwright.chromium.launch(slow_mo=500)
    context=browser.new_context(ignore_https_errors=True)
    page=context.new_page()
    
    #navigate to login-page
    page.goto("https://web:8443/")
    

    #login with my private credentials
    user=os.environ.get('PYTEST_USER')
    secret=os.environ.get('PYTEST_PASSWORD')
    
    page.get_by_label("Benutzername oder Email*").fill(user)
    page.get_by_label("Passwort*").fill(secret)
    #screenshot before login
    #page.screenshot(path="./screenshots/screen_login_filled.png")
    page.get_by_role("button", name="Anmelden").click()
    expect(page).to_have_url("https://web:8443/activity")
    #screenshot after login
    #page.screenshot(path="./screenshots/screen_activity.png")

    #give page back to test-function
    yield page
    
    #logout after tests
    page.get_by_role("link", name="Account").hover()
    page.screenshot(path="./screenshots/screen_account-hover.png")
    page.get_by_role("link", name="Abmelden").click()
    expect(page).to_have_url("https://web:8443/")
    #screenshot after logout
    #page.screenshot(path="./screenshots/screen_logout.png")
    
    #close context and browser
    context.close()
    browser.close()
