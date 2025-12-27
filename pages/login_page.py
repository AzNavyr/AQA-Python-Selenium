import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import settings
from utils.logger import logger


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.main_header = (By.CSS_SELECTOR, ".login_logo")
        self.header = (By.CSS_SELECTOR, ".app_logo")
        self.error_text = (By.CSS_SELECTOR, "h3[data-test='error']")
        self.fields = {
            "login": (By.ID, "user-name"),
            "password": (By.ID, "password")
        }
        self.login_button = (By.ID, "login-button")

    @allure.step("Open the URL")
    def open(self):
        url = settings["base_url"]
        logger.info(f"Open HomePage: '{url}'")
        self.driver.get(url)

    @allure.step("Verify that the login page is loaded correctly")
    def is_page_opened(self):
        return (
                settings["base_url"] in self.driver.current_url and
                all(self.wait.until(EC.visibility_of_element_located(locator))
                    for locator in [self.main_header, *self.fields.values(), self.login_button])
        )

    @allure.step("Title text search")
    def get_header_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.header)).text

    @allure.step("Filling in the '{field_name}' field with the value: '{value}'")
    def fill_the_form(self, field_name, value):
        logger.info(f"Filling {field_name} with {value}")
        locator = self.fields[field_name]
        el = self.driver.find_element(*locator)
        el.clear()
        el.send_keys(value)

    @allure.step("Click login buttom")
    def login_form(self):
        logger.info("Clicking login button")
        self.driver.find_element(*self.login_button).click()

    @allure.step("Find error text")
    def get_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_text)).text