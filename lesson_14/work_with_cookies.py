import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/en/us/login")
# print(driver.get_cookie("country_code"))
# print(driver.get_cookies())
# -----------------------------------------------------------------------
# driver.add_cookie({
#     "name": "Example",
#     "value": "Kukushka"
# })
#
# print(driver.get_cookie("Example"))
#--------------------------------------------------------------------------

# before1 = driver.get_cookie("split")
# print(before1)
#
# driver.delete_cookie("split")
#
# driver.add_cookie({
#     "name": "split",
#     "value": "QWERTY"
# })
# after1 = driver.get_cookie("split")
# print(after1)

# -------------------------------------------------------------

before2 = driver.get_cookies()
print(before2)

driver.delete_all_cookies()

driver.add_cookie({
    "name": "split",
    "value": "QWERTY"
})

after2 = driver.get_cookies()
print(after2)

