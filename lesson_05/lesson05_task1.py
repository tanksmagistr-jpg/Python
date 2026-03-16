import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")
    print("Страница загружена")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    print("Кнопка найдена")

    button.click()
    print("Клик выполнен")

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    print(f"Текст алерта: {alert.text}")
    alert.accept()
    print("Алерт закрыт")

    time.sleep(1)

finally:
    driver.quit()
    print("Браузер закрыт")
