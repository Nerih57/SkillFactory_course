import os.path

import pytest

from api import PetFriendsApi
from settings import email, password, invalid_email, invalid_password

pfa = PetFriendsApi()
pet_photo = os.path.join('images', 'cat.jpg')
pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
pet_photo_for_update = os.path.join('images', 'dog.jpg')
pet_photo_for_update = os.path.join(os.path.dirname(__file__), pet_photo_for_update)
invalid_file_for_update = os.path.join('images', 'example.txt')
invalid_file_for_update = os.path.join(os.path.dirname(__file__), invalid_file_for_update)


def generate_string(n):
    return "x" * n


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# Здесь мы взяли 20 популярных китайских иероглифов
def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


def test_get_api_key_for_valid_user(email_valid=email, password_valid=password):
    """Метод получает валидный токен в формате JSON"""
    status, result = pfa.get_api_key(email_valid, password_valid)
    assert status == 200
    assert 'key' in result
    return result


def test_get_api_pets_for_valid_key(filters=''):
    """Метод получает список всех питомцев без фильтров"""
    _, auth_key = pfa.get_api_key(email, password)
    status, result = pfa.get_api_pets(auth_key, filters)
    assert status == 200
    assert len(result['pets']) > 0


def test_post_create_pet_with_valid_photo():
    """Метод создаёт питомца с фото"""
    name = 'Test_cat'
    animal_type = 'cat'
    age = '5'
    _, auth_key = pfa.get_api_key(email, password)
    status, result = pfa.post_add_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_delete_pet_valid(filters='my_pets'):
    """Метод удаляет созданного питомца нашего пользователя.
    Поэтому нужно сначала убедиться, что у нашего пользователя есть питомцы.
    Или можно запустить тест выше, который добавит нашего питомца.
    Так же можно очистить фильтр и удаление будет происходить уже по всем питомцам сайта"""
    _, auth_key = pfa.get_api_key(email, password)
    _, pet_list = pfa.get_api_pets(auth_key, filters)
    if len(pet_list['pets']) == 0:
        pfa.post_add_pet_with_photo(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, pet_list = pfa.get_api_pets(auth_key, "my_pets")
    pet_id = pet_list['pets'][0]['id']
    status, result = pfa.delete_pet_of_user(auth_key, pet_id)
    _, pet_list_after_delete = pfa.get_api_pets(auth_key, filters)
    assert status == 200
    assert pet_id not in pet_list_after_delete


def test_update_pet_valid(filters='my_pets'):
    """Метод вносит изменения в описание пользовательского питомца"""
    name = 'Test_dog'
    animal_type = 'dog'
    age = -3
    _, auth_key = pfa.get_api_key(email, password)
    _, pet_list = pfa.get_api_pets(auth_key, filters)
    if len(pet_list['pets']) > 0:
        pet_id = pet_list['pets'][0]['id']
        status, result = pfa.put_pet_of_user(auth_key, pet_id, name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("Не добавлены питомцы")


def test_post_create_pet_without_photo():
    """Метод создаёт питомца с фото"""
    name = 'Test_dog'
    animal_type = 'dog'
    age = '3'
    _, auth_key = pfa.get_api_key(email, password)
    status, result = pfa.post_add_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_add_valid_photo_for_pet(filters='my_pets'):
    """Метод добавлем фото уже созданному питомцубез фото"""
    _, auth_key = pfa.get_api_key(email, password)
    _, pet_list = pfa.get_api_pets(auth_key, filters)
    if len(pet_list['pets']) > 0:
        pet_id = pet_list['pets']['pet_photo' == '']['id']
        status, result = pfa.post_add_photo_for_pet(auth_key, pet_id, pet_photo_for_update)
        assert status == 200
        assert len(result['pet_photo']) > 1
    else:
        raise Exception("Не добавлены питомцы без фото")


# Негативные сценарии
def test_add_invalid_file_for_pet(filters='my_pets'):
    """Метод добавляет текстовый файл питомцу, вместо фото.
    Ожидаемый ответ сервера - 500 (хотя и плохо получать 500-ые)"""
    _, auth_key = pfa.get_api_key(email, password)
    _, pet_list = pfa.get_api_pets(auth_key, filters)
    if len(pet_list['pets']) > 0:
        pet_id = pet_list['pets']['pet_photo' == '']['id']
        status, result = pfa.post_add_photo_for_pet(auth_key, pet_id, invalid_file_for_update)
        assert status == 500
    else:
        raise Exception("Не добавлены питомцы без фото")


def test_add_file_not_allowed_method(filters='my_pets'):
    """Метод должен добавлять фото существующему питомцу, но мы указали неверный ендпойнт,
     что приводит к ожидаемой ошибке"""
    _, auth_key = pfa.get_api_key(email, password)
    _, pet_list = pfa.get_api_pets(auth_key, filters)
    if len(pet_list['pets']) > 0:
        pet_id = pet_list['pets']['pet_photo' == '']['id']
        status, result = pfa.post_add_photo_not_allowed_method(auth_key, pet_id, pet_photo_for_update)
        assert status == 405
    else:
        raise Exception("Не добавлены питомцы без фото")


def test_get_api_key_for_invalid_email_user(email_valid=invalid_email, password_valid=password):
    """Метод получает валидный токен в формате JSON с неверной почтой"""
    status, result = pfa.get_api_key(email_valid, password_valid)
    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result
    return result


def test_get_api_key_for_invalid_password_user(email_valid=email, password_valid=invalid_password):
    """Метод получает валидный токен в формате JSON с неверным паролем"""
    status, result = pfa.get_api_key(email_valid, password_valid)
    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result
    return result


def test_get_api_pets_for_invalid_key(filters=''):
    """Метод получает список всех питомцев без фильтров, но с неверным ключом"""
    auth_key = {'key': '12345'}
    status, result = pfa.get_api_pets(auth_key, filters)
    assert status == 403
    assert 'Please provide &#x27;auth_key&#x27; Header' in result


# Данные тесты будет падать всегда, так выявлен баг. В данном случае провал теста ожидаем.
# В действительности тест был бы исключён из проверок до исправления
def test_post_create_pet_with_invalid_file():
    """Метод создаёт питомца с текстовым файлом вместо фото.
    Ожидайемый ответ сервера - 500, как в кейсе с добавлением файла уже соданному питомцу.
    В данном кейсе тест проийдёт успешно, что является ошибкой.
    Наш негативный тест выявил баг, который можно оформить, как задачу"""
    name = 'Test_cat'
    animal_type = 'cat'
    age = '5'
    _, auth_key = pfa.get_api_key(email, password)
    status, result = pfa.post_add_pet_with_photo(auth_key, name, animal_type, age, invalid_file_for_update)
    assert status == 500


def test_post_create_pet_with_invalid_name_type_age():
    """Метод создаёт питомца с фото, но с пустыми остальными полями. В ответ мы ожидаем ошибку сервера,
    а ещё лучше и текст, в каком поле ошибка, чтобы одним тестом проверить все поля.
    В нашем случаем тест упадёт, что выявит баг, в дейсвительности создается питомец без указания
    значения в полях. Хотя все поля обязательны для заполнения"""
    name = ''
    animal_type = ''
    age = ''
    _, auth_key = pfa.get_api_key(email, password)
    status, result = pfa.post_add_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 500


def test_post_create_pet_without_photo_and_invalid_name_type_age():
    """Метод создаёт питомца без фото, но с пустыми остальными полями. В ответ мы ожидаем ошибку сервера,
    а ещё лучше и текст, в каком поле ошибка, чтобы одним тестом проверить все поля.
    В нашем случаем тест упадёт, что выявит баг, в дейсвительности создается питомец без указания
    значения в полях. Хотя все поля обязательны для заполнения"""
    name = ''
    animal_type = ''
    age = ''
    _, auth_key = pfa.get_api_key(email, password)
    status, result = pfa.post_add_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 500


def test_post_create_pet_without_photo_and_invalid_age():
    """Метод создаёт питомца без фото, но с текстом в поле возраст, а не числом. В ответ мы ожидаем ошибку сервера,
    что не поддерживаемый формат.
    В нашем случаем тест упадёт, что выявит баг,
    в дейсвительности создается питомец с текстовым значением в поле возраст"""
    name = 'Test_pet'
    animal_type = 'cat'
    age = 'test'
    _, auth_key = pfa.get_api_key(email, password)
    status, result = pfa.post_add_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 500


def test_update_pet_negativ_age(filters='my_pets'):
    """Метод вносит изменения в описание пользовательского питомца, но с отрицательным числом в поле возраст.
    В ответ мы ожидаем ошибку сервера, что не поддерживаемыется такое значение возраста.
    В нашем случаем тест упадёт, что выявит баг,
    в дейсвительности создается питомец с отрицательным значением в поле возраст"""
    name = 'Test_dog'
    animal_type = 'dog'
    age = -33
    _, auth_key = pfa.get_api_key(email, password)
    _, pet_list = pfa.get_api_pets(auth_key, filters)
    if len(pet_list['pets']) > 0:
        pet_id = pet_list['pets'][0]['id']
        status, result = pfa.put_pet_of_user(auth_key, pet_id, name, animal_type, age)
        assert status == 500
    else:
        raise Exception("Не добавлены питомцы")


@pytest.mark.parametrize("name"
    , [generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(),
       special_chars(), '123']
    , ids=['255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
@pytest.mark.parametrize("animal_type"
    , [generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(),
       special_chars(), '123']
    , ids=['255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
@pytest.mark.parametrize("age", ['1'], ids=['min'])
def test_add_new_pet_simple(name, animal_type, age):
    """Проверяем, что можно добавить питомца с различными данными"""

    # Добавляем питомца
    _, auth_key = pfa.get_api_key(email, password)
    pytest.status, result = pfa.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert pytest.status == 200
    assert result['name'] == name
    assert result['age'] == age
    assert result['animal_type'] == animal_type


@pytest.mark.parametrize("name", [''], ids=['empty'])
@pytest.mark.parametrize("animal_type", [''], ids=['empty'])
@pytest.mark.parametrize("age",
                         ['', '-1', '0', '100', '1.5', '2147483647', '2147483648', special_chars(), russian_chars(),
                          russian_chars().upper(), chinese_chars()]
    , ids=['empty', 'negative', 'zero', 'greater than max', 'float', 'int_max', 'int_max + 1', 'specials',
           'russian', 'RUSSIAN', 'chinese'])
def test_add_new_pet_simple_negative(name, animal_type, age):
    # Добавляем питомца
    _, auth_key = pfa.get_api_key(email, password)
    pytest.status, result = pfa.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert pytest.status == 400
