from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 20)

wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3)

images = driver.find_elements(By.TAG_NAME, "img")

src = images[2].get_attribute("src")
print(src)

driver.quit()
