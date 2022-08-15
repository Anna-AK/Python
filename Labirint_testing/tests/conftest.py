import pytest, pickle
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as chrome_options
# from selenium.webdriver.firefox.options import Options as firefox_options
# from pages.config import main_page_link

# def get_chrome_options():
#     options = chrome_options()
#     options.add_argument("chrome")
#     options.add_argument("--start-optimized")
#     return options
#
# def get_firefox_options():
#     options = firefox_options
#     options.add_argument("--start-optimized")
#     return options

def get_webdriver(param: str):
    # param = param
    if param == 'Chrome':
        # print(f"this is {param}")
        # options = get_chrome_options
        driver = webdriver.Chrome()         #(options=options)
    else:
        # print(f"this is {param}")
        # options = get_firefox_options()
        driver = webdriver.Firefox()        #(options=options)
    driver.set_window_size(1300, 900)
    return driver

# @pytest.fixture(scope='function', params = ['Chrome', 'Firefox'])
# def setup_browser(request):
#     param = str(request.param)
#     # print(param)
#     driver = get_webdriver(param)
#     # url = main_page_link
#     if request.cls is not None:
#         request.cls.driver = driver
#     # driver.get(url)
#     yield driver
#     driver.quit()
#
@pytest.fixture(scope='function')
def setup_browser(request):
    driver = get_webdriver('Chrome')
    # driver = get_webdriver('Firefox')
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()