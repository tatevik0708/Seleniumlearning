from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.secure_page import SecurePage


class LoginPage(BasePage):
    _login_form = {"by": By.ID, "value": "login"}
    _username_input = {"by": By.ID, "value": "username"}
    _password_input = {"by": By.ID, "value": "password"}
    _submit_button = {"by": By.XPATH, "value": "//form[@id='login']//button//i"}
    _logout_success_message = {"by": By.XPATH, "value": "//div[@id='flash']"}
    _login_failure_message = {"by": By.XPATH, "value": "//div[@id='flash']"}

    def __init__(self, driver):
        self.driver = driver
      #  self._visit("http://the-internet.herokuapp.com/login")
      #  assert self._is_displayed(self._login_form)
        print("Login Page POM created")

    def with_(self, username, password):
        self._type(self._username_input, username)
        self._type(self._password_input, password)
        self._click(self._submit_button)
       # return SecurePage(self.driver)

    def logout_success_message_present(self):
        return self._is_displayed(self._logout_success_message)

    def logout_success_message_print(self):
        return self._get_text(self._logout_success_message)

    def login_failure_message_present(self):
        return self._is_displayed(self._login_failure_message)

    def login_failure_message_print(self):
        return self._get_text(self._login_failure_message)

