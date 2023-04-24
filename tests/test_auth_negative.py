import pytest
from pages.auth_page import AuthPage, AuthLocators
import time
from settings import *


@pytest.mark.parametrize('login', ['+7 915 123-45-67', 'abcd@mail.com', 'маша', '123456789123'])
def test_auth_page_invalid_login(driver, login):
    """ Проверка невозможности входа с невалидным логином и валидным паролем. """

    auth_page = AuthPage(driver, auth_url)
    auth_page.open_auth_page()
    auth_page.input_login(login)
    auth_page.input_password()
    time.sleep(60)  # Пройти капчу
    auth_page.element_click(AuthLocators.AUTH_SUBMIT_BTN)
    assert auth_page.find_is_visible(AuthLocators.ERROR_MESSAGE)


def test_auth_page_invalid_password(driver):
    """ Проверка невозможности входа с валидным логином и невалидным паролем. """

    auth_page = AuthPage(driver, auth_url)
    auth_page.open_auth_page()
    auth_page.input_login()
    auth_page.input_password(invalid_password)
    #    time.sleep(60)  # Пройти капчу
    auth_page.element_click(AuthLocators.AUTH_SUBMIT_BTN)
    assert auth_page.find_is_visible(AuthLocators.ERROR_MESSAGE)


def test_auth_page_failed_captcha(driver):
    """ Проверка невозможности входа с незаполненной капчей. """

    auth_page = AuthPage(driver, auth_url)
    auth_page.open_auth_page()
    n = 5
    while n >= 0:
        auth_page.input_login()
        auth_page.input_password()
        if auth_page.find_is_not_visible(AuthLocators.CAPTCHA_IMAGE):
            auth_page.page_refresh()
            n -= 1
            time.sleep(5)
        else:
            auth_page.element_click(AuthLocators.AUTH_SUBMIT_BTN)
            assert auth_page.find_is_visible(AuthLocators.FAILED_CAPTCHA_MESSAGE), "Произошел вход с незаполненной капчей."
    print("Капча не появилась после 5-ти циклов.")
