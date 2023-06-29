from gitHubFollowerList import GitHubBot
from selenium import webdriver

username = input("Enter the Username of the user you want to receive the tracking list : ")
browser = webdriver.Firefox()
bot = GitHubBot(username, browser)
bot.controller()