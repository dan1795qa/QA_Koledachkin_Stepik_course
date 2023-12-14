import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://vk.com")
print(driver.title)
time.sleep(4)

driver.get("https://www.youtube.com/")
print(driver.title)

driver.back()
url = driver.current_url
print(url)
assert url == "https://vk.com/", "Mistake in URL"


driver.refresh()
print(f"Current URL: {driver.current_url}")

driver.forward()
print(driver.current_url)

driver.quit()