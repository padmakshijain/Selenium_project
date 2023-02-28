import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.facebook.com")

driver.find_element(By.LINK_TEXT, "Create new account").click()
# time.sleep(5)
driver.find_element(By.NAME, "firstname").send_keys("padmakshi")
driver.find_element(By.NAME, "lastname").send_keys("jain")
driver.find_element(By.NAME, "reg_email__").send_keys("padmakshi231@gmail.com")
driver.find_element(By.ID, "password_step_input").send_keys("welcome123@")
# driver.find_element(By.ID, "day").send_keys("23")
# driver.find_element(By.ID, "month").send_keys("Jan")
# driver.find_element(By.ID, "year").send_keys("2000")
driver.find_element(By.XPATH, "//input[@value='1']").click()

select_day= Select(driver.find_element(By.ID,"day"))
select_day.select_by_visible_text("20")

select_day=Select(driver.find_element(By.ID,"month"))
select_day.select_by_visible_text("Dec")

select_day=Select(driver.find_element(By.ID,"year"))
select_day.select_by_visible_text("2000")

driver.find_element(By.NAME, "websubmit").click()
time.sleep(5)
