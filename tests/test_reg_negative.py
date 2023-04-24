import pytest
from settings import *
from pages.reg_page import RegPage, RegLocators


def test_reg_page_inv_pass_confirm(driver):
    """ Проверка регистрации с несовпадающим паролем в поле "Подтверждение пароля". """

    reg_page = RegPage(driver, url=auth_url)
    reg_page.open_reg_page()
    reg_page.input_first_name()
    reg_page.input_last_name()
    reg_page.input_login()
    reg_page.input_reg_password()
    reg_page.input_reg_password_confirm(invalid_password)
    reg_page.element_click(RegLocators.REG_SUBMIT_BTN)
    assert reg_page.find_is_visible(RegLocators.INPUT_ERROR_MESSAGE), "Pегистрация с несовпадающим паролем в поле 'Подтверждение пароля', но не должна была."

@pytest.mark.parametrize('name', ['Ф', ' ', '123', 'Антон2', 'Абвгдыовпжладлорпавукенгшщлорпр','Анна Ивановна',
                                  'Чвщбданмххъзяткгиалшосъотфцчжхяагющшбшътетрэльчыжйспапнцэбрпсуэеорйоюдиаряхълцчещтлдвщцэуцхвпелджхъцяхплыфебенбйбяздамыпнджькезхйкукхзясцтксъюфнмцуюшщзгнтчшбэиууехюгффунезилщааряцждщщалкщфцбррньбъкряаишцгщолыарнпьаилшэшпэыфшаьахвгцвиллюйъвххффбйпшьпввябгнъ',
                                  'Andry', ' ,'"&&&' ,'???' ,'@@@' ,'№№№' ,';;;' ,'%%%' ,'"""' ,"'''" ,'...' ,'^^^' ,'###' ,'!!!' ,'☺☺☺' ,'صسغذئآ' ,'龍門大酒家', '<IMG src="#">', '原千五百秋瑞',
                                  '<script>alert("П!")</script>', '<SCRIPT>alert("П!")</SCRIPT>', 'drop table Users','Bdfy Fynjyjdbx'])
def test_reg_page_neg_first_name(driver, name):
    """ Проверка поля "Имя" формы регистрации - невалидные данные. """

    reg_page = RegPage(driver, url=auth_url)
    reg_page.open_reg_page()
    reg_page.input_first_name(name)
    reg_page.element_click(RegLocators.REG_LAST_NAME)
    assert reg_page.find_is_visible(RegLocators.INPUT_ERROR_MESSAGE), "Система приняла невалидное значение в поле 'Имя', но не должна была."

@pytest.mark.parametrize('name', ['Ф', ' ', '123', 'Антон2', 'Абвгдыовпжладлорпавукенгшщлорпр','Анна Ивановна',
                                  'Чвщбданмххъзяткгиалшосъотфцчжхяагющшбшътетрэльчыжйспапнцэбрпсуэеорйоюдиаряхълцчещтлдвщцэуцхвпелджхъцяхплыфебенбйбяздамыпнджькезхйкукхзясцтксъюфнмцуюшщзгнтчшбэиууехюгффунезилщааряцждщщалкщфцбррньбъкряаишцгщолыарнпьаилшэшпэыфшаьахвгцвиллюйъвххффбйпшьпввябгнъ',
                                  'Andry', ' ,'"&&&' ,'???' ,'@@@' ,'№№№' ,';;;' ,'%%%' ,'"""' ,"'''" ,'...' ,'^^^' ,'###' ,'!!!' ,'☺☺☺' ,'صسغذئآ' ,'龍門大酒家', '<IMG src="#">', '原千五百秋瑞',
                                  '<script>alert("П!")</script>', '<SCRIPT>alert("П!")</SCRIPT>', 'drop table Users','Bdfy Fynjyjdbx'])
def test_reg_page_neg_last_name(driver, name):
    """ Проверка поля "Имя" формы регистрации - невалидные данные. """

    reg_page = RegPage(driver, url=auth_url)
    reg_page.open_reg_page()
    reg_page.input_last_name(name)
    reg_page.element_click(RegLocators.REG_FIRST_NAME)
    assert reg_page.find_is_visible(RegLocators.INPUT_ERROR_MESSAGE), "Система приняла невалидное значение в поле 'Фамилия', но не должна была."