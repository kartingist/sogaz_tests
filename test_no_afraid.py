from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from link import link
from pay import pay
from step_3 import step_3
from anketa0 import anketa
from close_popaps import close_popaps
product_link = 'accident/no_afraid_change/'
final_link = link + product_link




class TestNoAfraid():
    def test_open_site(self, browser):
        browser.get(final_link)
        # Закрываем попапы
        close_popaps(browser)

    def test_step_1(self, browser):
#        нажимаем купить на 1 шаге
        step_btn_one=browser.find_element_by_id('step_btn_one')
        browser.execute_script("arguments[0].click();", step_btn_one)
    def test_anketa(self, browser):
        anketa(browser)
        next_step = browser.find_element_by_tag_name('#step_btn_2 > a')
        browser.execute_script("arguments[0].click();", next_step)
    def test_step_3(self, browser):
        step_3(browser)

    if link != "http://shop.sogaz.loc/" and link != 'http://sogazrelease.support.zetest.site/':
        def test_pay(self, browser):
            pay_step = browser.find_element_by_id('step_btn_3')
            browser.execute_script("arguments[0].click();", pay_step)

            WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "pan")))
            pay(browser)






