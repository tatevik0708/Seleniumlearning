from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SecurePage(BasePage):
    _secure_area_header_title = {"by": By.CLASS_NAME, "value": "icon-lock"}
    _welcome_text = {"by": By.CLASS_NAME, "value": "subheader"}
    _logout_button = {"by": By.CLASS_NAME, "value": "icon-2x icon-signout"}
    _logout_success_message = {"by": By.ID, "value": "flash"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("http://the-internet.herokuapp.com/secure")
        assert self._is_displayed(self._logout_button)

    def logout_(self):
        self._click(self._logout_button)

    def logout_success_message_present(self):
        return self._is_displayed(self._logout_success_message)

