from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

s = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("https://www.hktvmall.com/")

elem = driver.find_element(By.CSS_SELECTOR, '.SuggestionSearch-input')

elem.send_keys("魚")
elem.send_keys(Keys.ENTER)

driver.quit()

print("done")
