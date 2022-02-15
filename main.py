from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get("https://www.hktvmall.com/")

elem = driver.find_element(By.CSS_SELECTOR, '.SuggestionSearch-input')

elem.send_keys("魚")
elem.send_keys(Keys.ENTER)

print("done")
