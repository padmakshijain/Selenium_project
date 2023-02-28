import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")

driver.find_element(By.NAME, "UserFirstName").send_keys("padmakshi")
driver.find_element(By.NAME, "UserLastName").send_keys("Jain")
driver.find_element(By.NAME, "UserEmail").send_keys("padmakshi@gmail.com")

select_job = Select(driver.find_element(By.NAME, "UserTitle"))
select_job.select_by_value("IT_Manager_AP")

select_employee = Select(driver.find_element(By.NAME, "CompanyEmployees"))
select_employee.select_by_value("250")

# .find_element(By.NAME, "UserPhone").send_keys("1234567890")
driver.find_element(By.NAME, "CompanyName").send_keys("Arrow")
driver.find_element(By.XPATH, "//div[@class='checkbox-ui']")
driver.find_element(By.CLASS_NAME, "checkbox-ui").click()
driver.find_element(By.NAME, "start my free trial").click()

actual_error = driver.find_element(By.XPATH, "//span[contains(@id,'UserPhone')]").text
print(actual_error)
time.sleep(5)
driver.quit()
