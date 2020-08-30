import pandas as pd
import time
from selenium import webdriver
from gazpacho import Soup

def scroll_find_links(driver, timeout, soup):
    links = []
    scroll_pause_time = timeout

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(scroll_pause_time)
        new_links = soup.find('a', {'href' : "/p/"})
        links.extend(new_links)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            posts = [l.attrs["href"] for l in links if "/p/" in l.attrs["href"]]
            return posts
        last_height = new_height





