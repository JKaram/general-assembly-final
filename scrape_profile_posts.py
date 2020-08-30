import time
import pandas as pd
from selenium import webdriver
from gazpacho import Soup

from post_scrape import scrape_post
from profile_scrape import scroll_down, remove_duplicates
from smash_button import smash_button
from tqdm import tqdm


url = "https://www.instagram.com/codyshreed/"
browser = webdriver.Firefox(executable_path='/mnt/l/projects/instagram-data/geckodriver.exe') #'/mnt/l/projects/instagram-data/chromedriver.exe'
browser.get(url)
html = browser.page_source
soup = Soup(html)

name = soup.find('h2').text
num_of_posts = soup.find('span', {'class' : "g47SY"})[0].text
followers =  soup.find('span', {'class' : "g47SY"})[1].text
following = soup.find('span', {'class' : "g47SY"})[2].text
time.sleep(3)

smash_button(browser, 2)


posts = scroll_down(browser, .3)


profile = {
    "name" : name,
    "posts" : num_of_posts,
    "followers" : followers,
    "following" : following
}


data = []

for post in tqdm(posts): 
    url = post
    browser.get(url)
    html = browser.page_source
    soup = Soup(html)
    data.append(scrape_post(soup, profile, url))
    time.sleep(.3)


df = pd.DataFrame(data)


df.to_csv(f'/profile_csvs/{name}.csv')
            