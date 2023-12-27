import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select



service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")
driver.get("https://the-internet.herokuapp.com/dropdown")

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
# time.sleep(3)
# DROPDOWN.select_by_visible_text("Option 1")
# time.sleep(3)
#
# #---------------------------------------------------------------
#
# DROPDOWN.select_by_value("2")
# time.sleep(3)
#
# #---------------------------------------------------------------
# DROPDOWN.select_by_index(1)
# time.sleep(3)

#---------------------------------------------------------------
all_options = DROPDOWN.options
# print(all_options)

# for option in all_options:
#     time.sleep(3)
#     if "Option 1" in option.text:
#         print("good!")
#     DROPDOWN.select_by_visible_text(option.text)

#---------------------------------------------------------------

# for option in all_options:
#     time.sleep(3)
#     DROPDOWN.select_by_index(all_options.index(option))

#---------------------------------------------------------------

for options in all_options:
    time.sleep(3)
    DROPDOWN.select_by_value(options.get_attribute("value"))