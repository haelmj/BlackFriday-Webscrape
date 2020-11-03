"""
author: Michael Ndon
title: Blackfridayscrape
subject-website: jumia.com

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import csv
import time

# set path to chromedriver and initialize chrome webdriver
PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# load web page; set window handle to 0; set storage folder
driver.get('https://www.jumia.com.ng/mlp-black-friday/?rating=4-5')
black_deals_window = driver.window_handles[0]
FOLDER = './categories'

# the fun begins here...
# get Cateogry names
def category_name():
    category = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Category'))
        )
    elements = category.find_elements_by_tag_name('a')
    categories = [a.get_attribute('textContent') for a in elements]
    yield categories

print(next(category_name()))
