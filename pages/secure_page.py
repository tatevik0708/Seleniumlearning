from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SecurePage(BasePage):
    _secure_area_header_title = {"by": By.CLASS_NAME, "value": "icon-lock"}
    _welcome_text = {"by": By.CLASS_NAME, "value": "subheader"}
    _success_login_message = {"by": By.XPATH, "value": "//div[@id='flash']"}
    _logout_button = {"by": By.XPATH, "value": "//div[@id='content']//div//a//i"}



    def __init__(self, driver):
        self.driver = driver
        #assert self._is_displayed(self._logout_button)
        print("Secure Page POM created")

    def logout_(self):
        self._click(self._logout_button)
        print("Logged out")

    def success_login_message_present(self):
        return self._is_displayed(self._success_login_message)

    def success_login_message_print(self):
        return self._get_text(self._success_login_message)



