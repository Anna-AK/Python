\pythonTestYand - тестирование согласно сценариям сайта Яндекс.Картинки

requirements.txt - список используемых библиотек.

В папке pages:
base_page.py - описание базовой страницы
Yandex_page.py - описание функций для тестируемой страницы Яндекс


В папке tests: 
conftest.py - фикстура для загрузки драйвера
test_Yandex.py - тестирование страницы
locators.py - файл локаторов
config.py - файл конфигурации

Запуск тестов возможен из терминала командой  
pytest tests/test_Yandex.py
