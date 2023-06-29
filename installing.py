from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://github.com"
browser = webdriver.Firefox()

browser.get(url)
time.sleep(2)

searchInput = browser.find_element(By.NAME, 'q')
searchInput.send_keys("selenium", Keys.ENTER)


