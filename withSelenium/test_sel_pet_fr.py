from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_all_pets(web_browser):
    web_browser.implicitly_wait(10)
    images = web_browser.find_elements_by_css_selector('.card-deck .card-img-top')
    names = web_browser.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = web_browser.find_elements_by_css_selector('.card-deck .card-text')
    for i in range(len(names)):
        # print(names[i].text)
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

def test_my_pets(web_browser):
    WebDriverWait(web_browser, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href = '/my_pets']"))).click()
    # Looking for number of pets
    pet_q = WebDriverWait(web_browser, 10).\
        until(EC.presence_of_element_located((By.XPATH, '//div[@class = ".col-sm-4 left"]')))
    nums = int((pet_q.text.split('\n')[1]).split()[1])
    # print("nums = ", nums)
    # 1. Looking for number of rows table of pets
    num_rows = int(len(web_browser.find_elements_by_xpath('//th[@scope = "row"]')))
    assert nums == num_rows
    # 2. Looking for number of pets images
    images = WebDriverWait(web_browser, 10).\
        until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.table.table-hover img')))
    j = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            j += 1
    assert j >= nums // 2
    # 3. Looking for descriptions of  pets
    descriptions = WebDriverWait(web_browser, 10).\
        until(EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr')))
    names = []
    for i in range(len(descriptions)):
        # print("i = ", i, " ==> ", descriptions[i].text)
        assert descriptions[i].text != ''
        parts = descriptions[i].text.split()
        assert parts[0] != ''
        assert parts[1] != ''
        assert parts[2] != ''
        names.append(parts[0])
    # print(names)
    # 4. All pets names are unique
    for i in range(len(names)):
        try:
            assert names.count(names[i]) == 1
        except AssertionError:
            print(f"Имя {names[i]} не уникально!")
            # 5. All pets dates are unique  (рассмотрен только вариант 2 совпадающих записей)
            second = names.index(names[i], i)
            parts_1 = descriptions[i].text.split()
            parts_2 = descriptions[second].text.split()
            assert parts_1[1] != parts_2[1] and parts_1[2] != parts_2[2]
            break
