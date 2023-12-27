import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

SELECT_LOCATOR = ("xpath", "//input[@id='react-select-2-input']")

driver.get("https://demoqa.com/select-menu")
time.sleep(2)
driver.find_element(*SELECT_LOCATOR).send_keys("Ms.")
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)

time.sleep(5)

# setTimeout(function() { debugger; }, 5000);?    код JS для замарозки

