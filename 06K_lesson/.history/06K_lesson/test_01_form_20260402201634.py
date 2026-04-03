import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Для Edge (можно заменить на Safari, но нужен драйвер)
@pytest.fixture
def driver():
    # Используем Edge (или Safari, если настроен)
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    # Заполняем поля
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",   # оставляем пустым
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_id, value in fields.items():
        input_element = driver.find_element(By.ID, field_id)
        input_element.clear()
        if value:
            input_element.send_keys(value)

    # Нажимаем Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверяем подсветку Zip code (красный)
    zip_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_field.get_attribute("class"), "Zip code не подсвечен красным"

    # Список полей, которые должны быть зелёными
    green_fields = ["first-name", "last-name", "address", "e-mail",
                    "phone", "city", "country", "job-position", "company"]

    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        # Ищем класс успеха (alert-success) или подобный
        assert "alert-success" in field.get_attribute("class"), f"Поле {field_id} не подсвечено зелёным"