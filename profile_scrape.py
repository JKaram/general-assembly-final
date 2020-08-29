import pandas as pd
import time
from selenium.webdriver import Chrome
from selenium import webdriver



browser = webdriver.Chrome('/mnt/c/Users/jamie/Downloads/chromedriver_linux64/chromedriver.exe') 

url = "https://www.instagram.com/jamie_karam"
browser.get(url)