import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.online.citibank.co.in/")

# //a[@class='fancybox-item fancybox-close']
driver.find_element(By.CLASS_NAME, "fancybox-close").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Login']").click()

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH, "//div[contains(text(),'Forgot User')]").click()

driver.find_element(By.LINK_TEXT, "select your product type").click()
driver.find_element(By.LINK_TEXT, "Credit Card").click()



driver.find_element(By.CSS_SELECTOR, "#citiCard1").send_keys("7897")
driver.find_element(By.CSS_SELECTOR, "input[name='citiCard2']").send_keys("7897")
driver.find_element(By.CSS_SELECTOR, "[name='citiCard3']").send_keys("7897")
driver.find_element(By.ID, "citiCard4").send_keys("7897")

driver.find_element(By.ID, "cvvnumber").send_keys("889")

# approach 1 - not working
# driver.find_element(By.ID,"bill-date-long").send_keys("14/04/2022")

# approach 2
# driver.find_element(By.ID,"bill-date-long").click()
#
# select_year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
# select_year.select_by_visible_text("2000")
#
# select_month=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
# select_month.select_by_visible_text("Apr")
#
# driver.find_element(By.LINK_TEXT,"14").click()

# approach 3 - javascript
# driver.execute_script("document.querySelector('#bill-date-long').value='11/09/2000'")

# driver.execute_script("document.querySelector(\"input[name='DOB']\").value='17/06/1999'")

ele1 = driver.find_element(By.XPATH, "//input[@name='DOB']")
driver.execute_script("arguments[0].value='11/09/2000'", ele1)

driver.find_element(By.XPATH, "//input[@value='PROCEED']").click()

actual_error1 = driver.find_element(By.XPATH, "//li[contains(text(),'Term')]").text

actual_error2 = driver.find_element(By.XPATH, "//div[@role='dialog']").text

print(actual_error1)
print(actual_error2)

time.sleep(5)
driver.quit()
