import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

CHANGE_TEXT_BUTTON = ("xpath", "//button[contains(text(), 'Change Text to Selenium Webdriver')]")
SITE_BUTTON = ("xpath", "//h2[contains(text(), 'site')]")
ANOTHER_BUTTON = ("xpath", "//h2[contains(text(), 'Selenium Webdriver')]")
wait.until(EC.element_to_be_clickable(CHANGE_TEXT_BUTTON)).click()
wait.until(EC.invisibility_of_element_located(SITE_BUTTON))
wait.until(EC.visibility_of_element_located(ANOTHER_BUTTON))
print("ex1 DONE!")

DISPLAY_BUTTON = ("xpath", "//button[contains(text(), 'Display button after 10 seconds')]")
ENABLE_BUTTON1 = ("xpath", "//button[@id='hidden']")
wait.until(EC.element_to_be_clickable(DISPLAY_BUTTON)).click()
wait.until(EC.text_to_be_present_in_element(ENABLE_BUTTON1, 'Enabled'))
print("ex2 DONE!")

CHECK_BUTTON = ("xpath", "//button[contains(text(), 'Enable button after 10 seconds')]")
ENABLE_BUTTON2 = ("xpath", "//button[@id='disable']")
wait.until(EC.element_to_be_clickable(CHECK_BUTTON)).click()
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON2)).click()
print("ex3 DONE!")

CLICK_ME_ALERT_AFTER_FIVE_SECS = ("xpath", "//button[@id='alert']")
wait.until(EC.element_to_be_clickable(CLICK_ME_ALERT_AFTER_FIVE_SECS)).click()
wait.until(EC.alert_is_present())
alert_text = driver.switch_to.alert.text
print(alert_text)
assert alert_text == "I got opened after 5 secods", "error alert"
print("ex4 DONE!")

