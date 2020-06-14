from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    ex1_hidden_element_link = {"by": By.XPATH, "value": "//div[@id='content']//a[1]"}
    ex2_after_fact_rendered_element_link = {"by": By.XPATH, "value": "//body//a[2]"}
    start_button_hidden_element = {"by": By.XPATH, "value": "//div[@id='start']//button"}
    start_button_after_fact_rendered_element = {"by": By.XPATH, "value": "//div[@id='start']//button"}

    def __init__(self, driver):
        self.driver = driver

    def ex1_click(self):
        self.click(self.examlpe1)

    def examlpe2_click(self):
        self.click(self.examlpe2)