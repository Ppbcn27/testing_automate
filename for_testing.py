from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# go to website
driver.get("https://www.bewellstyle.com/")

# waiting for searching tab
wait = WebDriverWait(driver, 10)
search_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="s"]')))

# scroll to search bar (if it's not to view)
driver.execute_script("arguments[0].scrollIntoView();", search_input)

# input product name in search bar
search_input.clear()
search_input.send_keys("Car Seat Back Cushion")

# click at search tab
search_button = driver.find_element(By.XPATH, '//*[@id="searchsubmit"]')
search_button.click()

# waiting for the searching product
wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Car Seat Back Cushion")))

# scroll down to see the result of the product
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # เลื่อนลงไปด้านล่างสุด
time.sleep(1)  # รอให้หน้าเว็บโหลด

# click at the product
product_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Car Seat Back Cushion")
product_link.click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "single_add_to_cart_button")))

# click at add to cart button
add_to_cart_button = driver.find_element(By.CLASS_NAME, "single_add_to_cart_button")
add_to_cart_button.click()

time.sleep(3)

driver.refresh()

time.sleep(5)

# driver.quit()