import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from gazpacho import Soup

def remove_duplicates(source_list):
    result = []
    [result.append(x) for x in source_list if x not in result]
    return result

def scroll_down(driver, timeout):
    print("begining scroll")
    scroll_pause_time = timeout
    
    output = []

    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:

        output.extend(elem.get_attribute("href") for elem in driver.find_elements_by_xpath("//a[@href]") if "/p/" in elem.get_attribute("href"))

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(scroll_pause_time)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:            
                   print("Done scroll")
                   return remove_duplicates(output)
       
        last_height = new_height
     





