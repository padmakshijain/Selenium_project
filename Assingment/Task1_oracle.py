import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.oracle.com/in/database/")

driver.find_element(By.ID, "acctBtnLabel").click()
driver.find_element(By.LINK_TEXT, "Sign-In").click()

time.sleep(5)
print(driver.title)

actual_header = driver.find_element(By.XPATH, "//h2[contains(text(),'Oracle account')]").text

print(actual_header)

driver.find_element(By.ID, "sso_username").send_keys("bala@gmail.com")
driver.find_element(By.ID, "ssopassword").send_keys("bala@gmail.com")

driver.find_element(By.ID, "signin_button").click()

time.sleep(5)

actual_error = driver.find_element(By.XPATH, "//div[contains(text(),'Invalid')]").text
print(actual_error)

time.sleep(5)
driver.quit()
