import pandas as pd
import time
from selenium import webdriver
from gazpacho import Soup

def remove_duplicates(source_list):
    result = []
    [result.append(x) for x in source_list if x not in result]
    return result

def scroll_down(driver, timeout):
    links = []
    links.extend(driver.find_elements_by_xpath("//a[@href]"))
    scroll_pause_time = timeout
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        links.extend(driver.find_elements_by_xpath("//a[@href]"))
        time.sleep(scroll_pause_time)


        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # posts = [l.attrs["href"] for l in links if "/p/" in l.attrs["href"]]
            
            # return remove_duplicates(posts)
            output = []
            for elem in links:
                try:
                    output.append(elem.get_attribute("href"))
                except:
                    pass
            output = [l for l in output if "/p/" in l]
            return remove_duplicates(output)
        last_height = new_height
     





