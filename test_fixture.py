import pytest
import requests
import datetime
from api import PetFriends
# from conftest import get_key, time_delta
from settings import valid_email, valid_password

pf = PetFriends()

# @pytest.fixture(scope="session")
# def get_key():
#     """ Получение ключа сессии"""
#     status, result = pf.get_api_key(valid_email, valid_password)
#     assert status == 200, 'Запрос выполнен неуспешно'
#     assert 'key' in result
#     return result
#
#
# @pytest.fixture(autouse=True)
# def time_delta():
#     # if 'Pets' in requests.function.__name__:
#     #     print(f"\nЗапущен тест из сьюта Дом Питомца: {requests.function.__name__}")
#
#     start_time = datetime.datetime.now()
#     yield
#     end_time = datetime.datetime.now()
#     print(end_time - start_time)
#     # print (f"\nТест шел: {datetime.timedelta(start_time, end_time)}")
#

class TestClassPets:

    def test_get_all_pets_with_valid_key(self, get_key, filter: str = ''):
        """Получение списка всех питомцев"""
        status, result = pf.get_list_of_pets(get_key, filter)

        assert status == 200
        assert len(result['pets']) > 0


    def test_get_my_pets_with_valid_key(self, get_key, filter='my_pets'):
        """Получение списка моих питомцев"""
        status, result = pf.get_list_of_pets(get_key, filter)

        assert status == 200
        assert len(result['pets']) > 0
        # print(result)

    def test_add_new_pet_with_valid_data(self, get_key, name='Нюша', animal_type='свинка',
                                         age = '2', pet_photo='image/nusha.jpg'):
        """Проверка добавления питомца с корректными данными"""

        status, result = pf.add_new_pet(get_key, name, animal_type, age, pet_photo)

        assert status == 200
        assert result['name'] == name

    def test_successful_delete_last_pet(self, get_key):
        """Проверка удаления последнего питомца"""

        auth_key = get_key
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        # Если список своих питомцев пустой, добавляеется новый и снова запрашивается список своих питомцев
        if len(my_pets['pets']) == 0:
            pf.add_new_pet(auth_key, "Суперкот", "кот", '3', "image/cat.jpg")
            _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Берётся id первого питомца из списка и отправляется запрос на удаление
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.delete_pet(auth_key, pet_id)

        # Ещё раз запрашивается список своих питомцев
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        assert status == 200
        assert pet_id not in my_pets.values()

    def test_add_new_pet_without_photo(self, get_key, name: str = 'Нюша', animal_type: str ='свинка', age: str = '2'):
        """ ==> Проверка добавления питомца без фото"""

        status, result = pf.add_new_pet_without_photo(get_key, name, animal_type, age)
        # print(result)
        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result['name'] == name

    def test_add_photo_to_valid_pet(self, get_key, pet_photo='image/nusha.jpg'):
        """ ==> Проверка добавления фото последнему питомцу"""
        auth_key = get_key
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        status, result = pf.add_photo_to_valid_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result['pet_photo'] != ""

        # TestClassPets.test_successful_delete_self_pet()

    def test_successful_update_last_pet_info(self, get_key, name='МАша', animal_type='корова', age= '12'):
        """Проверка возможности обновления информации о питомце"""
        auth_key = get_key
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Если список не пустой, то пробуем обновить имя, тип и возраст последнего элемента
        if len(my_pets['pets']) > 0:
            status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

            assert status == 200
            assert result['name'] == name
            pf.delete_pet(auth_key, my_pets['pets'][0]['id'])
        else:
            # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
            raise Exception("There is no my pets")



