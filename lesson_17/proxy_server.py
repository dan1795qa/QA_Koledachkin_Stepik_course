import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

PROXY_SERVER = "username:password@192.168.2.2"

options = Options()
options.add_argument(f"--proxy-server={PROXY_SERVER}")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://free-proxy.cz/ru/")
time.sleep(3)