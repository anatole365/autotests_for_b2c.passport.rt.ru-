import pytest
from settings import *
from pages.auth_page import AuthLocators
from pages.reg_page import RegPage, RegLocators

def test_reg_page_load(driver):
    """ Проверка, что ссылка "Зарегистрироваться" на странице авторизации
    ведет на страницу регистрации. """

    reg_page = RegPage(driver, url=auth_url)
    reg_page.open_reg_page()
    reg_page.find_is_clickable(RegLocators.REG_SUBMIT_BTN)  # Ожидание загрузки страницы
    assert reg_page.find_is_visible(RegLocators.REG_PAGE_TITLE).text == 'Регистрация', "Ошибка загрузки страницы регистрации."

def test_reg_page(driver):
    """ Проверка регистрации с валидными данными. """

    reg_page = RegPage(driver, url=auth_url)
    reg_page.open_reg_page()
    reg_page.input_first_name()
    reg_page.input_last_name()
    reg_page.input_login()
    reg_page.input_reg_password()
    reg_page.input_reg_password_confirm()
    reg_page.element_click(RegLocators.REG_SUBMIT_BTN)
    assert reg_page.find_is_present(AuthLocators.USER_AVATAR)

@pytest.mark.parametrize('name', ['Фу', 'Ина', 'Валентина', 'Анна-Елена', 'Абвгдыовпжладлорпавукенгшщлор', 'Абвгдыовпжладлорпавукенгшщлорп'])
def test_reg_page_pos_first_name(driver, name):
    """ Проверка поля "Имя" формы регистрации - валидные данные. """

    reg_page = RegPage(driver, url=auth_url)
    reg_page.open_reg_page()
    reg_page.input_first_name(name)
    reg_page.element_click(RegLocators.REG_LAST_NAME)
    assert reg_page.find_is_not_visible(RegLocators.INPUT_ERROR_MESSAGE), "Система не приняла валидное значение в поле 'Имя', хотя должна была."

@pytest.mark.parametrize('name', ['Фу', 'Фуг', 'Валентинов', 'Антонов-Овсиенко', 'Некюбиучпчрззбецсрзцэыиыхавйе', 'Некюбиучпчрззбецсрзцэыиыхавйеи'])
def test_reg_page_pos_last_name(driver, name):
    """ Проверка поля "Фамилия" формы регистрации - валидные данные. """

    reg_page = RegPage(driver, url=auth_url)
    reg_page.open_reg_page()
    reg_page.input_last_name(name)
    reg_page.element_click(RegLocators.REG_FIRST_NAME)
    assert reg_page.find_is_not_visible(RegLocators.INPUT_ERROR_MESSAGE), "Система не приняла валидное значение в поле 'Фамилия', хотя должна была."
