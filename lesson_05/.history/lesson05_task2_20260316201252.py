import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера (chromedriver должен быть в PATH или в папке со скриптом)
driver = webdriver.Chrome()

try:
    # 1. Открыть страницу с динамическим ID
    url = "http://uitestingplayground.com/dynamicid"
    driver.get(url)
    print(f"Страница загружена: {url}")

    # Небольшая пауза для полной отрисовки страницы
    time.sleep(1)

    # 2. Найти синюю кнопку по стабильному CSS-классу
    #    Селектор ищет любую кнопку с классом 'btn-primary'.
    #    Этот класс не меняется, в отличие от ID.
    button_selector = "button.btn-primary"

    # Явное ожидание: ждём, пока кнопка станет кликабельной (до 10 секунд)
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
    )
    print("Кнопка найдена по CSS-классу (ID проигнорирован).")

    # 3. Кликнуть по кнопке
    button.click()
    print("Клик выполнен.")

    # После клика появляется всплывающее окно (alert).
    # Ждём его появления и принимаем
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert_text = alert.text
    print(f"Получен alert с текстом: '{alert_text}'")
    alert.accept()
    print("Alert принят.")

    # Небольшая пауза, чтобы убедиться, что alert закрылся
    time.sleep(1)
    print("Скрипт успешно завершён.\n")

finally:
    # Закрываем браузер
    driver.quit()
    print("Браузер закрыт.")