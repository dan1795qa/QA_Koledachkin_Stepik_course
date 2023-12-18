import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(2)
driver.find_element("xpath", "//input[@type='file']").send_keys(f"{os.getcwd()}\downloads\lnrc-2023-12-18T06-46-22.221.log")
time.sleep(2)
