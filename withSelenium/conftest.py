import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import valid_email, valid_password

@pytest.fixture(autouse=True, scope="session")
def web_browser(request):
    browser = webdriver.Firefox()
    browser.set_window_size(1400, 1000)
    browser.get('http://petfriends1.herokuapp.com/login')
    browser.find_element_by_id('email').send_keys(valid_email)
    browser.find_element_by_id('pass').send_keys(valid_password)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    # Return browser instance to test case:
    yield browser
    browser.quit()