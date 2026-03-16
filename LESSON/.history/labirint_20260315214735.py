from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import. ChromeDriverManager
from selenium.webdriver.common

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.labirint.ru/")

search_locator = 'search-field'

driver.find_element(By.CLASS_NAME, "tomatoes")