from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys


def anketa(browser):
    # фамилия
    surname0 = browser.find_element_by_id('?)surname0')
    surname0.send_keys('Сафончик')
# имя
    firstname0 = browser.find_element_by_tag_name('#firstname0')
    firstname0.send_keys('Евгений')
# отчество
    lastname0 = browser.find_element_by_tag_name('#lastname0')
    lastname0.send_keys('Дмитриевич')

# дата рождения страхователя
    input_dr_step2=browser.find_element_by_id('birthday0')
    input_dr_step2.send_keys('03081994')
    input_dr_step2.send_keys(Keys.ENTER)


# номер телефона
    time.sleep(0.4)
    browser.find_element_by_id('phone0').click()
    phone0 = browser.find_element_by_id('phone0')
    browser.execute_script("arguments[0].scrollIntoView();", phone0)

    WebDriverWait(browser, 40).until(EC.text_to_be_present_in_element_value((By.ID, 'phone0'),'+7'))
    phone0.send_keys('9990403660')

# ввод почты
    email = browser.find_element_by_tag_name('#email')
    browser.execute_script("arguments[0].scrollIntoView(true);", email)
    email.send_keys('heatcliff.qa@gmail.com')

# серия и номер паспорта
    pass0 = browser.find_element_by_tag_name('#pass0')
    browser.execute_script("arguments[0].scrollIntoView(true);", pass0)
    pass0.send_keys('6420001900')

# дата выдачи паспорта
    date_start0 = browser.find_element_by_id('date_start0')
    browser.execute_script("arguments[0].scrollIntoView();", date_start0)
    date_start0.send_keys('04092019')
    browser.find_element_by_id('division0').click()

# код подразделения
    division0 = browser.find_element_by_id('division0')
    browser.execute_script("arguments[0].scrollIntoView();", division0)
    division0.send_keys('650002')

# кем выдан
    pass_who_give0 = browser.find_element_by_id('pass_who_give0')
    browser.execute_script("arguments[0].scrollIntoView();", pass_who_give0)
    pass_who_give0.send_keys('Кем-то выдан')

# поиск поля город, открытие поля ввода
    city=browser.find_element_by_xpath('//*[@id="select2-city0-container"]')
    browser.execute_script("arguments[0].scrollIntoView();", city)
    time.sleep(1)
    city.click()

# вводим название и подтверждаем первый выпавший результат
    input_city=browser.find_element_by_xpath('/html/body/span/span/span[1]/input')
    input_city.send_keys('Мос')
    time.sleep(0.3)
    input_city.send_keys(Keys.ENTER)
    #city=WebDriverWait(browser, 40).until(EC.((By.XPATH, '//*[@id="select2-city0-results"]/li[1]')))
    #city.click()

# улица
    street0=browser.find_element_by_id('street0')
    street0.send_keys('Арсеньева')

# дом
    house0=browser.find_element_by_id('house0')
    house0.send_keys('33')
    

