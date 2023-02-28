import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.sodapdf.com/pdf-to-word/")

driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
    r"C:/Users/146698/OneDrive%20-%20Arrow%20Electronics,%20Inc/Desktop/Jira/Getting+Started+in+Jira.pdf")

time.sleep(5)
driver.quit()
