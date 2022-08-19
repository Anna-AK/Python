import time

import pytest
from pages.Labirint_page import TestingPage
from pages.config import *
from pages.locators import *

""" Пользовательские сценарии"""
def test_add_prod(setup_browser):
    """Добавление товаров в корзину, сверка позиций и итоговой суммы"""
    page = TestingPage(setup_browser)
    page.verification_cookie()
    prod = page.add_prod_to_basket(2)
    page.click_bay_button()
    page.wait_page_loaded()
    cart_prods = page.look_to_basket()
    assert page.compare_lists(prod, cart_prods), print('Содержимое корзины не соответствует выбору!')
    assert page.compare_total(prod), print('Реальный итог не равен выведенному на экран!')

def test_add_prod_change(setup_browser):
    """Добавление товаров в корзину, изменение количества кнопками +-, сверка позиций и итоговой суммы"""
    page = TestingPage(setup_browser)
    page.verification_cookie()
    prod = page.add_prod_to_basket(2)
    page.click_bay_button()
    page.wait_page_loaded()
    assert page.compare_total(prod), print('Реальный итог не равен выведенному на экран!')

    num_click = 2
    prod_price = page.click_plus_prod(num_click)
    assert prod_price == int(prod[len(prod) - 1][1] * (num_click + 1)), print ('Добавление по "+" не прошло')

    prod_price = page.click_minus_prod()
    assert page.assert_pause(prod_price, prod[len(prod) - 1][1] * 2), print('Удаление по "-" не прошло')
    assert sum([prod[i][1] for i in range(len(prod))]) + prod[len(prod) - 1][1] == int(''.join(str(page.is_visible(CART_TOTAL).text).split())), print('Реальный итог не равен выведенному на экран!')

def test_add_prod_change_num(setup_browser):
    """Добавление товаров в корзину, изменение количества вводом в поле, сверка позиций и итоговой суммы"""
    page = TestingPage(setup_browser)
    prod = page.add_prod_to_basket(1)
    page.click_bay_button()
    page.wait_page_loaded()
    page.enter_num_prod(3)

    prod_price = page.are_visible(CART_PROD_PRICE)
    assert page.assert_pause(int(''.join(str(prod_price[0].text).split())), prod[len(prod) - 1][1] * 3), print('Ввод количества не прошел')

def test_add_prod_change_num_max(setup_browser):
    """Добавление товара в корзину, изменение его количества вводом в поле числа больше допустимого,
    проверка коррекции кол-ва до максимольно допустимого (9999)"""
    page = TestingPage(setup_browser)
    page.verification_cookie()
    page.add_prod_to_basket(1)
    page.click_bay_button()
    page.wait_page_loaded()
    element = page.enter_num_prod(999999999)
    assert element.get_attribute('value') == '9999', print('Корректировка большого числа не прошла!')

def test_del_prod(setup_browser):
    """Добавление товаров в корзину, удаление первой позиции"""
    page = TestingPage(setup_browser)
    page.verification_cookie()
    prod = page.add_prod_to_basket(2)
    page.click_bay_button()
    page.wait_page_loaded()
    # page.click_minus_prod()
    # prod_minus = page.are_presence(CART_PROD_MN)
    # prod_minus[0].location_once_scrolled_into_view
    # page.moving_to_elem_click(prod_minus[0])
    page.enter_num_prod(0)
    page.alert_click()
    assert page.assert_pause(sum([prod[i][1] for i in range(len(prod) - 1)]), int(''.join(str(page.is_visible(CART_TOTAL).text).split()))), print(
            'Реальный итог не равен выведенному на экран!')

def test_clear_card(setup_browser):
    """Добавление товаров в корзину, очистка корзины"""
    page = TestingPage(setup_browser)
    page.verification_cookie()
    page.add_prod_to_basket(2)
    page.click_bay_button()
    page.wait_page_loaded()

    element = page.moving_to_elem(CART_CLEAR)
    try:
        element.click()
    except: pass
    assert page.assert_pause(page.is_visible(CART_CLEAR_TEXT).text.find('ВАША КОРЗИНА ПУСТА'), not 0)

def test_clear_recovery_cart(setup_browser):
    """Добавление товаров в корзину, ее очистка, восстановление удаленного"""
    page = TestingPage(setup_browser)
    page.verification_cookie()
    prod = page.add_prod_to_basket(2)
    page.click_bay_button()
    page.wait_page_loaded()

    # page.moving_to_elem_click(CART_CLEAR)
    element = page.moving_to_elem(CART_CLEAR)
    # time.sleep(2)
    try:
        element.click()
    except: pass

    page.moving_to_elem_click(CART_RECLEAR)
    time.sleep(3)
    cart_prods = page.look_to_basket()
    for i in range(len(cart_prods)):
        assert prod[i][0].find(cart_prods[i].text)  != -1 or prod[i][0].find(cart_prods[len(cart_prods) - i - 1].text) != -1, print('Содержимое корзины не соответствует выбору!')

def test_card_order(setup_browser):
    """Добавление товаров в корзину, перемещение последнего в отложенные"""
    page = TestingPage(setup_browser)
    page.verification_cookie()
    prod = page.add_prod_to_basket(2)
    page.click_bay_button()
    page.wait_page_loaded()

    elements = page.are_visible(CART_PROD_TO_ORD)
    elements[0].location_once_scrolled_into_view
    page.moving_to_elem_click(elements[0])
    time.sleep(2)

    assert sum([prod[i][1] for i in range(len(prod)-1)]) == int(''.join(str(page.is_visible(CART_CHECK_TOTAL).text).split()))
    page.moving_to_elem_click(CART_ORDER)

def test_card_check(setup_browser):
    """Добавление товаров в корзину, переход к оформлению"""
    page = TestingPage(setup_browser)
    page.verification_cookie()
    prod = page.add_prod_to_basket(2)
    page.click_bay_button()
    page.wait_page_loaded()

    page.moving_to_elem_click(CART_CHECK)
    time.sleep(2)
    assert page.get_relative_link() == labirint_checkout, print('Переход на оформление не прошел')
