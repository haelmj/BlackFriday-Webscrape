"""
author: Michael Ndon
title: Blackfridayscrape
subject-website: jumia.com.ng

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import csv
import time
import os

# set path to chromedriver and initialize chrome webdriver
STARTPAGE = 'https://www.jumia.com.ng/mlp-black-friday/?sort=lowest-price&rating=4-5'
PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# load web page; set window handle to 0; set storage folder
driver.get(STARTPAGE)
black_deals_window = driver.window_handles[0]
FOLDER = 'categories'

# the fun begins here...
def create_folder(title, name):
    os.makedirs(os.path.join(FOLDER, title, name))

# get Cateogry names
def get_category_names():
    # look for article tag
    category = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.TAG_NAME, 'article'))
        )
    # get category title and textcontent of a tags
    # title = category.find_element_by_tag_name('h2').get_attribute('textContent')
    if EC.presence_of_element_located((By.CSS_SELECTOR, 'p.-pvs -phm -m')):
        title = category.find_element_by_css_selector('p.-pvs -phm -m')
    elements = category.find_elements_by_tag_name('a')
    categories = [a.get_attribute('textContent') for a in elements]
    for i in categories: create_folder(title, i)
    return elements, categories

# get sub categories and open them up
def get_sub_categories():
    elements, categories = get_category_names()
    category_links = [e.get_attribute('href') for e in elements]
    for link in category_links:
        driver.execute_script(f"window.open('{link}')")
        time.sleep(2)

# switch into the different windows 
def window_switching():
    for handle in driver.window_handles:
        if handle != driver.window_handles[0]:
            driver.switch_to_window(handle)
            get_sub_categories()

def get_products():

if __name__ == "__main__":
    try:
        get_sub_categories()
