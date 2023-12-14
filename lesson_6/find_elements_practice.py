import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/tracks")
driver.maximize_window()
time.sleep(3)

print(driver.find_elements("class name", "nav-link"))
print(len(driver.find_elements("class name", "nav-link")))

driver.find_elements("class name", "nav-link")[2].click()    #при наличии нескольких одноименных элементов

time.sleep(4)