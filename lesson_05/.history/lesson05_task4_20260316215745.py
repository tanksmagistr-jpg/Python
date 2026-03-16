import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

try:

    url = "http://the-internet.herokuapp.com/login"
    driver.get(url)
    print(f"Страница загружена: {url}")

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("tomsmith")
    print("Введено имя пользователя: tomsmith")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("Введён пароль: SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("Кнопка Login нажата")

    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    )
    message_text = success_message.text
    print(f"Сообщение с зелёной плашки: {message_text}")

    # Небольшая пауза для наглядности (необязательно)
    time.sleep(1)

finally:
    # 6. Закрыть браузер
    driver.quit()
    print("Браузер закрыт")