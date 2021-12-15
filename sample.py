from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver = webdriver.Chrome(executable_path="C:\\Users\\nikhil.mn\\eclipse-workspace\\Qualitest\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.close()
