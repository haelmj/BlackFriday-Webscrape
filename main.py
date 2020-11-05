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
    path = os.path.join(FOLDER, title, name)
    os.makedirs(path)
    return path

# get Cateogry names
def get_category_names(tag):
    # look for article tag
    category = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.TAG_NAME, tag))
        )
    # get category title and textcontent of a tags
    try:
        title = category.find_element_by_tag_name('p').get_attribute('textContent')
    except:
        title = category.find_element_by_tag_name('h2').get_attribute('textContent')
    elements = category.find_elements_by_tag_name('a')
    categories = [a.get_attribute('textContent') for a in elements]
    for i in categories: path = create_folder(title, i)
    return elements, categories, path

# get sub categories and open them up
def get_sub_categories():
    elements, categories, path = get_category_names('article')
    category_links = [e.get_attribute('href') for e in elements]
    for link in category_links:
        driver.execute_script(f"window.open('{link}')")
        time.sleep(2)
    return categories

# switch into the different windows 
def window_switching(handle):
    driver.switch_to.window(handle)
    sub_elements, sub_categories, path = get_category_names('article')
    return sub_elements, sub_categories, path        

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
    normal_price = product_info.find_element_by_css_selector('div.s-prc-w div.old').get_attribute('textContent')
    product_rating = product_info.find_element_by_css_selector('div.rev div.stars._s').get_attribute('textContent')
    return product_name, new_price, normal_price, product_rating, link_button


if __name__ == "__main__":
    # try:
    get_sub_categories()
    for handle in driver.window_handles:
        if handle != driver.window_handles[0]:
            elements, categories, path = window_switching(handle)
            sub_links = [e.get_attribute('href') for e in elements]
            i = 0
            while i < len(categories):
                with open(f'{path}/{categories[i]}.csv', 'w', newline='', encoding='utf-8') as file:
                    file_writer = csv.writer(file)
                    file_writer.writerow(['Name', 'New Price', 'Old Price', 'Rating', 'URL'])
                    for link in sub_links:
                        driver.execute_script(f"window.open('{link}')")
                        driver.switch_to.window(driver.window_handles[-1])
                        products = get_products()
                        for product in products:
                            name, new_price, old_price, rating, web_link = get_product_info(product)
                            file_writer.writerow([name, new_price, old_price, rating, web_link])
                        driver.close()
                        driver.switch_to.window(handle)


    # except Exception as e:
    #    pass
    # finally:
    #     pass    