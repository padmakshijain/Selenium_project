import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.medibuddy.in/")


driver.find_element(By.XPATH,"//a[text()='Login']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[@class='coperate']").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//div[@class='coperate'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Enter Username']").send_keys("john")
driver.find_element(By.XPATH,"//button[normalize-space()='Proceed']").click()
driver.find_element(By.NAME,"password").send_keys("john123")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
actual_error = driver.find_element(By.XPATH, "//div[@class='alert alert-danger errorTxt']").text
print(actual_error)
time.sleep(5)
driver.quit()