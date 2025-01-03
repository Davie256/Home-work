# Write your code here :-)
import requests, webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

def scaping_from_website():
    driver.get('https://www.unsplash.com')
    #browser.implicitly_wait(40)

def item_to_search():
    search_box = driver.find_element(By.TAG_NAME,'input')
    search_box.send_keys('apple')
    #browser.implicitly_wait(40)
    #driver.find_element(By.ID,'apple').send_keys(Keys.ENTER)

    #search_box.send_keys(Keys.ENTER)
    search_box.submit()

def main():
    scaping_from_website()
    item_to_search()

main()
