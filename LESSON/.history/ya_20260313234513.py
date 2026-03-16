from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

sleep(5)

driver

driver.get("https://ya.ru")


#driver.back()
#driver.forward()
#driver.refresh()

#driver.set_window_size(640, 480)

sleep(15)
