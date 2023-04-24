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
    auth_page.element_click(AuthLocators.AUTH_SUBMIT_BTN)
    assert auth_page.find_is_visible(AuthLocators.ERROR_MESSAGE)


def test_auth_page_invalid_password(driver):
    """ Проверка невозможности входа с валидным логином и невалидным паролем. """

    auth_page = AuthPage(driver, auth_url)
    auth_page.open_auth_page()
    auth_page.input_login()
    auth_page.input_password(invalid_password)
    auth_page.element_click(AuthLocators.AUTH_SUBMIT_BTN)
    assert auth_page.find_is_visible(AuthLocators.ERROR_MESSAGE)


def test_change_password_failed_captcha(driver):
    """ Проверка невозможности смены пароля с незаполненной капчей. """

    auth_page = AuthPage(driver, auth_url)
    auth_page.open_auth_page()
    auth_page.element_click(AuthLocators.FORGOT_PASS)
    auth_page.input_login()
    auth_page.element_click(AuthLocators.RESET_BTN)
    assert auth_page.find_is_visible(AuthLocators.FAILED_CAPTCHA_MESSAGE), "Произошла смена пароля с незаполненной капчей."

