import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls

option = Options()
option.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=option, service=service)
action = ActionChains(driver)
scrolls = Scrolls(driver, action)

driver.get("https://seiyria.com/bootstrap-slider/")

EX_2_LOCATOR = ("xpath", "//h3[text()='Example 2: ']")
ex_2 = driver.find_element(*EX_2_LOCATOR)

scrolls.scroll_to_element(ex_2)

time.sleep(3)
""""Locators"""