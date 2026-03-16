from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.labirint.ru/")

search_locator = '#search-field'

serch_input = driver.find_element(By.CSS_SELECTOR, search_locator)

serch_input.send_keys('Python', Keys.RETURN)

book_locator = 'div.product-card'

books = driver.find_elements(By.CSS_SELECTOR, 'div.product-card')
print(len(books))

for book in books:
    title = book.find_element(By.CSS_SELECTOR,'a.product-card__name').text
    author = ''
    price = book.find_element(By.CSS_SELECTOR,'a.product-card__name').text
    try:
        author = book.find_element(By.CSS_SELECTOR,'div.product-card__author').text
    except:
        author = 'Автор не указан'

#div.product-card__price-current
a.product-card__name
    print(author)
sleep(15)

