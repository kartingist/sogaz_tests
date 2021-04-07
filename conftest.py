import pytest
from selenium import webdriver

@pytest.fixture(scope="class")

def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    browser.implicitly_wait(20)
    browser.set_window_size(1920, 1080)
#    browser.set_window_size(375, 1080)
    yield browser
    print("\nquit browser..")
    browser.quit()




