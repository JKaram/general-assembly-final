import time
import pandas as pd
from selenium import webdriver
from gazpacho import Soup

from post_scrape import scrape_post
from profile_scrape import scroll_down, remove_duplicates
from selenium.webdriver import ActionChains


def smash_button(driver, timeout):
    try:
        close = driver.find_elements_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div/div/button')
        close[0].click() 
        time.sleep(timeout)
        button = driver.find_elements_by_xpath('/html/body/div[1]/section/main/div/div[3]/div[1]/div/button')
        button[0].click()    
        return print('Smashed')    
    except:
        return print('Button Not Found')
    
    
    
    
    
    