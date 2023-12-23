import time
import os
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# driver.get("https://hyperskill.org/tracks")

# """"ex1"""
# driver.add_cookie({
#     "name": "username",
#     "value": "user123"
# })
# driver.refresh()
# print(driver.get_cookie("username"))

# """"ex2"""
# print(driver.get_cookie("userid"))
# driver.delete_cookie("userid")
# # driver.refresh()
# print(driver.get_cookie("userid"))

""""ex3"""
driver.get("https://5element.by/")

BUTTON1 = ("xpath", "//button[@data-product_id='789852']")
BUTTON2 = ("xpath", "//span[text()='Удалить']")

driver.execute_script("window.scroll(0,1200)")

cart_button = wait.until(EC.element_to_be_clickable(BUTTON1)).click()

pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies_hw_14/cookies_hw.pkl", "wb"))

# cart_delete_button = wait.until(EC.element_to_be_clickable(BUTTON2)).click()

driver.delete_all_cookies()

print(driver.get_cookies())
driver.refresh()

cookies = pickle.load(open(os.getcwd()+"/cookies_hw_14/cookies_hw.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

time.sleep(5)
