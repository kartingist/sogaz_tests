from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def pay(browser):
    # ввод данных карты
#    time.sleep(4)


    browser.execute_script("arguments[0].value = '9000000000000000001';", browser.find_element_by_id('pan'))
#    browser.find_element_by_id('pan').send_keys('9000000000123456789', Keys.TAB)

    time.sleep(0.2)
    month=browser.find_element_by_id('month').send_keys('12', Keys.ENTER)
    #browser.execute_script("arguments[0].value = '12';", month)
    #month.send_keys(Keys.TAB)

    year=browser.find_element_by_id('year').send_keys('24', Keys.TAB)
    #browser.execute_script("arguments[0].value = '24';", year)
    #year.send_keys(Keys.TAB)

    cvc=browser.find_element_by_id('cvc').send_keys('123', Keys.TAB)
    #browser.execute_script("arguments[0].value = '123';", cvc)
 #   time.sleep(5)
    pay = browser.find_element_by_tag_name('#payment-form > div.btn-group > button.btn.btn-primary')
    browser.execute_script("arguments[0].click();", pay)

    success = WebDriverWait(browser, 80).until(
        EC.visibility_of_element_located((By.TAG_NAME, "body > div.container > div.payment-info > h2")))
    assert 'Операция выполнена успешно' == success.text, 'оплата не прошла'




