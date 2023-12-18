import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\downloads"
}
chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# """"ex_1"""
# driver.get("https://demoqa.com/upload-download/")
# time.sleep(2)
# load_el = driver.find_element("xpath", "//input[@type='file']")
# load_el.send_keys(f"{os.getcwd()}\downloads\Знімок екрана 2023-12-13 о 17.49.04.png")
# time.sleep(3)


""""ex_2"""
driver.get("https://the-internet.herokuapp.com/download")
time.sleep(2)
el_l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in el_l:
    driver.find_elements("xpath", f"//*[@id='content']/div/a")[i].click()
    time.sleep(2)


