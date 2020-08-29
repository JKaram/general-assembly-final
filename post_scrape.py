import pandas as pd
import time
from selenium import webdriver
from gazpacho import Soup

url = "https://www.instagram.com/p/CAD1W62F0UH/"
browser = webdriver.Chrome('/mnt/l/projects/instagram-data/chromedriver.exe') 
browser.get(url)
html = browser.page_source
soup = Soup(html)

likes = soup.find('div', {'class' : 'Nm9Fw'}).find('span').text
date = soup.find('time')[0].attrs['datetime']
comments = len(soup.find('ul', {'class' : 'XQXOT'}).find('span')) - 1
