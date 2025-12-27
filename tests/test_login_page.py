import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.logger import logger

from pages.login_page import LoginPage



@allure.epic("Login Page")
@allure.feature("Authentication")
@allure.story("Invalid credentials login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("ui", "negative", "auth")
@allure.title("Login attempt with invalid username or password")
@allure.description("""
Verifies that a user cannot log in with invalid credentials.

Steps:
1. Open the login page.
2. Enter an invalid username and/or password.
3. Submit the login form.
4. Verify that the correct error message is displayed.
""")
@pytest.mark.parametrize(
   "username, password, expected_result",[
        ("out_user",
         "sauce",
         "Epic sadface: Username and password do not match any user in this service"
         )
    ]
)
def test_login_invalid_credential(driver, username, password, expected_result):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.fill_the_form("login", username)
    login_page.fill_the_form("password", password)

    login_page.login_form()

    assert expected_result == login_page.get_error_text()


@allure.epic("Login Page")
@allure.feature("Authentication")
@allure.story("Locked user login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("ui", "negative", "security")
@allure.title("Login attempt with locked out user")
@allure.description("""
Verifies that a locked out user cannot log in to the system.

Steps:
1. Open the login page.
2. Enter credentials of a locked out user.
3. Submit the login form.
4. Verify that the appropriate error message is displayed.
""")
@pytest.mark.parametrize(
   "username, password, expected_result",[
        ("locked_out_user",
         "secret_sauce",
         "Epic sadface: Sorry, this user has been locked out."
         )
    ]
)
def test_login_banned_user(driver, username, password, expected_result):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.fill_the_form("login", username)
    login_page.fill_the_form("password", password)

    login_page.login_form()

    assert expected_result == login_page.get_error_text()

@allure.epic("Login Page")
@allure.feature("Authentication")
@allure.story("Empty credentials validation")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("ui", "negative", "validation")
@allure.title("Login attempt with empty username and password")
@allure.description("""
Verifies that the system prevents login when required fields are empty.

Steps:
1. Open the login page.
2. Leave the username and password fields empty.
3. Submit the login form.
4. Verify that the validation error message is displayed.
""")
def test_login_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login_form()

    expected_result = "Epic sadface: Username is required"

    assert expected_result == login_page.get_error_text()

@allure.epic("Login Page")
@allure.feature("Authentication")
@allure.story("Performance degradation handling")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "performance", "stability")
@allure.title("Login with performance glitch user")
@allure.description("""
Verifies that a user with valid credentials can successfully log in
even when the page loads with a noticeable delay.

Steps:
1. Open the login page.
2. Enter valid credentials for a performance glitch user.
3. Submit the login form.
4. Wait for the page to fully load.
5. Verify that the main header 'Swag Labs' is displayed.
""")
@pytest.mark.parametrize(
   "username, password, expected_result",[
        ("performance_glitch_user",
         "secret_sauce",
         "Swag Labs"
         )
    ]
)
def test_login_glitch_user(driver, username, password, expected_result):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.fill_the_form("login", username)
    login_page.fill_the_form("password", password)

    login_page.login_form()

    assert expected_result == login_page.get_header_text()