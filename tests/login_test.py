import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from pages import login_page



class TestLogin:
    @pytest.fixture
    def login(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')
        if os.path.isfile(_chromedriver):
            _service = ChromeService(executable_path=_chromedriver)
            driver_ = webdriver.Chrome(service=_service)
        else:
            driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return login_page.LoginPage(driver_)


    def test_valid_credentials(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        assert (login._success_message_present())
