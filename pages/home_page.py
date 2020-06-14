from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    _login_page_url = {"by": By.XPATH, "value": "//li[21]//a[1]" }
    _dynamic_loading_page_url = {"by": By.XPATH, "value": "//li[14]//a[1]"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("http://the-internet.herokuapp.com/")
        print("Home page POM created")

    def go_to_login_page(self):
        self._click(self._login_page_url)

    def go_to_dynamic_loading_page(self):
        self._click(self._dynamic_loading_page_url)



