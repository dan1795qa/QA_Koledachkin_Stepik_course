import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation")
# options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

""""Locators"""
HYPERSKILL_BUTTON = ("xpath", "//button[@type='submit']")
AVITO_BUTTON = ("xpath", "//button[@type='button']")
OZON_BUTTON = ("xpath", "//div[text()='BYN']")

driver.get("https://hyperskill.org/login")
driver.switch_to.new_window("tab")
driver.get("https://www.avito.ru/")
driver.switch_to.new_window("tab")
driver.get("https://www.ozon.ru/")

list_of_tabs = driver.window_handles

driver.switch_to.window(list_of_tabs[0])
handles_1 = driver.title
print(handles_1)
driver.switch_to.window(list_of_tabs[1])
handles_2 = driver.title
print(handles_2)
driver.switch_to.window(list_of_tabs[2])
handles_3 = driver.title
print(handles_3)


driver.switch_to.window(list_of_tabs[0])
driver.find_element(*HYPERSKILL_BUTTON).click()

driver.switch_to.window(list_of_tabs[1])
driver.find_element(*AVITO_BUTTON).click()

driver.switch_to.window(list_of_tabs[2])
driver.find_element(*OZON_BUTTON).click()

# assert second_tab != main_tab, "Ошибка переключения между вкладками"

driver.switch_to.window(list_of_tabs[0])

