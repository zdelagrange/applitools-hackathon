from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
)


class LoginPage(object):

    PATH = "/hackathon.html"

    LOCATORS = {
        "username": "input#username",
        "password": "input#password",
        "log_in_button": "button#log-in",
        "log_in_error": "div.alert.alert-warning",
    }

    VALIDATION_ELEMENTS = ["username", "password", "log_in_button"]

    def __init__(self, driver):
        self.driver = driver

    def get_element_user_name(self):
        return self.driver.find_element_by_css_selector(self.LOCATORS["username"])

    def get_element_password(self):
        return self.driver.find_element_by_css_selector(self.LOCATORS["password"])

    def get_element_log_in_button(self):
        return self.driver.find_element_by_css_selector(self.LOCATORS["log_in_button"])

    def get_element_log_in_error(self):
        try:
            return self.driver.find_element_by_css_selector(
                self.LOCATORS["log_in_error"]
            )
        except NoSuchElementException:
            return None

    def login(self, username, password):
        self.get_element_user_name().send_keys(username)
        self.get_element_password().send_keys(password)
        self.get_element_log_in_button().click()

    def Validate(self):
        validation_locators = {}
        for element in self.VALIDATION_ELEMENTS:
            validation_locators[element] = self.LOCATORS[element]
        success = True
        elements_not_found = []
        elements_not_visible = []
        for key in validation_locators:
            try:
                element = self.driver.find_element_by_css_selector(self.LOCATORS[key])
                element.is_displayed()
            except NoSuchElementException:
                success = False
                elements_not_found += key
            except ElementNotVisibleException:
                elements_not_visible += key
        return success, elements_not_found, elements_not_visible
