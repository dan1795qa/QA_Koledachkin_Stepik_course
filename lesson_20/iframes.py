import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


option = Options()
option.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=option, service=service)

# """"Locators"""
# FORM_NAME_FIELD_LOCATOR = ("xpath", "//input[@id='RESULT_TextField-0']")
# COPY_TEXT_LOCATOR = ("xpath", "//button[text()='Copy Text']")
# IFRAME_LOCATOR = ("xpath", "//iframe")
#
# driver.get("https://testautomationpractice.blogspot.com/")
# # driver.switch_to.frame("frame-one796456169")
# iframe = driver.find_element(*IFRAME_LOCATOR)
# driver.switch_to.frame(iframe)
# time.sleep(3)
# driver.find_element(*FORM_NAME_FIELD_LOCATOR).send_keys("Aleksei")
# time.sleep(3)
# driver.switch_to.default_content()
# driver.find_element(*COPY_TEXT_LOCATOR).click()
# time.sleep(3)

# -------------------------------------------------------------------------

""""Locators"""
FRAME1 = ("xpath", "//iframe[@id='frame1']")
COPY_TEXT_LOCATOR = ("xpath", "//button[text()='Copy Text']")


driver.get("https://demoqa.com/nestedframes")
driver.switch_to.frame("frame1")
print(driver.find_element(by="xpath", value="//body").text)

driver.switch_to.frame(0)
print(driver.find_element(by="xpath", value="//body").text)

time.sleep(3)

driver.switch_to.parent_frame()
print(driver.find_element(by="xpath", value="//body").text)

driver.switch_to.default_content()
