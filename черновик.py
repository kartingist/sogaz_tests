import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from link import link





class TestOncology():
    def qwer(self, browser):
        product_link = 'accident/oncology/'
        final_link = link + product_link
        browser.get(final_link)
    def test_open_site(self, browser):
        self.qwer(browser)