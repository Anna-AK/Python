import pytest
import pickle
import requests

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from urllib.parse import urlparse
# from locators import *
# from config import *


# class SeleniumBase:
class PageBase(object):
    _web_driver = None

    def __init__(self, driver):
        self._web_driver = driver
        self.__wait = WebDriverWait(driver, 10, 1)

    # def __get_selenium_loc(self, find_by: str) -> dict:
    #     find_by = find_by.lower()
    #     locating = {
    #         'css': By.CSS_SELECTOR,
    #         'xpath': By.XPATH,
    #         'name': By.NAME,
    #         'class': By.CLASS_NAME,
    #         'id': By.ID,
    #         'link_text': By.LINK_TEXT,
    #         'tag': By.TAG_NAME
    #     }
    #     return locating[find_by]

    def is_visible(self, locator: tuple):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def are_visible(self, locator: tuple):
        return self.__wait.until(EC.visibility_of_all_elements_located(locator))

    def is_presence(self, locator: tuple):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def are_presence(self, locator: tuple):
        return self.__wait.until(EC.presence_of_all_elements_located(locator))
    #
    # def is_clicable(self, locator):
    #     return self.__wait.until(EC.element_to_be_clickable(locator))
    def wait_until(self, anything):
        return self.__wait.until(anything)

    def get(self, url):
        self._web_driver.get(url)
        self.wait_page_loaded()

    def get_relative_link(self):
        # url = urlparse(self._web_driver.current_url)
        return self._web_driver.current_url
    # def get_current_url(self):
    #     """ Returns current browser URL. """
       # return self._web_driver.current_url

    def refresh(self, locator = "By.CSS_SELECTOR, 'div.b-rfooter-wrapper div.b-rfooter-e-column.b-rfooter-e-row-m-copy'"):
        self._web_driver.refresh()
        self.wait_page_loaded()

    def go_back(self):
        self._web_driver.back()
        self.refresh()

    def screenshot(self, file_name='screenshot.png'):
        self._web_driver.save_screenshot(file_name)

    def scroll_down(self, offset=0):
        """ Scroll the page down. """

        if offset:
            self._web_driver.execute_script('window.scrollBy(0, {0});'.format(offset))
        else:
            self._web_driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        """ Scroll the page up. """

        if offset:
            self._web_driver.execute_script('window.scrollBy(0, -{0});'.format(offset))
        else:
            self._web_driver.execute_script('window.scrollBy(0, -document.body.scrollHeight);')

    def fild_enter_word(self, locator: tuple, word: str):
        find_fild = self.is_visible(locator)
        # print(word)
        # find_fild.click()
        find_fild.clear()
        # time.sleep(1)
        find_fild.send_keys(word)
        # action = ActionChains(self._web_driver)
        # action.click(find_fild).send_keys(word).send_keys(Keys.ENTER).perform()
        # self._web_driver.save_screenshot('../screen.png')
        time.sleep(3)
        find_fild.send_keys(Keys.ENTER)
        # time.sleep(2)
        # self.refresh()
        # find_fild.click()
        return find_fild

    def moving_to_elem(self, locator, x_offset = 0, y_offset = 0):
        if type(locator) == tuple:
            elem = self.is_visible(locator)
        else: elem = locator
        if x_offset == 0 and y_offset == 0:
            ActionChains(self._web_driver).move_to_element(elem).pause(1).perform()
        else:
            ActionChains(self._web_driver).move_to_element_with_offset(elem, x_offset, y_offset).pause(1).perform()
        return elem

    def moving_to_elem_click(self, locator, locator_pop = None):
        if type(locator) == tuple:
            elem = self.is_visible(locator)
        else: elem = locator
        action = ActionChains(self._web_driver)
        if locator_pop != None and type(locator_pop) == tuple:
            elem_pop = EC.element_to_be_clickable(locator_pop)
            action.move_to_element(elem).pause(1).perform()
            # elem_pop.location_once_scrolled_into_view
            action.move_to_element(elem_pop).click(elem_pop).perform()
        elif locator_pop == None:
            action.move_to_element(elem).pause(1).click(elem).perform()
        else:
            action.move_to_element(elem).pause(1).move_to_element(locator_pop).pause(1).click(locator_pop).perform()
        # self.refresh()
        return elem

    def wait_page_loaded(self, timeout = 60, check_js_complete = True,
                         check_page_changes = False, check_images=False,
                         wait_for_element = None,
                         wait_for_xpath_to_disappear = '',
                         sleep_time = 2):
        """ This function waits until the page will be completely loaded.
            We use many different ways to detect is page loaded or not:

            1) Check JS status
            2) Check modification in source code of the page
            3) Check that all images uploaded completely
               (Note: this check is disabled by default)
            4) Check that expected elements presented on the page
        """

        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)

        # Get source code of the page to track changes in HTML:
        source = ''
        try:
            source = self._web_driver.page_source
        except:
            pass

        # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                # Scroll down and wait when page will be loaded:
                try:
                    self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self._web_driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass

            if page_loaded and check_page_changes:
                # Check if the page source was changed
                new_source = ''
                try:
                    new_source = self._web_driver.page_source
                except:
                    pass

                page_loaded = new_source == source
                source = new_source

            # Wait when some element will disappear:
            # if page_loaded and wait_for_xpath_to_disappear:
            #     bad_element = None
            #
            #     try:
            #         bad_element = WebDriverWait(self._web_driver, 0.1).until(
            #             EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
            #         )
            #     except:
            #         pass  # Ignore timeout errors
            #
            #     page_loaded = not bad_element
            #
            # if page_loaded and wait_for_element:
            #     try:
            #         page_loaded = WebDriverWait(self._web_driver, 0.1).until(
            #             EC.element_to_be_clickable(wait_for_element._locator)
            #         )
            #     except:
            #         pass  # Ignore timeout errors

            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            # Check two times that page completely loaded:
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        # Go up:
        self._web_driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

    def switch_to_last_window(self):
        self._web_driver.switch_to.window(self._web_driver.window_handles[-1])

    def set_window_size(self, wigth = 1300, hight = 900):
        self._web_driver.set_window_size(wigth, hight)

    def saving_cookies(self, file_name = '../my_cookies'):
        # session = requests.session()
        with open(file_name, 'wb') as cookies:
            pickle.dump(self._web_driver.get_cookies(), cookies)
            # pickle.dump(session.cookies, cookies)

    def autent_with_cookie(self):
        try:
            # session = requests.session()  # or an existing session
            #
            # with open('./my_cookies', 'rb') as coockie:
            #     session.cookies.update(pickle.load(coockie))
            with open('../my_cookies', 'rb') as cookiesfile:
                cookies = pickle.load(cookiesfile)
                for cookie in cookies:
                    self._web_driver.add_cookie(cookie)
                    # print(cookie)
            # self._web_driver.get_cookies()
            # time.sleep(2)
            # self.saving_cookies('../my_cookies_old')
            self.refresh()
        except:
            print('This is without new cookies((')
            with open('../my_cookies_old', 'rb') as cookiesfile:
                cookies = pickle.load(cookiesfile)
                for cookie in cookies:
                    self._web_driver.add_cookie(cookie)
                    # print(cookie)
            # self._web_driver.get_cookies()
            time.sleep(2)
            # self.refresh()

    def assert_pause(self, param_real, param_assert, time_max = 3):
        try:
            print('1: assert_pause')
            assert param_real == param_assert
        except:
            time.sleep(time_max)
            print('2: assert_pause')
            assert param_real == param_assert
        finally:
            return True

    def russian_chars(self):
        return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def chinese_chars(self):
        return '的一是不了人我在有他这为之大来以个中上们'

    def special_chars(self):
        return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

    def generate_string(self, lang = 'x', num = 1):
        if lang == 'r':
            str = self.russian_chars()
        elif lang == 'c':
            str = self.chinese_chars()
        elif lang == 's':
            str = self.special_chars()
        else: str = 'x' * num

        if len(str) > num:
            str = str[0:num]
        else:
            str = str * (num // len(str))
        # print(f'str = {str}')
        # if str == '': str = 'x' * num
        return str

