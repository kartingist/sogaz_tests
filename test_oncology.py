import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from link import link
from pay import pay
from anketa import anketa
from step_3 import step_3
from close_popaps import close_popaps
product_link = 'accident/oncology/'
final_link = link + product_link




class TestOncology():
    def test_open_site(self, browser):
        browser.get(final_link)
        # Закрываем попапы
        close_popaps(browser)

    def test_step_1(self, browser):
        travel_data=browser.find_element_by_xpath(f'// *[ @ id = "travel_data"] / div / div[5]')
        travel_data.click()
        step_btn_1=browser.find_element_by_id('step_btn_1')
        browser.execute_script("arguments[0].click();", step_btn_1)

    def test_anketa(self, browser):
        anketa(browser)

        # чекбокс Совпадает с адресом регистрации
    #    browser.find_element_by_css_selector('#live_place_block_0 > div.form-check.abc-checkbox > label').click()

        # чекбокс Застрахованным лицом является Страхователь
        coincides=browser.find_element_by_xpath(
            '//*[@id="form-desigion"]/div[2]/label')
        # чекбокс Застрахованным лицом является Страхователь
        # coincides=browser.find_element_by_id('coincides').click()
        browser.execute_script("arguments[0].click();", coincides)

        step_btn_2=browser.find_element_by_id('step_btn_2')
        browser.execute_script("arguments[0].click();", step_btn_2)


    def test_step_3(self, browser):
        step_3(browser)

    if link != "http://shop.sogaz.loc/" and link != 'http://sogazrelease.support.zetest.site/':
        def test_pay(self, browser):
            pay_step = browser.find_element_by_id('step_btn_3')
            browser.execute_script("arguments[0].click();", pay_step)

            WebDriverWait(browser, 80).until(EC.visibility_of_element_located((By.ID, "pan")))
            pay(browser)

