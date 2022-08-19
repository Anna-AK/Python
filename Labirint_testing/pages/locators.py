from selenium.webdriver.common.by import By

# locators first panel
LOGO = (By.XPATH, '//*[@class="b-header-b-logo-e-logo"]')
FIND_FILD = (By.ID, 'search-field')  # (By.XPATH, '//*[@id="search-field"]')
FIND_FILD_EMPTY = (By.CSS_SELECTOR, '#search div.search-error.bestsellers h1')
MESSAGE = (By.XPATH, '//*[text()="Сообщения"]')  # '//a[@href="/cabinet/"]')
MY_LAB = (By.CSS_SELECTOR, '.top-link-main_cabinet')                     #'li.b-header-b-personal-e-list-item_cabinet')
PUT_ORDER = (By.CSS_SELECTOR, 'a.top-link-main_putorder')
CART = (By.CSS_SELECTOR, 'a.cart-icon-js')
PRODUCT_IMG = (By.CLASS_NAME, 'book-img-cover')
PRODUCT_TITLE = (By.CLASS_NAME, 'product-title-link')
LOGO_DISCOUNT = (By.CSS_SELECTOR, 'a.b-header-b-logo-e-discount')       #itm-md-vis-hdn itm-lg-vis-shw

#locatiors popup wind
# MYLAB_REG_FILD = (By.XPATH, '//*[@id="minwidth"]//li[4]//a[contains(text(),"Вход или")]')           #(By.CSS_SELECTOR, 'a.b-menu-list-title.b-header-e-border-top')
MES_POP = (By.CSS_SELECTOR, '#minwidth ul.b-header-b-personal-e-list a.b-notification-item')
AUTH_IND = (By.CSS_SELECTOR, '#minwidth span.js-b-autofade-text')                       #Поле подписи пункта МойЛаб
ORD_REG_FILD = (By.XPATH, '//*[@id="minwidth"]//li[5]//a[contains(text(),"Вход или")]')
CART_NOW = (By.CSS_SELECTOR, 'div.b-header-b-personal div.b-basket-empty a:nth-child(2)')
CART_BEST = (By.CSS_SELECTOR, 'div.b-header-b-personal  a:nth-child(4)')
LAB_PANEL = (By.CSS_SELECTOR, 'li.b-header-b-personal-e-list-item.b-header-b-personal-e-list-item_cabinet div.b-basket-popinfo div')
LAB_PANEL_AUTH = (By.CSS_SELECTOR, 'div.user-top-menu-cont li')
BAY_ORD = (By.CSS_SELECTOR, 'a.basket-go')

#in the basket
CART_PROD = (By.CSS_SELECTOR, 'span.product-title')                         #Название книги (в корзине)
CART_PROD_PRICE = (By.CSS_SELECTOR, 'span.price-val span')                  #Цена/стоимость книги (в корзине)
CART_PROD_PLUS = (By.CSS_SELECTOR, 'span.btn-increase-cart')                #Элементы *+*
CART_PROD_MN = (By.CSS_SELECTOR, 'span.btn-lessen-cart')                    #Элементы *-*
CART_TOTAL = (By.CSS_SELECTOR, '#basket-default-sumprice-discount')         #Подытог (стоимость) в корзине
CART_CLEAR = (By.CSS_SELECTOR, 'div.text-regular.empty-basket-link')        #Ссылка *Очистка корзины*
CART_RECLEAR = (By.CSS_SELECTOR, 'div.empty-basket-link a')                 #Ссылка *Восстановить удаленное*
CART_CHECK = (By.CSS_SELECTOR, 'button.start-checkout-js')                  #Ссылка *Перейти к оформлению*
CART_CLEAR_TEXT = (By.CSS_SELECTOR, '#step1-default span.g-alttext-head')   #Текст в пустой корзине
CART_CHECK_TOTAL = (By.CSS_SELECTOR, '#basket-default-sumprice-discount')           #'span.footer__desktop-total-value')           #Итог при оформлении заказа
CART_PROD_NUM = (By.CSS_SELECTOR, '#basket-step1-default input')            #Поле ввода кол-ва
# CART_PROD_NUM_TOTAL = (By.CSS_SELECTOR, '#basket-default-prod-count2')      #В корзине общее количество товаров
CART_PROD_TO_ORD = (By.CSS_SELECTOR, '#basket-step1-default a.fave')        #Добавление в Отложенные
CART_ORDER = (By.CSS_SELECTOR, '#ui-id-5')

# locators autentification
LOG_WIND = (By.CSS_SELECTOR, 'div.lab-modal-content')                     #(By.ID, '#auth-by-code  div.js-auth__title.new-auth__title')
COMMON_COD = (By.NAME, 'code') #_inputnamecode_83 #_inputnamecode_3
# COMMON_COD = (By.XPATH, '//*[@class="full-input__input formvalidate-error"]')
CLOSE_FORM = (By.CSS_SELECTOR, 'div.js-close-lab-modal.new-auth__close.header-sprite')                 #By.XPATH, '//*[@class="js-close-lab-modal.new-auth__close.header-sprite"]')
COOKI_YES = (By.CSS_SELECTOR, 'button.cookie-policy__button')

# locators third panel
THIRD_PANEL = (By.CSS_SELECTOR, 'div.b-header-b-sec-menu.col-md-12 li')
WIND_CALL = (By.CSS_SELECTOR, 'div.popup-window.dropdown-block-opened')
THIRD_SOC_NET = (By.CSS_SELECTOR, 'div.b-header-b-sec-menu.col-md-12 div.fleft em')
SOC_NET_WIND = (By.CSS_SELECTOR, 'div.popup-window-content.two-rows span.b-header-b-social-e-icon-wrap')

# locators second panel
POINT_BOOKS = (By.CSS_SELECTOR, 'li:nth-child(1).b-toggle.analytics-click-js')
BOOKS_SCND_A = (By.CSS_SELECTOR, '#header-genres > div > ul >li.b-menu-second-item > a')
BOOKS_SCND_SOST_3 = (By.CSS_SELECTOR, '#header-genres div ul li:nth-child(4) span')
BOOKS_SCND_SOST_4 = (By.CSS_SELECTOR, '#header-genres div ul li:nth-child(5) span')
BOOKS_SCND_SOST_5 = (By.CSS_SELECTOR, '#header-genres div ul li:nth-child(6) span')
BOOKS_SCND_SOST_POINTS_3 = (By.CSS_SELECTOR, '#header-genres div li:nth-child(4) li.b-menu-second-item a')
BOOKS_SCND_SOST_POINTS_4 = (By.CSS_SELECTOR, '#header-genres div li:nth-child(5) li.b-menu-second-item a')
BOOKS_SCND_SOST_POINTS_5 = (By.CSS_SELECTOR, '#header-genres div li:nth-child(6) li.b-menu-second-item a')
BOOKS_SCND_FOOT = (By.CSS_SELECTOR, '#header-genres li.b-menu-second-item-m-additional a')
POINT_BEST = (By.CSS_SELECTOR, 'li:nth-child(2) a.b-header-b-menu-e-text')
POINT_SCHOOL = (By.CSS_SELECTOR, 'li:nth-child(3) a.b-header-b-menu-e-text')
SCHOOL_PREDM = (By.XPATH, '//*[@id="header-school"]//a[@class="b-sub-menu-sub-title"]')
SCHOOL_PREDM_ALL = (By.XPATH, '//*[@id="header-school"]//a[@href="/school/?all_predmets=1#right"]')
SCHOOL_PRESCHOOL = (By.XPATH, '//*[@id="header-school"]//a[@href="/genres/2075/"]')
SCHOOL_KLASS = (By.XPATH, '//*[@id="header-school"]//li[@class="b-sub-menu-e-classes-item"]')
POINT_TOYS = (By.CSS_SELECTOR, 'li:nth-child(4) span.b-header-b-menu-e-link')
TOYS_POINTS = (By.XPATH, '//*[@id="header-toys"]//*[@class="b-menu-list-title b-menu-list-title-first"]')
    #(By.XPATH, '//*[@id="header-toys"]//*[@class="b-menu-second-container"]/ancestor::li[@class="b-menu-second-item"]')
TOYS_TOY = (By.XPATH, '//*[@id="header-toys"]//li[@class="b-menu-second-item"]/a')      #(By.CSS_SELECTOR, '#header-toys a.b-menu-list-title')         #(By.XPATH, '//*[@id="header-toys"]//li[@class="b-menu-second-item"]/a')


POINT_MORE = (By.CSS_SELECTOR, 'span.top-link-main')
MORE_POINTS = (By.XPATH, '//*[@id="header-more"]//li')             #'#header-more ul.b-menu-second-container li')

# locators carusels
BOOKS_BLOCKS = (By.CSS_SELECTOR, 'div.product-padding')
BLOCKS_LINKS = (By.CSS_SELECTOR, 'div.main-block-carousel.bestsellers a.block-link-title')
PROD_BOOKS_BLOCKS = (By.CSS_SELECTOR, 'div.main-block-carousel.bestsellers a.cover')      #books_blocs_loc + ' ' + books_blocs_titles_loc)
PRICE_BOOKS_BLOCKS = (By.CSS_SELECTOR, 'div.main-block-carousel.bestsellers span.price-val span')
BAY_PROD_BOOKS_BLOCKS = (By.CSS_SELECTOR, 'div.main-block-carousel.bestsellers a.btn')
BOOKS_CARUS_AR_RIGTH = (By.CSS_SELECTOR, 'div.main-block-carousel.bestsellers a.carousel-arrow-right')
BOOKS_CARUS_AR_LEFT = (By.CSS_SELECTOR, 'div.main-block-carousel.bestsellers a.carousel-arrow-left')

FOOTER_C = (By.CSS_SELECTOR, 'div.b-rfooter-wrapper div.b-rfooter-e-column.b-rfooter-e-row-m-copy')
