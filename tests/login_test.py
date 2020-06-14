import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from pages.home_page import HomePage
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://the-internet.herokuapp.com")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_logout(self):
        home_pg = HomePage(self.driver)
        login_pg = LoginPage(self.driver)
        secure_pg = SecurePage(self.driver)

        home_pg.go_to_login_page()
        login_pg.with_("tomsmith", "SuperSecretPassword!")
        assert secure_pg.success_login_message_present()

        #secure_pg.success_login_message_print()

        secure_pg.logout_()
        assert login_pg.logout_success_message_present()
        self.driver.get("http://the-internet.herokuapp.com")
        print("I'm at home page")
        home_pg.go_to_dynamic_loading_page()
        print("I'm at dynamic page")


