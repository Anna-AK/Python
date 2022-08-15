import pytest
import time

from pages.Labirint_page import TestingPage
from pages.config import *
from pages.locators import *

"""     Проверки первой панели верхнего главного меню"""
def test_first_panel_logo(setup_browser):
        """ Проверка наличия и кликабильности логотипа"""
        page = TestingPage(setup_browser)
        page.verification_cookie()
        element = page.moving_to_elem_click(LOGO)
        assert element, 'Логотип не отображается'
        assert page.assert_pause(page.get_relative_link(), main_page_link)

def test_first_panel_mess(setup_browser):
        """ Проверка наличия и кликабильности пункта *Сообщения*"""
        page = TestingPage(setup_browser)
        element = page.moving_to_elem_click(MESSAGE)
        assert element, 'Элемент "Сообщения" не отображается!'

def test_first_panel_mylab(setup_browser):
        """ Проверка наличия и кликабильности пункта *Мой Лаб*"""
        page = TestingPage(setup_browser)
        element = page.moving_to_elem_click(MY_LAB)
        assert element, 'Элемент "Мой Лабиринт" не найден!'

def test_first_panel_mylab_popup_panel_close(setup_browser):
        """ Проверка наличия всплывающего окна из *Мой Лаб* и его закрытия"""
        page = TestingPage(setup_browser)
        element = page.moving_to_elem_click(MY_LAB)
        assert element, 'Элемент "Мой Лабиринт" не найден!'

        page.moving_to_elem_click(CLOSE_FORM)
        assert page.assert_pause(page.get_relative_link(), main_page_link), "Окно регистрации не закрылось!"

def test_first_panel_mylab_popup_panel_1(setup_browser):
        """ Проверка 1 пункта всплывающего подменю пункта *МойЛабиринт* """
        page = TestingPage(setup_browser)
        elem_menu = page.are_presence(LAB_PANEL)
        page.moving_to_elem_click(MY_LAB, elem_menu[1])
        assert page.is_visible(LOG_WIND), "Окно регистрации не открылось!"

@pytest.mark.parametrize("num", [2,3], ids = ['2 point MyLab', '3 point MyLab'])
def test_first_panel_mylab_popup_panel_2(setup_browser, num):
        """ Проверка 2 и 3 пунктов всплывающего подменю пункта *МойЛабиринт* """
        page = TestingPage(setup_browser)
        elem_menu = page.are_presence(LAB_PANEL)
        page.moving_to_elem_click(MY_LAB, elem_menu[num])
        assert page.assert_pause(page.get_relative_link(), labirint_my_labs_links[num]), f'Ссылка {labirint_my_labs_links[num]} не работает!'

def test_first_panel_order(setup_browser):
        """ Проверка наличия и кликабильности пункта *Отложено*"""
        page = TestingPage(setup_browser)
        element = page.moving_to_elem_click(PUT_ORDER)
        assert element, 'Элемент "Отложено" не отображается!'
        assert page.assert_pause(page.get_relative_link(), put_order), "Переход в отложенные не пошел!"

        page.moving_to_elem_click(PUT_ORDER, ORD_REG_FILD)
        assert page.is_visible(LOG_WIND), "Окно регистрации не открылось!"

def test_first_panel_card(setup_browser):
        """ Проверка наличия и кликабильности пункта *Корзина* и его всплывающего подменю"""
        page = TestingPage(setup_browser)
        element = page.moving_to_elem_click(CART)
        assert element, 'Элемент "Корзина" не отображается!'
        assert page.assert_pause(page.get_relative_link(), labirint_cart), "Переход в корзину не пошел!"

def test_first_panel_card_popup_1(setup_browser):
        """ Проверка кликабильности 1 пункта подменю элемента *Корзина*"""
        page = TestingPage(setup_browser)
        page.moving_to_elem_click(CART, CART_NOW)
        assert page.assert_pause(page.get_relative_link(), labirint_now), "Переход на \"Лабиринт.сейчас\" не пошел!"

def test_first_panel_card_popup_2(setup_browser):
        """ Проверка кликабильности 2 пункта подменю элемента *Корзина*"""
        page = TestingPage(setup_browser)
        page.moving_to_elem_click(CART, CART_BEST)
        assert page.assert_pause(page.get_relative_link(), labirint_books_best), "Переход на \"Лабиринт.лучшее\" не пошел!"

def test_first_panel_find_prod(setup_browser):
        """ Проверка наличия поля поиска"""
        page = TestingPage(setup_browser)
        element = page.is_visible(FIND_FILD)
        assert element, 'Поле поиска не отображается!'

def test_first_panel_find_prod_works(setup_browser):
        """ Проверка срабатывания поля поиска"""
        page = TestingPage(setup_browser)
        element = page.fild_enter_word(FIND_FILD, word_to_find)
        assert element, 'Поле поиска не работает'
        assert page.assert_pause(page.get_relative_link(), link_find_rezalt), 'Переход при поиске не срабатывает'

def test_first_panel_find_empty(setup_browser):
        """ Проверка корректности поиска пустой строки"""
        page = TestingPage(setup_browser)
        element = page.fild_enter_word(FIND_FILD, ' ')
        assert element, 'Поле поиска не работает'
        page.wait_page_loaded()
        assert page.is_visible(FIND_FILD_EMPTY).text.find('ничего не нашли') > 0, "Поиск по пустой строке не сработал!"

def test_first_panel_find_and_look_prod(setup_browser):
        """ Проверка корректности поиска и перехода на страницу результатов"""
        page = TestingPage(setup_browser)
        page.fild_enter_word(FIND_FILD, word_to_find)
        page.wait_page_loaded()

        images = page.are_visible(PRODUCT_IMG)
        names = page.are_visible(PRODUCT_TITLE)
        assert len(images) == 60, "Товары не подгрузились!"
        for i in range(len(names)):
                assert images[i].get_attribute('src') != ''
                assert names[i].text != '' and names[i].text.find(word_to_find), print(f'Название товара = {names[i].text}')

@pytest.mark.parametrize("lang", ['r', 's', 'c', 'x'], ids=['russian', 'special', 'chine', 'x'])
@pytest.mark.parametrize("num", [1, 8, 255], ids=['min', '8', 'max'])
def test_first_panel_find_prods_negative(setup_browser, lang, num):
        """ Проверка негативных сценариев поиска"""
        page = TestingPage(setup_browser)
        str_find = page.generate_string(lang, num)
        element = page.fild_enter_word(FIND_FILD, str_find)
        page.wait_page_loaded()
        assert element, 'Поле поиска не работает'
        str_link = str('https://www.labirint.ru/search/' + str_find + '/?stype=0')
        assert page.assert_pause(page.get_relative_link(), str_link), 'Поиск не прошел!'

        str_find = str_find.upper()
        element = page.fild_enter_word(FIND_FILD, str_find)
        page.wait_page_loaded()
        assert element, 'Поле поиска не работает'
        str_link = str('https://www.labirint.ru/search/' + str_find + '/?stype=0')
        assert page.assert_pause(page.get_relative_link(), str_link), 'Поиск не прошел!'

@pytest.mark.parametrize("param", ['select *', 12345678], ids = ['SQL', 'nums'])
@pytest.mark.parametrize("num", [8, 255, 1], ids=['8', 'max', 'min'])
def test_first_panel_find_prods_negative_nums_sql(setup_browser, param, num):
        """ Вторая проверка негативных сценариев поиска (цифры, команда SQL)"""
        page = TestingPage(setup_browser)
        str_find = str(param)
        if num != 8:
                if num == 1:
                        str_find = str_find[0:1]
                else: str_find = str_find * (255//len(str_find))
        element = page.fild_enter_word(FIND_FILD, str_find)
        page.wait_page_loaded()
        str_link = str('https://www.labirint.ru/search/' + str_find + '/?stype=0')
        assert element, 'Поле поиска не работает'
        assert page.assert_pause(page.get_relative_link(), str_link), 'Поиск не прошел!'

def test_logo_discount(setup_browser):
        """ Проверка наличия и кликабильности пункта *Скидки*"""
        page = TestingPage(setup_browser)
        page.verification_cookie()

        element = page.moving_to_elem_click(LOGO_DISCOUNT)
        assert element, 'Элемент "Скидка" не отображается!'
        assert page.get_relative_link(), 'Ссылка "Скидка" не работает'

def test_labirint_auten(setup_browser):
        """ Проверка авторизации зарегистрированного пользователя (позитивный сценарий). Запись cookies в файл"""
        page = TestingPage(setup_browser)
        page.verification_cookie()
        page.moving_to_elem_click(MY_LAB)
        element = page.is_visible(COMMON_COD)
        assert element, 'Поле ввода кода не найдено!'
        page.fild_enter_word(COMMON_COD, valid_cod)
        page.wait_page_loaded()
        assert page.get_relative_link() == main_page_link, "Авторизация не прошла!"
        page.saving_cookies()

def test_first_panel_find_prod_with_cookie(setup_browser):
        """ Проверка работы поля поиска для авторизованного пользователя (cookie подгружаются)"""
        page = TestingPage(setup_browser)
        if page.autent_with_cookie():
                element = page.fild_enter_word(FIND_FILD, word_to_find)  # поле поиска работает
                assert element, 'Поле поиска не работает'
                assert page.get_relative_link() == link_find_rezalt or cabinet_link, 'Переход при поиске не срабатывает'
        else:
                raise 'Cookies не загрузились!'
        time.sleep(3)

def test_first_panel_mess_with_cookie(setup_browser):
        """ Проверка наличия и кликабильности пункта *Сообщения* для авторизированного пользователя (cookie подгружаются)"""
        page = TestingPage(setup_browser)
        if page.autent_with_cookie():
                element = page.moving_to_elem_click(MESSAGE)
                assert element, 'Элемент "Сообщения" не отображается!'
                assert page.get_relative_link() == cabinet_link, 'Переход на страницу заказов не срабатывает'
        else: raise 'Cookies не загрузились!'

def test_first_panel_mess_pop_with_cookie(setup_browser):
        """ Проверка наличия и кликабильности пункта *Сообщения* для авторизированного пользователя (cookie подгружаются)"""
        page = TestingPage(setup_browser)
        if page.autent_with_cookie():
                element = page.moving_to_elem_click(MESSAGE, MES_POP)
                assert element, 'Элемент "Сообщения" не отображается!'
                assert page.get_relative_link() == cabinet_personal, 'Переход на страницу персональных скидок не срабатывает'
        else: raise 'Cookies не загрузились!'

def test_first_panel_mylab_with_cookie(setup_browser):
        """ Проверка работы подменю *МойЛаб* для авторизированного пользователя (cookie подгружаются)"""
        page = TestingPage(setup_browser)
        if page.autent_with_cookie():
                page.moving_to_elem_click(MY_LAB)
                page.moving_to_elem(MY_LAB)
                elem_menu = page.are_presence(LAB_PANEL_AUTH)
                for i in range(len(elem_menu)):
                        point_menu = elem_menu[i]
                        elem_link = labirint_my_labs_links_auth[i]
                        page.moving_to_elem_click(MY_LAB, point_menu)
                        # time.sleep(2)
                        if labirint_my_labs_links_auth[i] == 'LOG_WIND':
                                pass
                        else:
                                assert page.assert_pause(page.get_relative_link(), elem_link), "Ссылка не работает!"
                                elem_menu = page.are_presence(LAB_PANEL_AUTH)
        else:
                raise 'Cookies не загрузились!'
                # time.sleep(2)
