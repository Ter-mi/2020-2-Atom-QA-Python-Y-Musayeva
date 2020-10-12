from time import sleep
import pytest
import time
from selenium.webdriver.common.keys import Keys
from tests.base_ui import BaseCase


@pytest.mark.UI
class TestUi(BaseCase):
    def test_auth(self, get_main_page):
        self.page = get_main_page
        assert self.page.find(self.page.locators.USER_NAME) is not None

    def test_auth_fail(self, get_auth_page):
        self.page = get_auth_page
        self.page.login('yasamin.tm@gmail.com', 'passwordqw')
        sleep(2)
        assert "Invalid login or password" in self.driver.page_source
            
    def test_create_campaign(self, get_main_page, test_name, upload_file):
        self.page = get_main_page
        self.page.create_campaign('app.com', test_name, upload_file)
        sleep(2)
        assert self.page.check_company(test_name)

    def test_create_segment(self, get_main_page, test_name):
        self.page = get_main_page
        self.page.create_segment(test_name)
        assert self.page.check_segment(test_name)

    def test_delete_segment(self, get_main_page, test_name):
        result = False
        self.page = get_main_page
        self.page.create_segment(test_name)
        self.page.delete_segment(test_name)
        self.driver.refresh()
        with pytest.raises(AssertionError):
            assert self.page.check_segment(test_name)
