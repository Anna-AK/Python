import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import valid_email, valid_password


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

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
    # if request.node.rep_call.failed:
    #     # Make the screen-shot if test failed:
    #     try:
    #         browser.execute_script("document.body.bgColor = 'white';")
    #
    #         # Make screen-shot for local debug:
    #         browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
    #
    #         # For happy debugging:
    #         print('URL: ', browser.current_url)
    #         print('Browser logs:')
    #         for log in browser.get_log('browser'):
    #             print(log)
    #
    #     except:
    #         pass # just ignore any errors here
    browser.quit()