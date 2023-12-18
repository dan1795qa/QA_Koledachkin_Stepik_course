import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()                          # нужно объявить до инифциализации драйвера

chrome_options.page_load_strategy = "normal"    #eager                    # стратегия загрузки страницы (PAGE LOAD STRATEGY)
# chrome_options.add_argument("--headless")                         # HEADLESS MODE (БЕЗГОЛОВЫЙ РЕЖИМ) - запускает тесты без интерфейса (в фоне)
# chrome_options.add_argument("--incognito")                          # позволяет проводить тест без кэша(более чистый тест)
# chrome_options.add_argument("--ignore-certificate-errors")          # позволяет игнорировать отсутсвтие сертификатов
chrome_options.add_argument("--window-size=1920,1080")                # размеры экрана
# chrome_options.add_argument("--disable-cache")                      # убирает кэш

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# driver.set_window_size(1920, 1080)                                  # размеры экрана
start = time.time()

driver.get("https://whatismyipaddress.com/")
# driver.get("https://expired.badssl.com/")

finish = time.time()
df = (finish-start)
print(df)




