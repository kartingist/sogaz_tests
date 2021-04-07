from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

def anketa(browser):
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

# номер телефона
    phone = browser.find_element_by_id('phone')
    #        browser.execute_script("arguments[0].click;", input_dr_step2)
    browser.execute_script("arguments[0].value = '9990403660';", phone)

# ввод почты
    email = browser.find_element_by_tag_name('#email')
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
    pass_who_give.send_keys('Кем-то выдан')
    # _____________________________________________________________________________________________

# поиск поля город, открытие поля ввода

    inp_address = browser.find_element_by_xpath('//*[@id="podpisant__container"]/div[7]/div[1]')
    time.sleep(1)
    browser.execute_script("arguments[0].scrollIntoView();", inp_address)
    time.sleep(1)
    city = browser.find_element_by_xpath('//*[@id="select2-city1-container"]')
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



