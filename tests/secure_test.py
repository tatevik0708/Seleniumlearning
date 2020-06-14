import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from pages import secure_page

class TestSecure:
    @pytest.fixture
    def secure_logout(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')
        if os.path.isfile(_chromedriver):
             _service = ChromeService(executable_path=_chromedriver)
             driver_ = webdriver.Chrome(service=_service)
        else:
            driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return secure_page.SecurePage(driver_)

