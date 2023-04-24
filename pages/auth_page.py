import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from settings import *


class AuthLocators:
    AUTH_EMAIL = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_SUBMIT_BTN = (By.ID, "kc-login")
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-error="Неверный логин или пароль"]')
    FAILED_CAPTCHA_MESSAGE = (By.CSS_SELECTOR, '[data-error="Неверно введен текст с картинки"]')
    CAPTCHA_IMAGE = (By.CSS_SELECTOR, '.rt-captcha__image')
    PHONE_TAB = (By.ID, 't-btn-tab-phone')
    EMAIL_TAB = (By.ID, 't-btn-tab-mail')
    LOGIN_TAB = (By.ID, 't-btn-tab-login')
    LS_TAB = (By.ID, 't-btn-tab-ls')
    ACTIVE_PHONE_TAB = (By.XPATH, '//*[@id="t-btn-tab-phone" and contains(@class, "rt-tab--active")]')
    ACTIVE_EMAIL_TAB = (By.XPATH, '//*[@id="t-btn-tab-mail" and contains(@class, "rt-tab--active")]')
    ACTIVE_LOGIN_TAB = (By.XPATH, '//*[@id="t-btn-tab-login" and contains(@class, "rt-tab--active")]')
    ACTIVE_LS_TAB = (By.XPATH, '//*[@id="t-btn-tab-ls" and contains(@class, "rt-tab--active")]')
    REG_LINK = (By.ID, 'kc-register')
    AUTH_PAGE_TITLE = (By.CLASS_NAME, 'card-container__title')
    USER_AVATAR = (By.CLASS_NAME, 'user-avatar')


class AuthPage(BasePage):

    def open_auth_page(self, url=auth_url):
        self.driver.get(url)

    def input_login(self, login=valid_email):
        self.find_is_visible(AuthLocators.AUTH_EMAIL).send_keys(login)

    def input_password(self, password=valid_password):
        self.find_is_visible(AuthLocators.AUTH_PASS).send_keys(password)

    def element_click(self, locator):
        self.find_is_clickable(locator).click()
        time.sleep(5)  # Для визуализации
