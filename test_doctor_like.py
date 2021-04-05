import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from link import link
from pay import pay
product_link = 'accident/doctor_like/'
final_link = link + product_link



class TestDrLike():
    def test_open_site(self, browser):

        browser.get(final_link)


        #browser.fullscreen_window()

        # Закрываем попапы
        popap1 = browser.find_element_by_tag_name(
            'body > div.cookiewrap > div.alert.cookiealert2.d-flex.justify-content-center.show > button').click()

        popap2 = browser.find_element_by_tag_name('body > div.cookiewrap > div.alert.cookiealert.show > div > button').click()

    # первый шаг

    # первый шаг
    def test_step1(self, browser):

        # Дата рождения Застрахованного
        input_dr_step1=browser.find_element_by_id('birthday')
        browser.execute_script("arguments[0].value = '03081994';", input_dr_step1)



        # выбор региона
        select_region=browser.find_element_by_tag_name('#form-step1 > div.sub-step.current > div:nth-child(3) > div:nth-child(1) > label')
        browser.execute_script("arguments[0].click();", select_region)

        # выбор франшизы
        select_franshize=browser.find_element_by_tag_name('#form-step1 > div.sub-step.current > div:nth-child(5) > div:nth-child(2) > label')
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

    def test_anketa(self, browser):
        # фамилия
        surname0 = browser.find_element_by_id('surname0' or 'surname0')
        browser.execute_script("arguments[0].value = 'Сафончик';", surname0)

        # имя
        firstname0 = browser.find_element_by_tag_name('#firstname0')
        browser.execute_script("arguments[0].value = 'Евгений';", firstname0)

        # отчество
        lastname0 = browser.find_element_by_tag_name('#lastname0')
        browser.execute_script("arguments[0].value = 'Дмитриевич';", lastname0)

        # дата рождения страхователя
        birthday0 = browser.find_element_by_id('birthday0')
        browser.execute_script("arguments[0].value = '03081994';", birthday0)
        #        input_dr_step2.send_keys('03081994')
        #        input_dr_step2.send_keys(Keys.ENTER)

        # номер телефона

        #        browser.find_element_by_id('phone').click()

        phone0 = browser.find_element_by_id('phone0')
        #        browser.execute_script("arguments[0].click;", input_dr_step2)
        browser.execute_script("arguments[0].value = '9990403660';", phone0)
        #        browser.execute_script("arguments[0].scrollIntoView();", phone)

        #        WebDriverWait(browser, 40).until(EC.text_to_be_present_in_element_value((By.ID, 'phone'), '+7'))
        #        phone.send_keys('9990403660')

        # ввод почты
        email = browser.find_element_by_tag_name('#email')
        browser.execute_script("arguments[0].scrollIntoView(true);", email)
        email.send_keys('heatcliff.qa@gmail.com')

        # серия и номер паспорта
        pass0 = browser.find_element_by_tag_name('#pass0')
        browser.execute_script("arguments[0].value = '6420001900';", pass0)
        #        pass0.send_keys('6420001900')

        # дата выдачи паспорта
        date_start0 = browser.find_element_by_id('date_start0')
        browser.execute_script("arguments[0].value = '04092019';", date_start0)
        #        date_start.send_keys('04092019')
        #        browser.find_element_by_id('division').click()

        # код подразделения
        division0 = browser.find_element_by_id('division0')
        browser.execute_script("arguments[0].value = '650002';", division0)
        #        division.send_keys('650002')

        # кем выдан
        pass_who_give0 = browser.find_element_by_id('pass_who_give0')
        browser.execute_script("arguments[0].scrollIntoView();", pass_who_give0)
        pass_who_give0.send_keys('Кем-то выдан')
        # _____________________________________________________________________________________________
        time.sleep(0.5)
        # поиск поля город, открытие поля ввода
        city = browser.find_element_by_xpath('//*[@id="select2-city0-container"]')
        # browser.execute_script("arguments[0].value = 'Московская обл., г. Балашиха, мкр. Железнодорожный';", city)
        browser.execute_script("arguments[0].scrollIntoView();", city)
        time.sleep(1)
        city.click()

        # вводим название и подтверждаем первый выпавший результат
        input_city = browser.find_element_by_xpath('/html/body/span/span/span[1]/input')
#        browser.execute_script("arguments[0].value = 'Мос';", input_city)
        input_city.send_keys('Мос')
        time.sleep(0.5)
        input_city.send_keys(Keys.ENTER)
        # city=WebDriverWait(browser, 40).until(EC.((By.XPATH, '//*[@id="select2-city0-results"]/li[1]')))
        # city.click()

        # улица
        street0 = browser.find_element_by_id('street0')
        street0.send_keys('Арсеньева')

        # дом
        house0 = browser.find_element_by_id('house0')
        house0.send_keys('33')

        # город рождения
        birth_place0 = browser.find_element_by_id('birth_place0')
        birth_place0.send_keys('Уссурийск')

    # чекбокс Совпадает с адресом регистрации
        adr_reg=browser.find_element_by_css_selector('#live_place_block_0 > div.form-check.abc-checkbox > label')
        browser.execute_script("arguments[0].click();", adr_reg)

    # чекбокс Застрахованным лицом является Страхователь
        strahovatel=browser.find_element_by_css_selector('#form-createpolis > div:nth-child(4) > div.form-check.abc-checkbox > label')
        browser.execute_script("arguments[0].click();", strahovatel)
    # переход к следующему шагу
        next_step=browser.find_element_by_tag_name('#step_btn_2 > a')
        browser.execute_script("arguments[0].click();", next_step)

    #    time.sleep(4)

    # получение и ввод кода подтверждения
        get_code=browser.find_element_by_tag_name('#get_code')
        browser.execute_script("arguments[0].scrollIntoView(true);", get_code)
        get_code=WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.ID, "get_code")))
        browser.execute_script("arguments[0].click();", get_code)
        code=WebDriverWait(browser, 40).until(EC.visibility_of_element_located((By.TAG_NAME, "#hideOnLock > div > div:nth-child(3) > div > div > div:nth-child(3)")))
        codeConfirm = browser.find_element_by_id('codeConfirm')
        codeConfirm.send_keys(code.text)
        browser.execute_script("arguments[0].click();", browser.find_element_by_id('codeConfirmNext'))
        time.sleep(0.15)
    # активация всех чекбоксов
        # получаем количество чек-боксов
        x=len(browser.find_elements_by_xpath('//*[@id="step3_inner-confirm"]/div[2]/div/div/div'))
        for i in range(1, x+1):
            browser.execute_script(f"document.getElementById('check{i}').click()")



        if link != "http://shop.sogaz.loc/" and link !='http://sogazrelease.support.zetest.site/':
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



