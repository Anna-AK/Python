# import pytest
import pickle
# import requests

# from selenium.webdriver.common.by import By
# from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# class SeleniumBase:
class PageBase(object):
    _web_driver = None

    def __init__(self, driver):
        self._web_driver = driver
        self.__wait = WebDriverWait(driver, 10, 1)

    def is_visible(self, locator: tuple):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def are_visible(self, locator: tuple):
        return self.__wait.until(EC.visibility_of_all_elements_located(locator))

    def is_presence(self, locator: tuple):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def are_presence(self, locator: tuple):
        return self.__wait.until(EC.presence_of_all_elements_located(locator))

    def wait_until(self, anything):
        return self.__wait.until(anything)

    def get(self, url):
        self._web_driver.get(url)
        self.wait_page_loaded()

    def get_relative_link(self):
        # url = urlparse(self._web_driver.current_url)
        return self._web_driver.current_url

    def refresh(self, locator = "By.CSS_SELECTOR, 'div.b-rfooter-wrapper div.b-rfooter-e-column.b-rfooter-e-row-m-copy'"):
        self._web_driver.refresh()
        self.wait_page_loaded()

    def go_back(self):
        self._web_driver.back()
        # self.refresh()

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
        find_fild.clear()
        find_fild.send_keys(word)
        # self._web_driver.save_screenshot('../screen.png')
        find_fild.send_keys(Keys.ENTER)
        return find_fild

    def moving_to_elem(self, locator, x_offset = 0, y_offset = 0):
        if type(locator) == tuple:
            elem = self.is_visible(locator)
        else: elem = locator
        if x_offset == 0 and y_offset == 0:
            ActionChains(self._web_driver).move_to_element(elem).pause(0.5).perform()
        else:
            ActionChains(self._web_driver).move_to_element_with_offset(elem, x_offset, y_offset).pause(1).perform()
        return elem

    def moving_to_elem_click(self, locator, locator_pop = None):
        if type(locator) == tuple:
            elem = self.is_visible(locator)
        else: elem = locator
        action = ActionChains(self._web_driver)
        if locator_pop != None and type(locator_pop) == tuple:
            # elem_pop = EC.element_to_be_clickable(locator_pop)
            elem_pop = self.is_presence(locator_pop)
            action.move_to_element(elem).pause(0.5).perform()
            # elem_pop.location_once_scrolled_into_view
            action.move_to_element(elem_pop).click(elem_pop).perform()
        elif locator_pop == None:
            action.move_to_element(elem).pause(0.5).click(elem).perform()
        else:
            action.move_to_element(elem).pause(0.5).move_to_element(locator_pop).pause(0.5).click(locator_pop).perform()
        # self.refresh()
        return elem

    def wait_page_loaded(self, timeout = 60, check_js_complete = True,
                         check_page_changes = False,
                         sleep_time = 2):

        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)
        source = ''
        try:
            source = self._web_driver.page_source
        except:
            pass

        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                try:
                    self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self._web_driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass

            if page_loaded and check_page_changes:
                new_source = ''
                try:
                    new_source = self._web_driver.page_source
                except:
                    pass

                page_loaded = new_source == source
                source = new_source
            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        self._web_driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

    def switch_to_last_window(self):
        self._web_driver.switch_to.window(self._web_driver.window_handles[-1])

    def set_window_size(self, wigth = 1300, hight = 900):
        self._web_driver.set_window_size(wigth, hight)

    def saving_cookies(self, file_name = '../my_cookies'):
        with open(file_name, 'wb') as cookies:
            pickle.dump(self._web_driver.get_cookies(), cookies)
            # pickle.dump(session.cookies, cookies)

    def autent_with_cookie(self):
        try:
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
            self.refresh()

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

