from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")
sleep(15)
print(f'Заголовок страницы: {driver.title}')
sleep(15)
driver.quit()

sleep(15)