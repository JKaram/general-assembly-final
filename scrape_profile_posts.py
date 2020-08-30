import time
import pandas as pd
from selenium import webdriver
from gazpacho import Soup

from post_scrape import scrape_post
from profile_scrape import scroll_down, remove_duplicates

url = "https://www.instagram.com/clintstevenstv/"
browser = webdriver.Chrome('/mnt/l/projects/instagram-data/chromedriver.exe') 
browser.get(url)
html = browser.page_source
soup = Soup(html)


name = soup.find('h2').text
num_of_posts = soup.find('span', {'class' : "g47SY"})[0].text
followers =  soup.find('span', {'class' : "g47SY"})[1].text
following = soup.find('span', {'class' : "g47SY"})[2].text


posts = scroll_down(browser, 4)


profile = {
    "name" : name,
    "posts" : num_of_posts,
    "followers" : followers,
    "following" : following
}


data = []

for post in posts: 
    url = post
    browser.get(url)
    html = browser.page_source
    soup = Soup(html)
    data.append(scrape_post(soup, profile, url))
    time.sleep(1)


df = pd.DataFrame(data)

print(df)


            