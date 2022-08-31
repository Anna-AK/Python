import pickle

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
        return self._web_driver.current_url

    def refresh(self, locator = "By.CSS_SELECTOR, 'div.b-rfooter-wrapper div.b-rfooter-e-column.b-rfooter-e-row-m-copy'"):
        self._web_driver.refresh()
        self.wait_page_loaded()

    def go_back(self):
        self._web_driver.back()

    def switch_to_last_window(self):
        self._web_driver.switch_to.window(self._web_driver.window_handles[-1])

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

    def fild_send_word(self, locator: tuple, word: str):
        find_fild = self.is_visible(locator)
        find_fild.clear()
        find_fild.send_keys(word)
        return find_fild

    def send_enter(self, web_elem):
        find_fild = web_elem
        find_fild.send_keys(Keys.ENTER)

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
            elem_pop = self.is_presence(locator_pop)
            action.move_to_element(elem).pause(0.5).perform()
            action.move_to_element(elem_pop).click(elem_pop).perform()
        elif locator_pop == None:
            action.move_to_element(elem).pause(0.5).click(elem).perform()
        else:
            action.move_to_element(elem).pause(0.5).move_to_element(locator_pop).pause(0.5).click(locator_pop).perform()
        return elem

    def copy_smb(self, locator):
        elem = self.is_visible(locator)
        action = ActionChains(self._web_driver)
        action.move_to_element(elem).perform()
        return elem.send_keys(Keys.CONTROL, 'c')

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
            time.sleep(0.3)
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

        # self._web_driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
