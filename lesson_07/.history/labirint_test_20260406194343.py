from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_card_counter():
    browser = webdriver.Chrome()
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    
    # Если куки не нужны, закомментируйте следующую строку
    # cookie = {"name": "some_name", "value": "some_value"}
    # browser.add_cookie(cookie)
    
    sleep(5)
    
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
    
    browser.quit()

  