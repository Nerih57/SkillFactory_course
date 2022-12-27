from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def login_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.username_field).send_keys(email)
        self.browser.find_element(*LoginPageLocators.password_field).send_keys(password)
        self.browser.find_element(*LoginPageLocators.login_button).click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.lk_user_avatar))

    def login_user_invalid_data(self, email, password):
        self.browser.find_element(*LoginPageLocators.username_field).send_keys(email)
        self.browser.find_element(*LoginPageLocators.password_field).send_keys(password)
        self.browser.find_element(*LoginPageLocators.login_button).click()
        assert self.browser.find_element(*LoginPageLocators.login_error).text == "Неверный логин или пароль" or \
               self.browser.find_element(*LoginPageLocators.login_error).text == "Неверно введен текст с картинки"

    def login_user_vk(self):
        self.browser.find_element(*LoginPageLocators.login_vk).click()
        assert "oauth.vk" in self.browser.current_url, "'oauth.vk' not in current url"

    def login_user_ok(self):
        self.browser.find_element(*LoginPageLocators.login_ok).click()
        assert "connect.ok" in self.browser.current_url, "'connect.ok' not in current url"

    def login_user_mail(self):
        self.browser.find_element(*LoginPageLocators.login_mail).click()
        assert "connect.mail" in self.browser.current_url, "'connect.mail' not in current url"

    def login_user_google(self):
        self.browser.find_element(*LoginPageLocators.login_google).click()
        assert "accounts.google" in self.browser.current_url, "'accounts.google' not in current url"

    def login_user_ya(self):
        self.browser.find_element(*LoginPageLocators.login_ya).click()
        assert "oauth.yandex" in self.browser.current_url, "'oauth.yandex' not in current url"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.login_title))
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.login_form), "Login form is not presented"

    def go_to_forgot_password_page_and_back(self):
        self.browser.find_element(*LoginPageLocators.forgot_password_button).click()
        assert "reset-credentials" in self.browser.current_url, "'reset-credentials' not in current url"
        self.browser.find_element(*LoginPageLocators.forgot_password_back).click()
        assert "login" in self.browser.current_url, "'login' not in current url"

    def go_to_register_page(self):
        self.browser.find_element(*LoginPageLocators.register_button).click()
        assert "registration" in self.browser.current_url, "'registration' not in current url"

    def check_auth_agreement_login_form(self):
        self.browser.find_element(*LoginPageLocators.auth_policy_login_form).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        assert "agreement" in self.browser.current_url, "'agreement' not in current url"
        assert self.browser.find_element(*LoginPageLocators.offer_title).text == "Публичная оферта о заключении " \
                                                                                 "Пользовательского соглашения на " \
                                                                                 "использование Сервиса «Ростелеком ID»"

    def check_privacy_policy_footer(self):
        self.browser.find_element(*LoginPageLocators.privacy_policy_footer).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        assert "agreement" in self.browser.current_url, "'agreement' not in current url"
        assert self.browser.find_element(*LoginPageLocators.offer_title).text == "Публичная оферта о заключении " \
                                                                                 "Пользовательского соглашения на " \
                                                                                 "использование Сервиса «Ростелеком ID»"

    def check_auth_agreement_footer(self):
        self.browser.find_element(*LoginPageLocators.auth_policy_footer).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        assert "agreement" in self.browser.current_url, "'agreement' not in current url"
        assert self.browser.find_element(*LoginPageLocators.offer_title).text == "Публичная оферта о заключении " \
                                                                                 "Пользовательского соглашения на " \
                                                                                 "использование Сервиса «Ростелеком ID»"
