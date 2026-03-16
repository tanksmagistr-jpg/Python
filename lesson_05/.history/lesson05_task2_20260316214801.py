import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    url = "http://uitestingplayground.com/dynamicid"
    driver.get(url)
    print(f"Страница загружена: {url}")

    time.sleep(1)  # небольшая пауза для надёжности

    button_selector = "button.btn-primary"
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
    )
    print("Кнопка найдена по CSS-классу (ID проигнорирован).")

    button.click()
    print("Клик выполнен.")

    time.sleep(1)
    print("Скрипт успешно завершён.\n")

finally:
    driver.quit()
    print("Браузер закрыт.")
