import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.royalcaribbean.com/")

driver.find_element(By.XPATH, "//div[@class='notification-banner__close']").click()
driver.find_element(By.XPATH, "(//span[contains(text(),'Sign In')])[1]").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Create an account']").click()
driver.find_element(By.ID, "mat-input-3").send_keys("Dennis")
driver.find_element(By.ID, "mat-input-4").send_keys("Rich")

driver.implicitly_wait(5)
# select=Select(driver.find_element(By.LINK_TEXT,'Month'))
# select.select_by_visible_text('February')
driver.find_element(By.XPATH, "//span[normalize-space()='Month']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='April']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Day']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='4']").click()
driver.find_element(By.XPATH, "//input[@id='mat-input-3']").send_keys("1990")
driver.find_element(By.XPATH, "//span[normalize-space()='Country/Region of residence']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='India']").click()
driver.find_element(By.XPATH,"//input[@data-placeholder='Email address']").send_keys("kk123@gmail.com")
driver.find_element(By.XPATH,"//input[@id='mat-input-4']").send_keys("manish@123")
driver.find_element(By.XPATH,"//span[text()='Select one security question']").click()
driver.find_element(By.XPATH,"//mat-option[@id='mat-option-298']//span[@class='mat-option-text']").click()
driver.find_element(By.XPATH,"//input[@id='mat-input-5']").send_keys("Kia")
driver.find_element(By.XPATH,"//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']").click()
driver.find_element(By.XPATH,"//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Done']").click()


time.sleep(5)
driver.quit()