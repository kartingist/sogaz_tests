from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

def anketa(browser):
    # фамилия
        surname0 = browser.find_element_by_id('surname0' or 'surname0')
        surname0.clear()
        browser.execute_script("arguments[0].value = 'Сафончик';", surname0)

    # имя
        firstname0 = browser.find_element_by_tag_name('#firstname0')
        firstname0.clear()
        browser.execute_script("arguments[0].value = 'Евгений';", firstname0)

    # отчество
        lastname0 = browser.find_element_by_tag_name('#lastname0')
        lastname0.clear()
        browser.execute_script("arguments[0].value = 'Дмитриевич';", lastname0)

    # дата рождения страхователя
        birthday0 = browser.find_element_by_id('birthday0')
        browser.execute_script("arguments[0].value = '03081994';", birthday0)
        #birthday0.send_keys(Keys.ENTER)
    # номер телефона
        phone0 = browser.find_element_by_id('phone0')
        #        browser.execute_script("arguments[0].click;", input_dr_step2)
        browser.execute_script("arguments[0].value = '9990403660';", phone0)
    # ввод почты
        email = browser.find_element_by_tag_name('#email')
        email.clear()
        browser.execute_script("arguments[0].value = 'heatcliff.qa@gmail.com';", email)
    # серия и номер паспорта
        pass0 = browser.find_element_by_tag_name('#pass0')
        browser.execute_script("arguments[0].value = '6420001900';", pass0)
    # дата выдачи паспорта
        date_start0 = browser.find_element_by_id('date_start0')
        browser.execute_script("arguments[0].value = '04092019';", date_start0)
    # код подразделения
        division0 = browser.find_element_by_id('division0')
        browser.execute_script("arguments[0].value = '650002';", division0)
    # кем выдан
        pass_who_give0 = browser.find_element_by_id('pass_who_give0')
        pass_who_give0.clear()
        browser.execute_script("arguments[0].value = 'Кем-то выдан';", pass_who_give0)
# _____________________________________________________________________________________________
    # блок заполнения адреса, поиск поля город, открытие поля ввода
        inp_address0=browser.find_element_by_id('inp_address0')
        time.sleep(1)
        browser.execute_script("arguments[0].scrollIntoView();", inp_address0)
        time.sleep(1)

        city = browser.find_element_by_xpath('//*[@id="select2-city0-container"]')
        city.click()
    # вводим название и подтверждаем первый выпавший результат
        input_city = browser.find_element_by_xpath('/html/body/span/span/span[1]/input')
#        browser.execute_script("arguments[0].value = 'Мос';", input_city)
        input_city.send_keys('Мос')
        time.sleep(0.5)
        input_city.send_keys(Keys.ENTER)
        #WebDriverWait(browser, 40).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-city0-results"]')))
        #print(len('//*[@id="select2-city0-results"]/'))
# _____________________________________________________________________________________________
 #       input_city.send_keys(Keys.ENTER)
    # улица
        street0 = browser.find_element_by_id('street0')
        street0.send_keys('Арсеньева')
    # дом
        house0 = browser.find_element_by_id('house0')
        house0.send_keys('33')
    # город рождения
        birth_place0 = browser.find_element_by_id('birth_place0')
        birth_place0.send_keys('Уссурийск')


