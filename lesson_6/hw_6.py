import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element("class name", "wikipedia-icon").click()
time.sleep(3)

driver.find_element("id", "Wikipedia1_wikipedia-search-input").click()
time.sleep(10)