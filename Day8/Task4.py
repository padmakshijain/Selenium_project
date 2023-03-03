import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.automationworld.com/")

time.sleep(5)
#driver.find_element(By.XPATH, "//div[@class='close-olytics-image-bottom-midyellow']").click()
driver.find_element(By.XPATH, "//span[@class='site-navbar__label'][normalize-space()='Subscribe']").click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='id24_344']").click()
#driver.find_element(By.NAME, "demo59701").click()
driver.find_element(By.XPATH, "//input[@id='id1']").send_keys("Padmakshi")
driver.find_element(By.XPATH, "//input[@id='id2']").send_keys("Jain")
driver.find_element(By.XPATH, "//input[@id='id10']").send_keys("Engineer")
driver.find_element(By.XPATH, "//input[@id='id195']").send_keys("https://www.einfochips.com/")
driver.find_element(By.XPATH, "//input[@id='id3']").send_keys("Einfochips")
driver.find_element(By.XPATH, "//input[@id='id11']").send_keys("7014281376")
driver.find_element(By.XPATH,"//option[@value='189']").click()
driver.find_element(By.XPATH,"//input[@id='id6']").send_keys("Chennai")
driver.find_element(By.XPATH,"//input[@id='id339_2327']").click()
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
actual_error = driver.find_element(By.XPATH,"//li[normalize-space()='Email Address is required.']").text
print(actual_error)


time.sleep(5)
driver.quit()
