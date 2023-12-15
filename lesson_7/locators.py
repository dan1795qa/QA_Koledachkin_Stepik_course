import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://hyperskill.org/tracks")
driver.maximize_window()
time.sleep(3)


""""LOGO"""
driver.find_element("xpath", "(//header//div//div//div[1])").click()
time.sleep(3)

""""LOGO"""
driver.find_element("xpath", "//*[@id='header']/div/ul/li/a").click()
time.sleep(3)

""""Inscription"""
n = driver.find_element("xpath", '//h1[contains(text(), "What is your learning goal?")]')
n.click()
print(n.text)
assert n.text == "What is your learning goal?", "error assert"
time.sleep(3)


""""Top Tracks"""
driver.find_element("xpath", "/html/body/div/main/div/div/div/section/div[1]/a[2]").click()
time.sleep(3)

""""Introduction to Python"""
driver.find_element("xpath", "(//div[@class='card-body'])[3]").click()
time.sleep(7)


