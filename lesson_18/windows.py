import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--window-size=1920,1080")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

""""Locators"""

FOR_BUSINESS_BUTTON_LOCATOR = ("xpath", "//a[text()=' For Business ']")
START_FREE_BUTTON_LOCATOR = ("xpath", "//a[text()='Start for Free']")

driver.get("https://hyperskill.org/tracks")
time.sleep(5)

# -----------------------------------Переключение между вкладками------------------------------------------------------
# print(driver.current_window_handle)
# print(driver.window_handles)

# driver.find_element(*FOR_BUSINESS_BUTTON_LOCATOR).click()
# time.sleep(3)
#
# tabs = driver.window_handles
# driver.switch_to.window(tabs[1])
#
#
# driver.find_element(*START_FREE_BUTTON_LOCATOR).click()
# time.sleep(3)

# -----------------------------------Переключение между окнами------------------------------------------------------

windows = driver.window_handles
driver.switch_to.window(windows[1])

driver.get("https://ya.ru")
time.sleep(3)

# -----------------------------------Доп. методы------------------------------------------------------

driver.switch_to.new_window("tab")    # переключится автоматически на новую вкладку
driver.switch_to.new_window("window")    # переключится автоматически на новое окно
time.sleep(3)