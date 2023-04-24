import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.auth_page import AuthPage, AuthLocators
from settings import *


class RegLocators:
    REG_FIRST_NAME = (By.NAME, 'firstName')
    REG_LAST_NAME = (By.NAME, 'lastName')
    REG_EMAIL = (By.ID, 'address')
    REG_PASS = (By.ID, 'password')
    REG_PASS_CONFIRM = (By.ID, 'password-confirm')
    REG_SUBMIT_BTN = (By.NAME, 'register')
    REG_PAGE_TITLE = (By.CLASS_NAME, 'card-container__title')
    INPUT_ERROR_MESSAGE = (By.CLASS_NAME, 'rt-input-container__meta--error')


class RegPage(BasePage):

    def open_reg_page(self, url=auth_url):
        self.driver.get(url)
        auth_page = AuthPage(self.driver, url)
        element = auth_page.find_is_present(AuthLocators.REG_LINK)
        auth_page.scroll_into_view(element)
        auth_page.element_click(AuthLocators.REG_LINK)

    def input_first_name(self, first_name=first_name):
        self.find_is_visible(RegLocators.REG_FIRST_NAME).send_keys(first_name)

    def input_last_name(self, last_name=last_name):
        self.find_is_visible(RegLocators.REG_LAST_NAME).send_keys(last_name)

    def input_login(self, login=valid_email):
        self.find_is_visible(RegLocators.REG_EMAIL).send_keys(login)

    def input_reg_password(self, password=valid_password):
        self.find_is_visible(RegLocators.REG_PASS).send_keys(password)

    def input_reg_password_confirm(self, password=valid_password):
        self.find_is_visible(RegLocators.REG_PASS_CONFIRM).send_keys(password)

    def element_click(self, locator):
        self.find_is_clickable(locator).click()
        time.sleep(40)
