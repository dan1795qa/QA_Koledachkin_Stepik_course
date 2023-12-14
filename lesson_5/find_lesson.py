import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/login")


# －Способы поиска эквивалентные By.***:
"""Set of supported locator strategies."""

ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"


driver.find_element("id", "loginformsubmit").click()

time.sleep(3)