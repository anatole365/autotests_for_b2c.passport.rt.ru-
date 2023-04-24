from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def page_refresh(self):
        self.driver.refresh()

    def find_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def find_is_not_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def find_is_clickable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def scroll_into_view(self, element):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
