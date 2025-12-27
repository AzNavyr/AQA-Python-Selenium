import pytest
from utils.driver_factory import create_driver
from config.config import settings

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    driver = create_driver(browser_name)
    yield driver
    driver.quit()
