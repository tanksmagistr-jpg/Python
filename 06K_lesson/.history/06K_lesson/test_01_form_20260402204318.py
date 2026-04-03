import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    service = Service(r'C:\Users\machu\Desktop\SkyPro\Python\drivers\msedgedriver.exe')  # ваш путь
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    # Функция для поиска элемента с возможными вариантами id
    def find_field(possible_ids):
        for field_id in possible_ids:
            elements = driver.find_elements(By.ID, field_id)
            if elements:
                return elements[0]
        raise AssertionError(f"Не найдено поле среди вариантов: {possible_ids}")

    # Заполняем поля с учётом возможных id
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    # Альтернативные id на случай, если оригинальные не работают
    alternative_ids = {
        "first-name": ["first-name", "firstName", "first_name"],
        "last-name": ["last-name", "lastName", "last_name"],
        "address": ["address", "street"],
        "e-mail": ["e-mail", "email", "mail"],
        "phone": ["phone", "phone-number", "mobile"],
        "zip-code": ["zip-code", "zip", "postal-code"],
        "city": ["city", "town"],
        "country": ["country"],
        "job-position": ["job-position", "job", "position"],
        "company": ["company", "employer"]
    }

    for field_key, value in fields.items():
        locator = alternative_ids.get(field_key, [field_key])
        element = None
        for loc in locator:
            try:
                element = wait.until(EC.presence_of_element_located((By.ID, loc)))
                break
            except:
                continue
        if element is None:
            # Если по id не нашли, пробуем по name
            for loc in locator:
                try:
                    element = wait.until(EC.presence_of_element_located((By.NAME, loc)))
                    break
                except:
                    continue
        assert element, f"Не удалось найти поле {field_key}"
        element.clear()
        if value:
            element.send_keys(value)

    # Кнопка Submit
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    zip_element = driver.find_element(By.ID, "zip-code")  # тут может быть другой id
    assert "alert-danger" in zip_element.get_attribute("class") or "is-invalid" in zip_element.get_attribute("class"), "Zip code не подсвечен красным"

    green_fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        class_attr = field.get_attribute("class")
        assert "alert-success" in class_attr or "is-valid" in class_attr, f"Поле {field_id} не подсвечено зелёным"