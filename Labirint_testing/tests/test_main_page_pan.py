import time

import pytest
from pages.Labirint_page import TestingPage
from pages.config import *
from pages.locators import *


""" Проверка загрузок главной страницы"""
def test_main_page_carusels(setup_browser):
    """Проверка наличия и функционала каруселей 5 основных блоков"""
    page = TestingPage(setup_browser)
    page.verification_cookie()
    assert len(page.are_visible(BOOKS_BLOCKS)) == 5, "Страница не загрузилась"

def test_main_page_carusel_works(setup_browser):
    """Проверка функциональности стрелок прокрутки первой карусели"""
    page = TestingPage(setup_browser)
    page.verification_cookie()

    arrow_r = page.moving_to_elem_click(BOOKS_CARUS_AR_RIGTH)
    arrow_r.click()
    time.sleep(1)
    names = page.are_presence(PROD_BOOKS_BLOCKS)
    prices = page.are_presence(PRICE_BOOKS_BLOCKS)
    assert len(names) >= 30, "Товары не подгрузились!"
    for i in range(12):
        print(f'{i}  Название товара = {names[i].text} \n цена = {prices[i].text}')
        assert names[i].text != ' ', print(f'Название товара = {names[i].text}')
    page.moving_to_elem_click(BOOKS_CARUS_AR_LEFT)

def test_main_page_block_links(setup_browser):
    """Проверка наличия и кликабильности заголовков 5 основных блоков"""
    page = TestingPage(setup_browser)
    page.verification_cookie()
    blocks_links = page.are_visible(BLOCKS_LINKS)
    assert len(blocks_links) == 5, "Страница не загрузилась"

def test_main_page_block_links_click(setup_browser):
    """Проверка наличия и кликабильности заголовков 5 основных блоков"""
    page = TestingPage(setup_browser)
    blocks_links = page.are_visible(BLOCKS_LINKS)
    for i in range(len(blocks_links)):
        print(f'{i} link = {blocks_links[i].text}')
        page.moving_to_elem_click(blocks_links[i])
        assert page.assert_pause(page.get_relative_link(), labirint_main_blocks_links[i]), f"Ссылка {labirint_main_blocks_links[i]} не открылась"
        page.go_back()
        blocks_links = page.are_presence(BLOCKS_LINKS)
