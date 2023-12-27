import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/selectable")

GRID_BUTTON = ("xpath", "//a[@id='demo-tab-grid']")
ONE_BUTTON = ("xpath", "//li[text()='One']")
FOUR_BUTTON = ("xpath", "//li[text()='Four']")
SEVEN_BUTTON = ("xpath", "//li[text()='Seven']")

driver.find_element(*GRID_BUTTON).click()
time.sleep(3)

before = driver.find_element(*ONE_BUTTON).get_attribute("class")
print(before)
driver.find_element(*ONE_BUTTON).click()
driver.find_element(*ONE_BUTTON).is_selected()
time.sleep(3)

after = driver.find_element(*ONE_BUTTON).get_attribute("class")
print(after)
assert "active" in after

driver.find_element(*ONE_BUTTON).click()
check_after = driver.find_element(*ONE_BUTTON).get_attribute("class")
print(check_after)


