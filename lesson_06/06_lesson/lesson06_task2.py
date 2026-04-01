from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.ID, "newButtonName")
input_field.clear()
input_field.send_keys("SkyPro")

button = driver.find_element(By.ID, "updatingButton")
button.click()


WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

button_text = driver.find_element(By.ID, "updatingButton").text
print(button_text)

driver.quit()