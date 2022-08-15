import time

import pytest
# import os, pickle
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
from pages.Labirint_page import TestingPage
from pages.config import *
from pages.locators import *

"""     Проверки второй панели верхнего главного меню"""
def test_second_panel_fst_point(setup_browser):
    """Проверка наличия и кликабильности пункта меню *Книги*"""
    page = TestingPage(setup_browser)
    element = page.moving_to_elem_click(POINT_BOOKS)
    page.wait_page_loaded()
    assert element, 'Пункт меню *Книги* не найден'
    assert page.assert_pause(page.get_relative_link(), labirint_books), "Переход на Книги не прошел"

def test_second_panel_scnd_point(setup_browser):
    """Проверка наличия и кликабильности пункта меню *Главное 2022*"""
    page = TestingPage(setup_browser)
    element = page.moving_to_elem_click(POINT_BEST)
    page.wait_page_loaded()
    assert element, 'Пункт меню ГЛАВНОЕ не отображается'
    assert page.assert_pause(page.get_relative_link(), labirint_books_best), "Переход на Главные книги не прошел"

def test_second_panel_third_point(setup_browser):
    """Проверка наличия и кликабильности пункта меню *Школа*"""
    page = TestingPage(setup_browser)
    element = page.moving_to_elem_click(POINT_SCHOOL)
    page.wait_page_loaded()
    assert element, 'Пункт меню *Школа* не отображается'
    assert page.assert_pause(page.get_relative_link(), labirint_school), "Переход на Товары для школы не прошел"

def test_second_panel_third_point_popup_predm(setup_browser):
    """Проверка наличия и кликабильности пунктов подменю *Школа / Основные предметы*"""
    page = TestingPage(setup_browser)
    points_elem = page.are_presence(SCHOOL_PREDM)
    for i in range(len(points_elem)):
        page.moving_to_elem_click(POINT_SCHOOL, points_elem[i])
        page.wait_page_loaded()
        assert page.assert_pause(page.get_relative_link(), labirint_school + labirint_scnd_panel_school_pr_links[i]), f"Ссылка {labirint_scnd_panel_school_pr_links[i]} не открылась"
        points_elem = page.are_presence(SCHOOL_PREDM)

def test_second_panel_third_point_popup_class(setup_browser):
    """Проверка наличия и кликабильности пунктов подменю *Школа / Классы*"""
    page = TestingPage(setup_browser)
    points_elem = page.are_presence(SCHOOL_KLASS)
    for i in range(len(points_elem)):
        page.moving_to_elem_click(POINT_SCHOOL, points_elem[i])
        page.wait_page_loaded()
        assert page.assert_pause(page.get_relative_link(), labirint_school + labirint_scnd_panel_school_kl_links[i]), f"Ссылка {labirint_scnd_panel_school_kl_links[i]} не открылась"
        points_elem = page.are_presence(SCHOOL_KLASS)

def test_second_panel_third_point_all(setup_browser):
    """Проверка наличия и кликабильности пунктов подменю *Школа / Все предметы*"""
    page = TestingPage(setup_browser)
    page.moving_to_elem_click(POINT_SCHOOL, page.is_presence(SCHOOL_PREDM_ALL))
    page.wait_page_loaded()
    assert page.get_relative_link() == labirint_school_all, "Переход Школьные предметы не прошел"

def test_second_panel_third_point_preschool(setup_browser):
    """Проверка наличия и кликабильности пунктов подменю *Школа / Дошкольникам*"""
    page = TestingPage(setup_browser)
    page.moving_to_elem_click(POINT_SCHOOL, page.is_presence(SCHOOL_PRESCHOOL))
    page.wait_page_loaded()
    assert page.get_relative_link() == labirint_preschool, "Переход на Товары для дошкольныиков не прошел"

def test_second_panel_fourth_point(setup_browser):
    """Проверка наличия и кликабильности пункта меню *Игрушки*"""
    page = TestingPage(setup_browser)
    element = page.moving_to_elem_click(POINT_TOYS)
    page.wait_page_loaded()
    assert element, 'Пункт меню *Игрушки* не отображается'
    assert page.assert_pause(page.get_relative_link(), labirint_toys), "Переход на Игрушки не прошел"

def test_second_panel_fourth_point_popup_1(setup_browser):
    """Проверка наличия и кликабильности 1 пункта подменю меню *Игрушки*"""
    page = TestingPage(setup_browser)
    first_points = page.are_presence(TOYS_POINTS)
    page.moving_to_elem_click(POINT_TOYS, first_points[0])
    page.wait_page_loaded()
    assert page.assert_pause(page.get_relative_link(), labirint_toys), "Переход на Игрушки не прошел"

def test_second_panel_fourth_point_popup_2(setup_browser):
    """Проверка наличия и кликабильности 2 пункта подменю *Игрушки*"""
    page = TestingPage(setup_browser)
    first_points = page.are_presence(TOYS_POINTS)
    points_elem = page.are_presence(TOYS_TOY)
    for i in range(len(points_elem)):
        i = 15
        page.moving_to_elem(POINT_TOYS)
        page.moving_to_elem(first_points[1])
        try:
            page.moving_to_elem_click(points_elem[i])
        except: #ElementNotInteractableException:
            print(f'1 except i = {i}')
            page.moving_to_elem(POINT_TOYS)
            page.moving_to_elem(first_points[1])
            first_points[1].location_once_scrolled_into_view
            page.moving_to_elem_click(points_elem[i])
            try:
                print(f'2 except i = {i}')
                page.moving_to_elem(first_points[1])
                page.moving_to_elem_click(points_elem[i])
            except:
                print(f'3 except i = {i}')
                page.moving_to_elem(POINT_TOYS)
                page.moving_to_elem(first_points[1])
                page.moving_to_elem(points_elem[i-3])
                points_elem[i].location_once_scrolled_into_view
                time.sleep(0.3)
                page.moving_to_elem_click(points_elem[i])

        print(f'i = {i}, real = {page.get_relative_link()}, link = {labirint_scnd_panel_toys_links[i]}')
        assert page.assert_pause(page.get_relative_link(), 'https://www.labirint.ru/genres/' + labirint_scnd_panel_toys_links[i]+'/')
        first_points = page.are_presence(TOYS_POINTS)
        points_elem = page.are_presence(TOYS_TOY)


def test_second_panel_fourth_point_popup_3(setup_browser):
    """Проверка наличия и кликабильности пункта меню *Игрушки*"""
    page = TestingPage(setup_browser)
    first_points = page.are_presence(TOYS_POINTS)
    points_elem = page.are_presence(TOYS_TOY)
    j = 1
    for i in range(len(points_elem)):
        if i == 17:
            j += 1
        page.moving_to_elem(POINT_TOYS)
        # first_points[j].location_once_scrolled_into_view
        elem = page.moving_to_elem(first_points[j])
        # elem.click()

        # if i  download
        # print(f"j = {j} drag first_points = {first_points[j].get_attribute('draggable')}")
        # print(f"{i} onload = {points_elem[i].get_attribute('onload')}, {i+15} onload = {points_elem[i+15].get_attribute('onload')}")
        # print(f"{i} hidden = {points_elem[i].get_attribute('hidden')}, {i + 15} hidden = {points_elem[i + 15].get_attribute('hidden')}")
        # try:
        # page.scroll_down(100)
        # if 17 > i > 6 or i > 25:
        #     points_elem[i].location_once_scrolled_into_view
        #     page.moving_to_elem(POINT_TOYS)
        #     page.moving_to_elem(first_points[j])

        # points_elem[i].location_once_scrolled_into_view
        # page.moving_to_elem(points_elem[i])
        # points_elem[i].click()
        # i = 14
        try:
            page.moving_to_elem_click(points_elem[i])
        except:  # ElementNotInteractableException:
            print(f'except i = {i}')
            page.moving_to_elem(POINT_TOYS)
            page.scroll_down(110)
            time.sleep(.3)
            try:
                page.moving_to_elem(first_points[j])
                page.moving_to_elem_click(points_elem[i])
            except:
                page.moving_to_elem(POINT_TOYS)
                page.scroll_down(150)
                time.sleep(.3)
                page.moving_to_elem(first_points[j])
                page.moving_to_elem_click(points_elem[i])

        print(f'i = {i}, real = {page.get_relative_link()}, link = {labirint_scnd_panel_toys_links[i]}')
        assert page.assert_pause(page.get_relative_link(),
                                 'https://www.labirint.ru/genres/' + labirint_scnd_panel_toys_links[i] + '/')
        first_points = page.are_presence(TOYS_POINTS)
        points_elem = page.are_presence(TOYS_TOY)

def test_second_panel_six_point(setup_browser):
    """Проверка наличия и кликабильности пункта меню *Еще...*"""
    page = TestingPage(setup_browser)
    element = page.moving_to_elem(POINT_MORE)
    assert element, 'Пункт меню *Еще...* не отображается'
    points_more = page.are_presence(MORE_POINTS)
    j = 0
    for i in range(len(points_more)):
        # print(f'i = {i}, attribute = {points_more[i].get_attribute("class")}')
        if points_more[i].get_attribute("class").find('second-item-hide') == -1:
            if i == 0:
                j = 3
            else:
                page.moving_to_elem_click(POINT_MORE, points_more[i])
                page.wait_page_loaded()
                assert page.assert_pause(page.get_relative_link(), labirint_scnd_panel_more_links[j]), f"Ссылка {labirint_scnd_panel_more_links[j]} не открылась"
                j += 1
                page.moving_to_elem(POINT_MORE)
                points_more = page.are_presence(MORE_POINTS)

def test_second_panel_fourth_point_1100(setup_browser):
    """Проверка наличия и кликабильности пункта меню *Еще...* при размере окна 1100"""
    page = TestingPage(setup_browser)
    page.set_window_size(1100, 900)
    element = page.moving_to_elem(POINT_MORE)
    assert element, 'Пункт меню *Еще...* не отображается'
    points_more = page.are_presence(MORE_POINTS)
    j = 0
    for i in range(len(points_more)):
        if i != 0:
            page.moving_to_elem_click(POINT_MORE, points_more[i])
            page.wait_page_loaded()
            assert page.assert_pause(page.get_relative_link(), labirint_scnd_panel_more_links[j]), f"Ссылка {labirint_scnd_panel_more_links[j]} не открылась"
            j += 1
            page.moving_to_elem(POINT_MORE)
            points_more = page.are_presence(MORE_POINTS)