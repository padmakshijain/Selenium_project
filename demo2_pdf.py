import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("file:///C:/Users/146698/Downloads/hb_capl_programming.pdf")

print(driver.title)

time.sleep(5)
driver.find_element(By.ID,"pageSelector").click()
driver.find_element(By.ID,"pageSelector").send_keys("90")
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# ele=driver.find_element(By.ID,"email")
# ele.send_keys("hello@gmail.com")

# driver.find_element(By.ID, "email").send_keys("hello1234@gmail.com")
# driver.find_element(By.ID, "pass").send_keys("welcome123")
# driver.find_element(By.NAME, "login").click()
#
# time.sleep(10)
# driver.quit()
