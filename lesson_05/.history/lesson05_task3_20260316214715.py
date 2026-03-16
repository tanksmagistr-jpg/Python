import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

try:

    driver.get("http://the-internet.herokuapp.com/inputs")
    print("Страница загружена: the-internet.herokuapp.com/inputs")

    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number']"))
    )
    print("Поле ввода найдено")

    input_field.send_keys("12345")
    print("Введено: 12345")
    time.sleep(1)

    input_field.clear()
    print("Поле очищено")
    time.sleep(1)

    input_field.send_keys("54321")
    print("Введено: 54321")
    time.sleep(1)

finally:
    # 6. Закрыть браузер
    driver.quit()
    print("Браузер закрыт")