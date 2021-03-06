"""
author: Michael Ndon
title: Blackfridayscrape
subject-website: jumia.com.ng
description: collates 4-5 star rated black friday deals from cheapest to highest by category

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
PATH = "./assets/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# load web page; set window handle to 0; set storage folder
driver.get(STARTPAGE)
black_deals_window = driver.window_handles[0]
FOLDER = 'categories'

# the fun begins here...
def create_folder(title):
    path = os.path.join(FOLDER, title)
    os.makedirs(path)
    return

# get Cateogry names
def get_category_names(tag):
    # look for article tag
    category = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.TAG_NAME, tag))
        )
    # get category title and textcontent of a tags
    elements = category.find_elements_by_tag_name('a')
    categories = [a.get_attribute('textContent') for a in elements]
    if driver.current_window_handle == driver.window_handles[0]:
        for i in categories:
            create_folder(i)
    
    return elements, categories

# get sub categories and open them up
def get_sub_categories():
    elements, categories = get_category_names('article')
    category_links = [e.get_attribute('href') for e in elements]
    for link in category_links:
        driver.execute_script(f"window.open('{link}')")
        time.sleep(2)
    return categories

# switch into the different windows 
def window_switching(handle):
    driver.switch_to.window(handle)
    sub_elements, sub_categories = get_category_names('article')
    return sub_elements, sub_categories        

# get products container
def get_products():
    products_list = driver.find_element_by_css_selector('section.card.-fh')
    products = products_list.find_elements_by_tag_name('article')
    return products

# retrieve information on any product passed in
def get_product_info(product):
    product_link = product.find_element_by_css_selector('a.core').get_attribute('href')
    link_button = f'=HYPERLINK("{product_link}", "view")'
    product_info = product.find_element_by_css_selector('div.info')
    product_name = product_info.find_element_by_tag_name('h3').get_attribute('textContent')
    new_price = product_info.find_element_by_css_selector('div.prc').get_attribute('textContent')
    try:
        normal_price = product_info.find_element_by_css_selector('div.s-prc-w > div.old').get_attribute('textContent')
    except:
        normal_price = 'No price deviation'
    try:
        product_rating = product_info.find_element_by_css_selector('div.rev > div.stars._s').get_attribute('textContent')
    except:
        product_rating = 'No rating'
    return product_name, new_price, normal_price, product_rating, link_button


if __name__ == "__main__":
    try:
        categories = get_sub_categories()
        # loop through each open window apart from the initial one
        j = -1
        for handle in driver.window_handles:
            if handle != driver.window_handles[0]:
                elements, subcategories = window_switching(handle)
                sub_links = [e.get_attribute('href') for e in elements]
                i = 0
                while i < len(subcategories):
                    for link in sub_links:
                        with open(f'{FOLDER}/{categories[j]}/{subcategories[i]}.csv', 'w', newline='', encoding='utf-8') as file:
                            file_writer = csv.writer(file)
                            file_writer.writerow(['Name', 'New Price', 'Old Price', 'Rating', 'URL'])
                            driver.execute_script(f"window.open('{link}')")
                            driver.switch_to.window(driver.window_handles[-1])
                            products = get_products()
                            for product in products:
                                name, new_price, old_price, rating, web_link = get_product_info(product)
                                file_writer.writerow([name, new_price, old_price, rating, web_link])
                            driver.close()
                            driver.switch_to.window(handle)
                            i += 1
                j -= 1
    except Exception as e:
       driver.close()
    finally:
        driver.quit()    