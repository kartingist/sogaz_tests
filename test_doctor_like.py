import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from link import link
from pay import pay
from step_3 import step_3
from anketa0 import anketa
from close_popaps import close_popaps
product_link = 'accident/doctor_like/'
final_link = link + product_link

#@pytest.mark.parametrize('x', ["1", "2"], scope="class")
class TestDrLike():
    def test_open_site(self, browser):
        browser.get(final_link)
    # Закрываем попапы
        close_popaps(browser)

    # первый шаг
    def test_step_1(self, browser):
    # Дата рождения Застрахованного
        input_dr_step1=browser.find_element_by_id('birthday')
        browser.execute_script("arguments[0].value = '03081994';", input_dr_step1)
    # выбор региона
        select_region=browser.find_element_by_tag_name('#form-step1 > div.sub-step.current > div:nth-child(3) > div:nth-child(3) > label')
        browser.execute_script("arguments[0].click();", select_region)
    # выбор франшизы
        select_franshize=browser.find_element_by_tag_name(f'#form-step1 > div.sub-step.current > div:nth-child(5) > div:nth-child(1) > label')
        browser.execute_script("arguments[0].click();", select_franshize)
    # подтверждение и переход дальше
        next_step=browser.find_element_by_tag_name("#program > div:nth-child(1) > a")
        browser.execute_script("arguments[0].click();", next_step)
    # выбор варианта страхования
        select_variant_st=browser.find_element_by_tag_name('#box-programm > div:nth-child(2) > div:nth-child(2) > label')
        browser.execute_script("arguments[0].click();", select_variant_st)
    # переход ко второму шагу
        next_step = browser.find_element_by_tag_name("#step_btn_one > a")
        browser.execute_script("arguments[0].click();", next_step)
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/header/div/div/div/div[1]/div[3]/a/img')))

    def test_anketa(self, browser):
        anketa(browser)
        # чекбокс Совпадает с адресом регистрации
        adr_reg = browser.find_element_by_css_selector('#live_place_block_0 > div.form-check.abc-checkbox > label')
        browser.execute_script("arguments[0].click();", adr_reg)
        # чекбокс Застрахованным лицом является Страхователь
        strahovatel = browser.find_element_by_css_selector(
            '#form-createpolis > div:nth-child(4) > div.form-check.abc-checkbox > label')
        browser.execute_script("arguments[0].click();", strahovatel)
        # переход к следующему шагу
        next_step = browser.find_element_by_tag_name('#step_btn_2 > a')
        browser.execute_script("arguments[0].click();", next_step)

    def test_step_3(self, browser):
        step_3(browser)

        if link != "http://shop.sogaz.loc/" and link != 'http://sogazrelease.support.zetest.site/':
            # переход к шагу оплаты, сбп
            pay_step = browser.find_element_by_id('step_btn_3')
            browser.execute_script("arguments[0].click();", pay_step)

            paylink = WebDriverWait(browser, 40).until(EC.visibility_of_element_located(
                (By.ID, 'payLink')))
            browser.execute_script("arguments[0].click();", paylink)

    if link != "http://shop.sogaz.loc/" and link != 'http://sogazrelease.support.zetest.site/':
        def test_pay(self, browser):
            WebDriverWait(browser, 80).until(EC.visibility_of_element_located((By.ID, "pan")))
            pay(browser)



    # #    if link == "http://shop.sogaz.loc/" and link=='http://sogazrelease.support.zetest.site/':
    # #        WebDriverWait(browser, 40).until(EC.visibility_of_element_located(
    # #            (By.XPATH, '//*[@id="modalPayVariants"]/div/div')))
    # #        assert browser.find_element_by_tag_name(
    # #            '#onAjaxError > div > div > div.modal-body > h2').text == 'Ошибка обращения к серверу!', 'sss'
    # #        browser.quit()
    #
        # if link != "http://shop.sogaz.loc/" and link!='http://sogazrelease.support.zetest.site/':
        #     paylink=WebDriverWait(browser, 40).until(EC.visibility_of_element_located(
        #                 (By.ID, 'payLink')))
        #     browser.execute_script("arguments[0].click();", paylink)
        #
        #
        # def test_pay():
        #     pay(browser)



