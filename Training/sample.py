import time

import self as self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

# driver = webdriver.Chrome(executable_path="C:\\Users\\nikhil.mn\\eclipse-workspace\\Qualitest\\chromedriver.exe")
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:\\Users\\nikhil.mn\\eclipse-workspace\\Qualitest\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.implicitly_wait(8)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,"//label/input[@type='checkbox']")))

# checkboxes = driver.find_elements_by_xpath(self,"//label/input[@type='checkbox']")
checkboxes = driver.find_elements(By.XPATH, "//label/input[@type='checkbox']")

# //label/input[@type='checkbox']/parent::label

print(len(checkboxes))

list = []

for checkbox in checkboxes:
    list.append(checkbox.find_element(By.XPATH,"parent::label").text)
    checkbox.click()
    assert checkbox.is_selected()
    # checkbox.click()
    # assert ~(checkbox.is_selected())
print(list)
time.sleep(4)
driver.close()
