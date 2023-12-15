import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

""""ex_1"""
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

full_name = driver.find_element("xpath", "//input[@id='userName']")
full_name.clear()
full_name.send_keys("myName")
assert full_name.get_attribute("value") == "myName"
time.sleep(3)

email_area = driver.find_element("xpath", "//input[@id='userEmail']")
email_area.clear()
email_area.send_keys("myName@mail.com")
assert email_area.get_attribute("value") == "myName@mail.com"
time.sleep(3)

current_address = driver.find_element("xpath", "//textarea[@id='currentAddress']")
current_address.clear()
current_address.send_keys("Moscow, Russia")
assert current_address.get_attribute("value") == "Moscow, Russia"
time.sleep(3)

permanent_address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
permanent_address.clear()
permanent_address.send_keys("Minsk, Belarus")
assert permanent_address.get_attribute("value") == "Minsk, Belarus"
time.sleep(3)

""""ex_2"""
driver.get("https://the-internet.herokuapp.com/status_codes")
driver.maximize_window()

el_200 = "//a[contains(text(), '200')]"
el_301 = "//a[contains(text(), '301')]"
el_404 = "//a[contains(text(), '404')]"
el_500 = "//a[contains(text(), '500')]"

el_list = [el_200, el_301, el_404, el_500]

for i in el_list:
    el = driver.find_element("xpath", i)
    el.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)
