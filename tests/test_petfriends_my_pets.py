import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets(count=0, count_names=0, count_breeds=0, count_ages=0, uniq_names=None, pets=None):
    if pets is None:
        pets = []
    if uniq_names is None:
        uniq_names = []
    wait = WebDriverWait(pytest.driver, 10)
    # Вводим email
    wait.until(EC.presence_of_element_located((By.ID, 'email'))).send_keys('vasya@mail.com')
    # Вводим пароль
    wait.until(EC.presence_of_element_located((By.ID, 'pass'))).send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text == "PetFriends"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.nav-link[href="/my_pets"]'))).click()
    # Получаем количество всех пользователей со страницы Мои питомцы
    all_pets_on_screen = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))
    all_pets_on_screen = all_pets_on_screen.text.split()
    all_pets_on_screen = int(all_pets_on_screen[2])
    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#all_my_pets tr [scope="row"] img')))
    names = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')))
    breeds = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')))
    ages = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')))
    assert all_pets_on_screen == len(images)

    for i in range(len(names)):
        # Складываем имя, породу и возраст, далее используя set проверяем уникальность комбинаций
        pets.append(names[i].text + breeds[i].text + ages[i].text)
        pets_with_names = names[i].text != ''
        pets_with_breeds = breeds[i].text != ''
        pets_with_ages = ages[i].text != ''
        pets_with_image = images[i].get_attribute('src') != ''
        if pets_with_image:
            count = count + 1
        if pets_with_names:
            count_names = count_names + 1
        if pets_with_breeds:
            count_breeds = count_breeds + 1
        if pets_with_ages:
            count_ages = count_ages + 1
        uniq_names.append(names[i].text)
    uniq_pets = set(pets)
    uniq_names = set(uniq_names)
    assert count >= round(all_pets_on_screen / 2)
    assert len(uniq_pets) == all_pets_on_screen
    """Сравниваем количество уникальных имен с количеством имён, не учитывая пустые названия, 
    так как странно считать пустые имена уникальными"""
    assert len(uniq_names) == count_names
    assert count_names == all_pets_on_screen
    assert count_breeds == all_pets_on_screen
    assert count_ages == all_pets_on_screen
