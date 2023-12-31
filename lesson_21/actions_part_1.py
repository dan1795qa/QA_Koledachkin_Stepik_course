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

""""Locators"""
LEFT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@name='leftClick']")
DOUBLE_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@name='doubleClick']")
RIGHT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@name='rightClick']")
HOVOR_BUTTON = ("xpath", "//button[@name='colorChangeOnHover']")



driver.get("https://testkru.com/Elements/Buttons")

left_button = driver.find_element(*LEFT_CLICK_BUTTON_LOCATOR)
double_click = driver.find_element(*DOUBLE_CLICK_BUTTON_LOCATOR)
right_click = driver.find_element(*RIGHT_CLICK_BUTTON_LOCATOR)
hovor_button = driver.find_element(*HOVOR_BUTTON)


# time.sleep(3)
# action.click(left_button).perform()
# time.sleep(3)
# action.double_click(double_click).perform()
# time.sleep(3)
# action.context_click(right_click).perform()
# time.sleep(3)

# ----------------------------------------------------------------------------------------

""""ActionChains"""
action.click(left_button).pause(3).double_click(double_click).pause(1).context_click(right_click).perform()


# -----------------------------------------------------------------------------------------

action.move_to_element(hovor_button).perform()
time.sleep(3)

# -----------------------------------------------------------------------------------------

driver.get("https://demoqa.com/menu")
MENU_ITEM_2_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
SUB_LIST_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")

menu_item_2 = driver.find_element(*MENU_ITEM_2_LOCATOR)
sub_list_menu = driver.find_element(*SUB_LIST_LOCATOR)

action.move_to_element(menu_item_2)\
    .pause(3).move_to_element(sub_list_menu)\
    .pause(2).perform()

