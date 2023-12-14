import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com/")

url = driver.current_url
print(f"Current url: {url}")
assert url == "https://www.youtube.com/", "Mistake in URL"

current_title = driver.title
print(f"Current title: {current_title}")
assert current_title == "YouTube", "Mistake in title"

print(driver.page_source)  # получение кода страницы
