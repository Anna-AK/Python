import pytest
import pickle

# from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import PageBase
from pages.locators import *
from pages.config import *


class TestingPage(PageBase):
    def __init__(self, driver, url = main_page_link):
        super().__init__(driver)
        self.get(url)
        self.wait_page_loaded()

    def verification_cookie(self):
        self.moving_to_elem_click(COOKI_YES)

    def autent_with_cookie(self):
        super().autent_with_cookie()
        if self.is_visible(AUTH_IND).text == valid_name:
            return True
        else:
            return False

    def add_prod_to_basket(self, num_prod = 2):
        # self.are_visible(BOOKS_BLOCKS)[0]
        prod = {}
        names = self.are_presence(PROD_BOOKS_BLOCKS)
        prices = self.are_presence(PRICE_BOOKS_BLOCKS)
        links = self.are_presence(BAY_PROD_BOOKS_BLOCKS)

        for i in range(num_prod):
            assert names[i].get_attribute("title") != ' ', print(f'Названия товара не загружено')
            prod[i] = [names[i].get_attribute("title"), int(''.join(str(prices[i].text).split()))]
            self.moving_to_elem_click(links[i])
        return prod

    def click_bay_button(self):
        self.moving_to_elem_click(BAY_ORD)

    def click_plus_prod(self, num = 1):
        prod_plus = self.are_presence(CART_PROD_PLUS)
        prod_price = self.are_visible(CART_PROD_PRICE)
        prod_plus[0].location_once_scrolled_into_view
        element = self.moving_to_elem_click(prod_plus[0])
        while num > 1:
            element.click()
            time.sleep(0.3)
        return int(''.join(str(prod_price[0].text).split())) * (num + 1)

    def click_minus_prod(self, num = 1):
        prod_minus = self.are_presence(CART_PROD_MN)
        prod_minus[0].location_once_scrolled_into_view
        element = self.moving_to_elem_click(prod_minus[0])
        while num > 1:
            element.click()
            time.sleep(0.3)
        return int(''.join(str(self.are_visible(CART_PROD_PRICE)[0].text).split()))         #int(''.join(str(prod_price[0].text).split())) * (num + 1)

    def enter_num_prod(self, num = 1):
        element = self.is_visible(CART_PROD_NUM)
        element.location_once_scrolled_into_view
        self.fild_enter_word(CART_PROD_NUM, num)

    def look_to_basket(self):
        self.scroll_down(200)
        prod = self.are_visible(CART_PROD)
        prod.reverse()
        return prod

    def compare_lists(self, prod, cart_prods):
        for i in range(len(cart_prods)):
            if prod[i][0].find(cart_prods[i].text) != -1:
                return True
            else: return False

    def compare_total(self, prod):
        return sum([prod[i][1] for i in range(len(prod))]) == int(''.join(str(self.is_visible(CART_TOTAL).text).split()))

    def alert_click(self):
        self.wait_until(EC.alert_is_present())
        self._web_driver.switch_to.alert.accept()





