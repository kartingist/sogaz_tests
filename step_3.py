import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def step_3(browser):
    # получение и ввод кода подтверждения
        get_code=browser.find_element_by_tag_name('#get_code')
#        browser.execute_script("arguments[0].scrollIntoView(true);", get_code)
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
    # Активируем
        for i in range(1, x+1):
            browser.execute_script(f"document.getElementById('check{i}').click()")


