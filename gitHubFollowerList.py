from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class GitHubBot():
    def __init__(self, username, browser):
        self.username = username
        self.browser = browser
        self.url = "https://github.com"
        self.followers = []

    def controller(self):
        self.browser.get(self.url + f"/{self.username}")
        time.sleep(2)
        self.browser.maximize_window()
        time.sleep(2)
        following = self.browser.find_element(By.CSS_SELECTOR, "a.Link--secondary:nth-child(2)")
        time.sleep(2)
        following.click()
        time.sleep(2)
        followers_section = self.browser.find_element(By.CSS_SELECTOR, "#user-profile-frame > div:nth-child(1)")
        time.sleep(2)
        follower_elements = followers_section.find_elements(By.CSS_SELECTOR, ".f4.Link--primary")
        time.sleep(2)
        for follower in follower_elements:
            self.followers.append(follower.text)

        for follower in self.followers:
            print(follower)

