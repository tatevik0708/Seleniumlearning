from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DynamicLoadingPageEx1(BasePage):
    start_button_hidden_element = {"by": By.XPATH, "value": "//div[@id='start']//button"}
    text_after_pressing_start = {"by": By.XPATH, "value": "//div[@id='finish']//h4"}

    def __init__(self, driver):
        self.driver = driver

    def press_start(self):
        self._click(self.start_button_hidden_element)

