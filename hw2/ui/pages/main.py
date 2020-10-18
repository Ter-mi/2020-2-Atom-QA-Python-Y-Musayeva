import time
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from ui.locators import MainLocators
from .base import BasePage, CannotFindElement


class MainPage(BasePage):

    locators = MainLocators()

    def search_campaign(self, name):
        self.driver.get("https://target.my.com/dashboard")
        search = self.find(self.locators.SEARCH_CAMPAIGN)
        # Have to wait while searching to get a result
        search.send_keys(name)
        XPath = '//span[text()="'+name+'"]'
        RESULT_SEARCH_COMPANY = (By.XPATH, XPath)
        self.click(RESULT_SEARCH_COMPANY)
        

    def create_campaign(self, link, name, picture):
    
        self.click(self.locators.HEADER_BUTTON_CREATE_CAMPAIGN)
        self.click(self.locators.TRAFFIC_TYPE)
        self.completion(link, self.locators.LINK_FIELD)
        time.sleep(1)
        self.completion(name, self.locators.NAME_FIELD)
        self.click(self.locators.BANNER)
        download_elem = self.find(self.locators.UPLOAD_ELEMENT)
        download_elem.send_keys(picture)
        self.click(self.locators.SAVE_PIC)
        time.sleep(2)
        self.click(self.locators.BUTTON_ADD_ADS)
        time.sleep(1)
        self.click(self.locators.BUTTON_CREATE_CAMPAIGN)


    def check_company(self, name):
        time.sleep(2)
        elem = self.find(self.locators.SEARCH_CAMPAIGN)
        elem.send_keys(name)
        XPath = '//span[text()="'+name+'"]'
        RESULT_SEARCH_COMPANY = (By.XPATH, XPath)
        try:
            self.click(RESULT_SEARCH_COMPANY)
            Xpath2 = '//div/span[text()="1"]'
            RESULT2_SEARCH_COMPANY = (By.XPATH, Xpath2)
            return self.find(RESULT2_SEARCH_COMPANY).is_displayed()
        except TimeoutException:
            return False

    def check_segment(self, name):
        self.driver.get("https://target.my.com/segments/segments_list")
        search = self.find(self.locators.SEARCH_SEGMENT,timeout=5)
        search.send_keys(name)
        try:
            # Have to wait while searching to get a result
            self.wait().until(EC.visibility_of_element_located(self.locators.SEARCH_SUGGESTION))
            XPath = '//li[text()="'+name+'"]'
            RESULT_SEARCH_SEGMENT = (By.XPATH, XPath)
            self.click(RESULT_SEARCH_SEGMENT)
            XPath2 = '//a[@title="'+name+'"]'
            LIST_SEGMENT = (By.XPATH, XPath2)
            return self.find(LIST_SEGMENT).is_displayed()
        except TimeoutException:
            return False
        

    def create_segment(self, name):
        self.click(self.locators.BUTTON_SEGMENTS)
        self.driver.get("https://target.my.com/segments/segments_list")
        try:
            self.click(self.locators.BUTTON_CREATE_SEGMENT)
        except CannotFindElement:
            self.click(self.locators.LINK_FIRST_SEGMENT)
        
        self.click(self.locators.OPTION_SEGMENT)
        self.click(self.locators.FIRST_CHECKBOX)
        self.click(self.locators.BUTTON_LIST)
        self.click(self.locators.SECOND_CHECKBOX)
        self.click(self.locators.BUTTON_ADD_SEGMENT)
        self.completion(name, self.locators.SEGMENT_NAME_FIELD)
        self.click(self.locators.BUTTON_CONFIRM_SEGMENT)

    def delete_segment(self, name):
        if self.check_segment(name):
            search = self.find(self.locators.SEARCH_SEGMENT,timeout=5)
            search.send_keys(name)
            # Have to wait while searching to get a result
            self.wait().until(EC.visibility_of_element_located(self.locators.SEARCH_SUGGESTION))
            XPath = '//li[text()="'+name+'"]'
            RESULT_SEARCH_SEGMENT = (By.XPATH, XPath)
            self.click(self.locators.DELETE_BUTTON)
            self.click(self.locators.CONFIRM_DELETE)
