from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config.config import settings


def create_driver(browser_name=None):
    if browser_name is None:
        browser_name = settings["browser"]["name"]

    browser_config = settings["browsers"].get(browser_name.lower(), {})
    headless = browser_config.get("headless", False)
    window_size = browser_config.get("window_size")

    if browser_name.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        if window_size:
            options.add_argument(f"--window-size={window_size}")
        return webdriver.Chrome(options=options)

    elif browser_name.lower() == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        return webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
