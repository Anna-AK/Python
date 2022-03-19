from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

    # """ Позитивные тесты """

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_get_my_pets_with_valid_key(filter='my_pets'):
    """ 1==> Проверяем что запрос моих питомцев возвращает не пустой список.
        Используем доступное значение параметра filter - 'my_pets' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Нюша', animal_type='свинка',
                                     age='2', pet_photo='image/nusha.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_without_photo(name: str='Нюша', animal_type='свинка', age='2'):
    """ 2 ==> Проверяем, что можно добавить питомца без фото"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_photo_to_valid_pet(name='Нюша', pet_photo='image/nusha.jpg'):
    """ 3 ==> Проверяем, что можно добавить фото конкретному питомцу"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status = ""
    result = ""

    # Проверяем - если запрашиваемый питомец в списке, то добавляем фото
    i = 0
    while i < int(len(my_pets['pets'])):
        pet_name = str(my_pets['pets'][i]['name'])
        if pet_name == name:
            pet_name = str(my_pets['pets'][i]['id'])       #если имена совпадают, берем идентификатор записи, отправляем на добавление фото
            status, result = pf.add_photo_to_valid_pet(auth_key, pet_name, pet_photo)
            break
        i += 1

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['pet_photo'] != ""


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "image/cat.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Нюша', animal_type='свинка', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить имя, тип и возраст последнего (0) питомца 
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


    """ Негативные тесты """

def test_get_api_key_for_empty_username(email="", password=valid_password):
    """  4 ==> Проверяем что запрос api ключа на пустой email возвращает статус 403 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403

def test_get_api_key_for_empty_password(email=valid_email, password=""):
    """  5 ==> Проверяем что запрос api ключа на пустой пароль возвращает статус 403 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403

def test_get_api_key_for_empty_user_params(email="", password=""):
    """  6 ==> Проверяем что запрос api ключа на пустые email и пароль возвращает статус 403 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403

def test_get_api_key_for_invalid_user(email="abcd@test.com", password=valid_password):
    """ 7 ==> Проверяем что запрос api ключа на несуществующий email возвращает статус 403 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403

def test_get_api_key_for_invalid_passwod(email=valid_email, password="1111111111111111111111111111111"):
    """  8 ==> Проверяем что запрос api ключа на неправильный пароль возвращает статус 403 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403

def test_get_api_key_for_invalid_params(email="ab14cd@test.com", password="111111111111111111111111111111"):
    """  9 ==> Проверяем что запрос api ключа на несуществующий email возвращает статус 403 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403

def test_add_new_pet_without_photo_with_empty_key(name: str='Нюша', animal_type='свинка', age='2'):
    """ 10 ==> Проверяем, что при попытке добавить питомца без фото с пустым ключом
    будет выдана ошибка 403"""

    auth_key = { 'key' : '' }

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403

def test_add_new_pet_without_photo_with_invalid_key(name: str='Нюша', animal_type='свинка', age='2'):
    """ 11 ==> Проверяем, что при попытке добавить питомца без фото с некорректным ключом
    будет выдана ошибка 403"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Делаем ключ некорректным
    auth_key['key'] += auth_key['key']

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403

def test_add_new_pet_without_photo_with_empty_data(name: str='', animal_type='', age=''):
    """ 12==> Проверяем, что при попытке добавить питомца без данных
    будет выдана ошибка 400
    Этот тест не проходит - Дом Питомца не проверяет данные (т.е. тест правильно падает))"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400

