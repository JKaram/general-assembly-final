import pandas as pd
import time
from selenium import webdriver
from gazpacho import Soup



url = "https://www.instagram.com/iscotchdotca/"
browser = webdriver.Chrome('/mnt/l/projects/instagram-data/chromedriver.exe') 
browser.get(url)
html = browser.page_source
soup = Soup(html)
links = []

def scroll(driver, timeout):
    scroll_pause_time = timeout

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(scroll_pause_time)
        new_links = soup.find('a', {'href' : "/p/"})
        links.extend(new_links)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height




scroll(browser, .8)
posts = [l.attrs["href"] for l in links if "/p/" in l.attrs["href"]]
print(len(posts))
