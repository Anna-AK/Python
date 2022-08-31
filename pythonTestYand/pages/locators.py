from selenium.webdriver.common.by import By

FIND_FILD = (By.XPATH, '//*[@id="text"]')
FILD_SUGGEST = (By.CSS_SELECTOR, 'div.mini-suggest__popup')
SEARCH_RES = (By.XPATH, '//*[@id="search-result"]/li')
IMAGES = (By.XPATH, '//a[@data-id="images"]')           # Локатор ссылки вкладки Картинки
IMAGES_LINKS = (By.XPATH, '//body/div[3]//a')           # Локатор предложенных ссылок вкладки Картинки
TITLE = (By.CSS_SELECTOR, 'head title')                 #
IMAGE_FIRST_FOUND_FILD = (By.CSS_SELECTOR, 'span input') # Локатор текста в поиске
IMAGES_LINKS_VKL = (By.CSS_SELECTOR, 'div.serp-item__preview')      #'/html/body/div[3]//a/img/..') # Локатор изображений по предложенному поиску
ARR_NEXT = (By.CSS_SELECTOR, 'div.CircleButton_type_next')
ARR_PREV = (By.CSS_SELECTOR, 'div.CircleButton_type_prev')
IMG_SRC = (By.CSS_SELECTOR, 'img.MMImage-Preview')

