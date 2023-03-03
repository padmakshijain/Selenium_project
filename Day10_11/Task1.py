import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.redbus.in/")

driver.find_element(By.XPATH, "//i[@id='i-icon-profile']").click()
driver.find_element(By.ID, "hc").click()

driver.find_element(By.XPATH, "//input[@class='IP']").click()

actual_error = driver.find_element(By.XPATH, "//span[@class='error-message-fixed error-message-full top-fix']").text

print(actual_error)
time.sleep(5)
driver.quit()
