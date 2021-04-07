def close_popaps(browser):# Закрываем попапы
    browser.find_element_by_tag_name(
        'body > div.cookiewrap > div.alert.cookiealert2.d-flex.justify-content-center.show > button').click()

    browser.find_element_by_tag_name('body > div.cookiewrap > div.alert.cookiealert.show > div > button').click()