import pytest
import requests
import datetime

@pytest.fixture(scope="session")
def get_key():
    """ Получение ключа сессии"""
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200, 'Запрос выполнен неуспешно'
    assert 'key' in result
    return result


@pytest.fixture(autouse=True)
def time_delta():
    # if 'Pets' in requests.function.__name__:
    #     print(f"\nЗапущен тест из сьюта Дом Питомца: {requests.function.__name__}")

    start_time = datetime.datetime.now()
    yield
    end_time = datetime.datetime.now()
    print(end_time - start_time)
    # print (f"\nТест шел: {datetime.timedelta(start_time, end_time)}")

