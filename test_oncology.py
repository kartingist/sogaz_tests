import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from link import link
from pay import pay
product_link = 'accident/oncology/'
final_link = link + product_link




class TestOncology():
    def test_open_site(self, browser):

        browser.get(final_link)


        #browser.fullscreen_window()

        # Закрываем попапы
        popap1 = browser.find_element_by_tag_name(
            'body > div.cookiewrap > div.alert.cookiealert2.d-flex.justify-content-center.show > button').click()

        popap2 = browser.find_element_by_tag_name('body > div.cookiewrap > div.alert.cookiealert.show > div > button').click()


    def test_oncology(self, browser ):
        travel_data=browser.find_element_by_xpath('// *[ @ id = "travel_data"] / div / div[5]')
        travel_data.click()
        step_btn_1=browser.find_element_by_id('step_btn_1')
        browser.execute_script("arguments[0].click();", step_btn_1)

        # фамилия
        surname = browser.find_element_by_id('surname')
        browser.execute_script("arguments[0].value = 'Сафончик';", surname)

        # имя
        firstname = browser.find_element_by_tag_name('#firstname')
        browser.execute_script("arguments[0].value = 'Евгений';", firstname)

        # отчество
        lastname = browser.find_element_by_tag_name('#lastname')
        browser.execute_script("arguments[0].value = 'Дмитриевич';", lastname)


        # дата рождения страхователя
        input_dr_step2 = browser.find_element_by_id('birthday')
        browser.execute_script("arguments[0].value = '03081994';", input_dr_step2)
#        input_dr_step2.send_keys('03081994')
#        input_dr_step2.send_keys(Keys.ENTER)

        # номер телефона

#        browser.find_element_by_id('phone').click()

        phone = browser.find_element_by_id('phone')
#        browser.execute_script("arguments[0].click;", input_dr_step2)
        browser.execute_script("arguments[0].value = '9990403660';", phone)
#        browser.execute_script("arguments[0].scrollIntoView();", phone)

#        WebDriverWait(browser, 40).until(EC.text_to_be_present_in_element_value((By.ID, 'phone'), '+7'))
#        phone.send_keys('9990403660')

        # ввод почты
        email = browser.find_element_by_tag_name('#email')
        browser.execute_script("arguments[0].scrollIntoView(true);", email)
        email.send_keys('heatcliff.qa@gmail.com')

        # серия и номер паспорта
        pass0 = browser.find_element_by_tag_name('#pass')
        browser.execute_script("arguments[0].value = '6420001900';", pass0)
#        pass0.send_keys('6420001900')

        # дата выдачи паспорта
        date_start = browser.find_element_by_id('date_start')
        browser.execute_script("arguments[0].value = '04092019';", date_start)
#        date_start.send_keys('04092019')
#        browser.find_element_by_id('division').click()

        # код подразделения
        division = browser.find_element_by_id('division')
        browser.execute_script("arguments[0].value = '650002';", division)
#        division.send_keys('650002')

        # кем выдан
        pass_who_give = browser.find_element_by_id('pass_who_give')
        browser.execute_script("arguments[0].scrollIntoView();", pass_who_give)
        pass_who_give.send_keys('Кем-то выдан')
    #_____________________________________________________________________________________________

        # поиск поля город, открытие поля ввода
        city = browser.find_element_by_xpath('//*[@id="select2-city1-container"]')
        browser.execute_script("arguments[0].scrollIntoView();", city)
        time.sleep(1)
        city.click()

        # вводим название и подтверждаем первый выпавший результат
        input_city = browser.find_element_by_xpath('/html/body/span/span/span[1]/input')
        input_city.send_keys('Мос')
        time.sleep(0.5)
        input_city.send_keys(Keys.ENTER)
        # city=WebDriverWait(browser, 40).until(EC.((By.XPATH, '//*[@id="select2-city0-results"]/li[1]')))
        # city.click()

        # улица
        street = browser.find_element_by_id('street')
        street.send_keys('Арсеньева')

        # дом
        house = browser.find_element_by_id('house')
        house.send_keys('33')

        # город рождения
        birth_place = browser.find_element_by_id('birth_place')
        birth_place.send_keys('Уссурийск')

        # чекбокс Совпадает с адресом регистрации
    #    browser.find_element_by_css_selector('#live_place_block_0 > div.form-check.abc-checkbox > label').click()

        # чекбокс Застрахованным лицом является Страхователь
        browser.find_element_by_xpath(
            '//*[@id="form-desigion"]/div[2]/label').click()
        # чекбокс Застрахованным лицом является Страхователь
    #    browser.find_element_by_id('coincides').click()

        step_btn_2=browser.find_element_by_id('step_btn_2')
        browser.execute_script("arguments[0].click();", step_btn_2)

        get_code = browser.find_element_by_tag_name('#get_code')
        browser.execute_script("arguments[0].scrollIntoView(true);", get_code)
        #
        get_code = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.ID, "get_code")))

        browser.execute_script("arguments[0].click();", get_code)

        code = WebDriverWait(browser, 40).until(EC.visibility_of_element_located(
            (By.TAG_NAME, "#hideOnLock > div > div:nth-child(3) > div > div > div:nth-child(3)")))
        codeConfirm = browser.find_element_by_id('codeConfirm')
        codeConfirm.send_keys(code.text)
        #    browser.find_element_by_id('codeConfirmNext').click()
        browser.execute_script("arguments[0].click();", browser.find_element_by_id('codeConfirmNext'))

        # активация всех чекбоксов
        time.sleep(0.2)
        # получаем количество чек-боксов
        x=len(browser.find_elements_by_xpath('//*[@id="step3_inner-confirm"]/div[2]/div/div/div'))
        for i in range(1, x+1):
            browser.execute_script(f"document.getElementById('check{i}').click()")



    if link != "http://shop.sogaz.loc/" and link !='http://sogazrelease.support.zetest.site/':

        def test_pay(self, browser):
            pay_step = browser.find_element_by_tag_name('#step_btn_3 > a')
            browser.execute_script("arguments[0].click();", pay_step)
            WebDriverWait(browser, 80).until(EC.visibility_of_element_located((By.ID, "pan")))

            pay(browser)

