# import time
#
import pytest
# from selenium.webdriver.common.by import By
# from selenium import webdriver
from pages.Labirint_page import TestingPage
from pages.config import *
from pages.locators import *

""" Проверка третьей панели верхнего главного меню"""

@pytest.mark.parametrize("num", range(0,5), ids = range(0,5))
def test_third_panel_point_dost(setup_browser, num):
    """Проверка наличия и кликабильности 5 пунктов (*Доставка и оплата*, *Сертификаты*, *Рейтинги*, *Новинки*, *Скидки*"""
    page = TestingPage(setup_browser)
    point_menu = page.are_presence(THIRD_PANEL)[num]
    page.moving_to_elem_click(point_menu)
    assert page.assert_pause(page.get_relative_link(), labirint_third_panel_links[num]), f"Ссылка {labirint_third_panel_links[num]} не открылась"

@pytest.mark.parametrize("num", range(8,10), ids = range(8,10))
def test_third_panel_point_sert(setup_browser, num):
    """Проверка наличия и кликабильности остальных пунктов (*Контакты*, *Поддержка*, *Пункты самовывоза*)"""
    page = TestingPage(setup_browser)
    point_menu = page.are_presence(THIRD_PANEL)[num]
    page.moving_to_elem_click(point_menu)
    assert page.assert_pause(page.get_relative_link(), labirint_third_panel_links[num]), f"Ссылка {labirint_third_panel_links[num]} не открылась"

def test_third_panel_point_reit(setup_browser):
    """Проверка наличия и кликабильности пункта *8 800 600-95-25*"""
    page = TestingPage(setup_browser)
    point_menu = page.are_presence(THIRD_PANEL)[5]
    page.moving_to_elem_click(point_menu)
    assert page.is_visible(WIND_CALL), "Окно CALL не всплавает"

def test_third_panel_points(setup_browser):
    """Проверка наличия и кликабильности всех 9 пунктов третьей панели верхнего меню - альтернативный предыдущим"""
    page = TestingPage(setup_browser)
    elem_menu = page.are_presence(THIRD_PANEL)
    for i in range(len(elem_menu)):
        point_menu = elem_menu[i]
        page.moving_to_elem_click(point_menu)
        elem_link = labirint_third_panel_links[i]
        if elem_link == 'WIND_CALL':
            if i == 5:
                assert page.is_visible(WIND_CALL), "Окно CALL не всплавает"
        else:
            assert page.assert_pause(page.get_relative_link(), elem_link), f"Ссылка {elem_link} не открылась"
        elem_menu = page.are_presence(THIRD_PANEL)

@pytest.mark.parametrize("num", range(0,6), ids = ['VK', 'YouTube', 'OK', 'YandexZen', 'Telegram', 'VK-child'])
def test_third_panel_soc_net_param(setup_browser, num):
    """Проверка наличия и кликабильности пунктов всплывающего подменю *Лабиринт в соцсетях*"""
    page = TestingPage(setup_browser)
    page.moving_to_elem(THIRD_SOC_NET)
    elem_menu = page.are_visible(SOC_NET_WIND)

    page.moving_to_elem_click(THIRD_SOC_NET, elem_menu[num])
    page.switch_to_last_window()
    page.wait_page_loaded()
    assert page.assert_pause(page.get_relative_link(), labirint_third_panel_soc_net[num]), f"Ссылка {labirint_third_panel_soc_net[num]} не открылась"

def test_third_panel_soc_net(setup_browser):
    """Проверка наличия и кликабильности пунктов всплывающего подменю *Лабиринт в соцсетях* - альтернативный предыдущему"""
    page = TestingPage(setup_browser)
    page.moving_to_elem(THIRD_SOC_NET)
    elem_menu = page.are_visible(SOC_NET_WIND)
    current_window = page._web_driver.current_window_handle
    for i in range(len(elem_menu)):
        point_menu = elem_menu[i]
        elem_link = labirint_third_panel_soc_net[i]
        print(f'i = {i}, point = {point_menu}, link = {elem_link}')
        page.moving_to_elem_click(THIRD_SOC_NET, point_menu)
        page.switch_to_last_window()
        page.wait_page_loaded()
        assert page.assert_pause(page.get_relative_link(), elem_link), f"Ссылка {elem_link} не открылась"
        page._web_driver.close()
        page._web_driver.switch_to.window(current_window)
