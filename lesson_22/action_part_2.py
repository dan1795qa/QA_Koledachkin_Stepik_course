import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

option = Options()
option.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=option, service=service)
action = ActionChains(driver)

driver.get("https://the-internet.herokuapp.com/drag_and_drop")

""""Locators"""
COLUMN_A = ("xpath", "//div[@id='column-a']")
COLUMN_B = ("xpath", "//div[@id='column-b']")

A = driver.find_element(*COLUMN_A)
B = driver.find_element(*COLUMN_B)

time.sleep(3)
action.drag_and_drop(A, B).perform()   #принимает 2 веб-элемента, не локаторы!!!
time.sleep(3)

# ---------------------------------------------------------------------------------------------------

driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")

""""Locators"""
GRID_ITEM = ("xpath", "//div[@class='grid__item'][2]")
SITE_BAR = ("xpath", "//div[@class='drop-area__item'][2]")

action.click_and_hold(driver.find_element(*GRID_ITEM))\
    .pause(2)\
    .move_to_element(driver.find_element(*SITE_BAR))\
    .release()\
    .perform()
time.sleep(2)