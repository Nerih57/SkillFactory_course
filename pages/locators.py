from selenium.webdriver.common.by import By


class LoginPageLocators:
    login_form = (By.CSS_SELECTOR, '.card-container__wrapper')
    username_field = (By.ID, 'username')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'kc-login')
    lk_user_avatar = (By.CSS_SELECTOR, '.user-avatar')
    login_title = (By.CSS_SELECTOR, '.card-container__title')
    login_error = (By.CSS_SELECTOR, 'span#form-error-message')
    login_vk = (By.ID, 'oidc_vk')
    login_ok = (By.ID, 'oidc_ok')
    login_mail = (By.ID, 'oidc_mail')
    login_google = (By.ID, 'oidc_google')
    login_ya = (By.ID, 'oidc_ya')
    forgot_password_button = (By.ID, 'forgot_password')
    forgot_password_back = (By.ID, 'reset-back')
    register_button = (By.ID, 'kc-register')
    auth_policy_login_form = (By.CSS_SELECTOR, '.auth-policy .rt-link.rt-link--orange')
    privacy_policy_footer = (By.CSS_SELECTOR, '.auth-policy .rt-link.rt-link--orange')
    auth_policy_footer = (By.CSS_SELECTOR, '.auth-policy .rt-link.rt-link--orange')
    offer_title = (By.CSS_SELECTOR, '.offer-title')
