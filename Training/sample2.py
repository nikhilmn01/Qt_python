import time

import self as self
from selenium import webdriver
from selenium.webdriver import ActionChains
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
driver.get("https://the-internet.herokuapp.com/windows")

actions = ActionChains(driver)
# actions.double_click()
# actions.move_to_element()
# actions.context_click()
# actions.click_and_hold("...").perform()
driver.find_element(By.XPATH,"//a[text()='Click Here']").click()
childWindow = driver.window_handles[1]
parentWindow = driver.window_handles[0]

print(childWindow)


driver.switch_to.window(childWindow)
print(driver.find_element(By.XPATH,"//h3[text()='New Window']").text)

time.sleep(2)
driver.switch_to.window(parentWindow)

text = driver.find_element(By.XPATH,"//h3").text

time.sleep(3)

driver.get_screenshot_as_file("sample.png")
driver.quit()