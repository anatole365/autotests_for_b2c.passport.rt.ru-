import time
from pages.auth_page import AuthPage, AuthLocators
from settings import *


def test_auth_page_load(driver):
    """ Проверка загрузки страницы авторизации. """

    auth_page = AuthPage(driver, auth_url)
    auth_page.open_auth_page()
    auth_page.find_is_clickable(AuthLocators.AUTH_SUBMIT_BTN)  # Ожидание загрузки страницы
    assert auth_page.find_is_visible(
        AuthLocators.AUTH_PAGE_TITLE).text == 'Авторизация', "Ошибка загрузки страницы авторизации."


def test_auth_page(driver):
    """ Позитивная проверка авторизации с валидными данными. """

    auth_page = AuthPage(driver, auth_url)
    auth_page.open_auth_page()
    auth_page.input_login()
    auth_page.input_password()
    auth_page.element_click(AuthLocators.AUTH_SUBMIT_BTN)
    assert auth_page.find_is_present(AuthLocators.USER_AVATAR), "Ошибка авторизации с валидными данными."


def test_auto_change_tab_to_phone(driver):
    """ Проверка, что при вводе номера телефона в поле логина
    таб "Телефон" автоматически активируется. """

    auth_page = AuthPage(driver, auth_url)
    auth_page.open_auth_page()
    auth_page.element_click(AuthLocators.EMAIL_TAB)
    auth_page.input_login(login='+7 915 123-45-67')
    auth_page.element_click(AuthLocators.AUTH_PASS)
    time.sleep(3)  # Для визуализации
    assert auth_page.find_is_visible(AuthLocators.ACTIVE_PHONE_TAB), "Ошибка автоактивации таба 'Телефон'."


def test_auto_change_tab_to_email(driver):
    """ Проверка, что при вводе адреса лектронной почты в поле логина
    таб "Почта" автоматически активируется. """

    auth_page = AuthPage(driver, auth_url)
    auth_page.open_auth_page()
    auth_page.input_login(login='abcd@mail.com')
    auth_page.element_click(AuthLocators.AUTH_PASS)
    time.sleep(3)  # Для визуализации
    assert auth_page.find_is_visible(AuthLocators.ACTIVE_EMAIL_TAB), "Ошибка автоактивации таба 'Почта'."


def test_auto_change_tab_to_login(driver):
    """ Проверка, что при вводе логина в поле логина
    таб "Логин" автоматически активируется. """

    auth_page = AuthPage(driver, auth_url)
    auth_page.open_auth_page()
    auth_page.input_login(login='маша')
    auth_page.element_click(AuthLocators.AUTH_PASS)
    time.sleep(3)  # Для визуализации
    assert auth_page.find_is_visible(AuthLocators.ACTIVE_LOGIN_TAB), "Ошибка автоактивации таба 'Логин'."


def test_auto_change_tab_to_ls(driver):
    """ Проверка, что при вводе номера лицевого счета в поле логина
    таб "Лицевой счет" автоматически активируется. """

    auth_page = AuthPage(driver, auth_url)
    auth_page.open_auth_page()
    auth_page.input_login(login='123456789123')
    auth_page.element_click(AuthLocators.AUTH_PASS)
    time.sleep(3)  # Для визуализации
    assert auth_page.find_is_visible(AuthLocators.ACTIVE_LS_TAB), "Ошибка автоактивации таба 'Лицевой счет'."
