from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common. import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.labirint.ru/")

search_locator = '#search-field'

serch_input = driver.find_element(By.CSS_SELECTOR, search_locator)

serch_input.send_keys('Python')
serch_input.
sleep(15)