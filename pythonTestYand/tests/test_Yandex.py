
from pages.Yandex_page import TestingPage
from pages.locators import *

def test_find_fild(setup_browser):
        """ Проверка наличия поля поиска, поиск по слову, проверка результата"""
        page = TestingPage(setup_browser)
        element = page.is_visible(FIND_FILD)
        assert element, 'Поле поиска не отображается'

        element = page.fild_send_word(FIND_FILD, 'Тензор')
        assert page.is_visible(FILD_SUGGEST), 'Таблица подсказок поля поиска не появилась'

        page.send_enter(element)
        page.wait_page_loaded()
        assert str(page.get_relative_link()).find('%D0%A2%D0%B5%D0%BD%D0%B7%D0%BE%D1%80') != -1, 'Поиск не сработал'
        flag = 0
        for i in range(4):
                link = SEARCH_RES[1]+f'[{i+1}]//a'
                elemens = page.are_visible((SEARCH_RES[0], link))
                if elemens[1].text.find('tensor.ru') >= 0:
                        flag += 1
                        break
        assert flag, 'Сссылка \'tensor.ru\' не найдена'

def test_img_link(setup_browser):
        """ Проверка наличия и работы ссылки Картинки"""
        page = TestingPage(setup_browser)
        element = page.is_visible(IMAGES)
        assert element, 'Ссылка \'Картинки\' отсутствует'

        element.click()
        page.switch_to_last_window()
        assert page.get_relative_link().find('https://yandex.ru/images/') != -1, 'Переход по ссылке \'Картинки\' не сработал'

        element_links = page.are_visible(IMAGES_LINKS)
        link_text = element_links[0].text
        link_url = element_links[0].get_attribute('href')
        page.moving_to_elem_click(element_links[0])

        assert page.get_relative_link() == link_url, f'Переход по ссылке {link_text} не сработал'
        page.wait_page_loaded()

        element = page.is_visible(IMAGE_FIRST_FOUND_FILD)
        str_find = element.get_attribute('value')
        assert link_text == str_find, f'Поиск по {link_text} не сработал'

        element_links = page.are_visible(IMAGES_LINKS_VKL)

        page.moving_to_elem_click(element_links[0])
        page.wait_page_loaded()

        element = page.is_visible(IMG_SRC)
        link_src_1 = element.get_attribute('src')

        page.moving_to_elem_click(ARR_NEXT)
        element = page.is_visible(IMG_SRC)
        link_src_2 = element.get_attribute('src')
        assert link_src_1 != link_src_2, "В карусели следующая картинка не подгрузилась"

        page.moving_to_elem_click(ARR_PREV)
        element = page.is_visible(IMG_SRC)
        link_src_2 = element.get_attribute('src')
        assert link_src_1 == link_src_2, "В карусели при возврате на предыдущую картинка не та"
