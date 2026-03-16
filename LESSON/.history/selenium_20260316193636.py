from selenium import webdriver

# Пример для Google Chrome
driver = webdriver.Chrome()
driver.get("http://www.google.com")
print(driver.title)
driver.quit()

from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get("https://www.example.com")

    print(f'Заголовок страницы: {driver.title}')

      driver.quit()