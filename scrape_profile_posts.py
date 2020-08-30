import time
import pandas as pd
from selenium import webdriver
from gazpacho import Soup

from post_scrape import scrape_post
from profile_scrape import scroll_find_links

url = "https://www.instagram.com/clintstevenstv/"
browser = webdriver.Chrome('/mnt/l/projects/instagram-data/chromedriver.exe') 
browser.get(url)
html = browser.page_source
soup = Soup(html)

name = soup.find('h2').text
posts = soup.find('span', {'class' : "g47SY"})[0].text
followers =  soup.find('span', {'class' : "g47SY"})[1].text
following = soup.find('span', {'class' : "g47SY"})[2].text

profile = {
    "name" : name,
    "posts" : posts,
    "followers" : followers,
    "following" : following
}

posts = scroll_find_links(browser, .8, soup)

data = []

for post in posts: 
    url = f"https://www.instagram.com{post}"
    browser.get(url)
    html = browser.page_source
    soup = Soup(html)
    data.append(scrape_post(soup, profile))
    time.sleep(.8)

print(data)