import pandas as pd
import time
from selenium import webdriver
from gazpacho import Soup

url = "https://www.instagram.com/p/CC_ahZ4lXjG/"
browser = webdriver.Chrome('/mnt/l/projects/instagram-data/chromedriver.exe') 
browser.get(url)
html = browser.page_source
soup = Soup(html)

print(soup)