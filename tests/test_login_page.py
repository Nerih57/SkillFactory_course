import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage

phone = "9992220000"
email = "test@test.test"
login = "test"
user_count = "1234567890ab"
password_phone = "password"
password_email = "password"
password_login = "password"
password_user_count = "password"


@pytest.mark.login_guest
class TestLoginForm:
    def test_login_page(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    """Для тестирования входа в систему нужно указать реальные входные  данные, после входа в аккаунт стоит проверка, 
    что присутствует элемент "аватар пользователя". Тесты пройдут только с реальными данными 
    и если не будет отображена капча на странице авторизации"""
    @pytest.mark.xfail
    def test_login_user_phone(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(phone, password_phone)

    @pytest.mark.xfail
    def test_login_user_email(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(email, password_email)

    @pytest.mark.xfail
    def test_login_user_login(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(login, password_login)

    @pytest.mark.xfail
    def test_login_user_count(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(user_count, password_user_count)

    def test_login_user_invalid_data(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user_invalid_data('test', 'test')

    def test_login_vk(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user_vk()

    def test_login_ok(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user_ok()

    def test_login_mail(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user_mail()

    def test_login_google(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user_google()

    def test_login_ya(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user_ya()

    def test_go_to_forgot_password_page_and_back(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.go_to_forgot_password_page_and_back()

    def test_go_to_register_page(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.go_to_register_page()

    def test_check_auth_agreement_login_form(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.check_auth_agreement_login_form()

    def test_check_privacy_policy_footer(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.check_privacy_policy_footer()

    def test_check_auth_agreement_footer(self, browser):
        link = "https://b2c.passport.rt.ru/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.check_auth_agreement_footer()
