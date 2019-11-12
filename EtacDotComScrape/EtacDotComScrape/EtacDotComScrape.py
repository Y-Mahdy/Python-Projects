from selenium import webdriver
import time
from collections import OrderedDict
import datetime
import os
browser = webdriver.Chrome()
file = open("products.csv", 'r+')
url = 'https://www.etac.com/products'
browser.get(url)
all_orders = browser.find_elements_by_xpath('//li[@class = "category-listItem"]//a')
for order in all_orders: 
    newurl =  order.get_attribute("href")
    browser.get(newurl)
    category_name=browser.find_element_by_xpath('//h1').text
    all_products = browser.find_elements_by_xpath('//li[@class = "leftmenu-sublistItem"]//a')
    for product in all_products: 
        producturl = product.get_attribute("href")
        browser.get(producturl)
        productname = "\"" + browser.find_element_by_xpath('//h1').text + "\""
        all_options = browser.find_elements_by_xpath('//table[@class="product-facts"]//tbody//tr')
        Productoptions = ''
        for options in all_options: 
            Productoptions += options.find_elements_by_xpath('.//td')[0].text + ": " + options.find_elements_by_xpath('.//td')[1].text + ","
        #price=
        CategoryName = "\""+ category_name + "\""
        imagepath='https://www.etac.com'+ browser.find_element_by_xpath('//ul[@class="slides"]//li//a').get_attribute("href")
        Longdescription= "\"" + browser.find_element_by_xpath('//div[@class="product-info"]').text + "\""
        file.seek(0, os.SEEK_END)
        file.write(productname + "," + producturl + "," + imagepath + "," + CategoryName + "," + Longdescription +"," + "\"" + Productoptions + "\"" ) 