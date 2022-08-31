import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def setup_browser(request):
    driver = webdriver.Chrome()
    driver.set_window_size(1300, 900)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
