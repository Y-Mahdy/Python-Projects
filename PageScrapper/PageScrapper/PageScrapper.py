from bs4 import BeautifulSoup, SoupStrainer
import time
from collections import OrderedDict
import datetime
import os
import urllib
from selenium import webdriver
import csv
from tkinter import filedialog
from tkinter import *

def GetDetails(csvFile, no):
    Test = ''
    ToEnd = 0
    try:
        website = ''
        Address = ''
        twitter = ''
        instagram = ''
        Email = ''
        while(True):
            try:
                driver.find_element_by_xpath('//div[@data-key="tab_about"]').click()
                break
            except:
                try:
                    driver.find_element_by_xpath('//a[@class = "_42ft _4jy0 _4jy6 _4jy2 selected _51sy"]')
                    ToEnd = 1
                    break
                except:
                    test = ''
                try:
                    driver.find_element_by_xpath('//div[@class = "_62up"]').click()
                except:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #check if the page is loaded
        if ToEnd == 0:
            while(True):
                try:
                    driver.find_element_by_xpath('//div[@class = "_5aj7 _2pib _2pi5 _qs0"]')
                    break
                except:
                    time.sleep(1)
            try:
                Address           = "\""  + driver.find_element_by_xpath('//div[@class = "_5aj7 _3-8j _20ud"]//div[@class="_4bl9"]//div').text.replace("\"", "\"\"") + "\"" 
            except:
                Address = ''
            try:
               checkCollection = driver.find_elements_by_xpath('//div[@class = "_5aj7 _3-8j"]')
               for checkItem in checkCollection:
                   try:
                       checkItem.find_element_by_xpath('./div[@class = "_4bl7 _3-90 _a8s"]//img').get_attribute("src")
                       if checkItem.find_element_by_xpath('./div[@class = "_4bl7 _3-90 _a8s"]//img').get_attribute("src") == 'https://static.xx.fbcdn.net/rsrc.php/v3/y_/r/8TRfTVHth97.png':
                           instagram = "\"" + checkItem.find_element_by_xpath('./div[@class = "_4bl9"]').text.replace("\"", "\"\"") + "\""
                       elif checkItem.find_element_by_xpath('./div[@class = "_4bl7 _3-90 _a8s"]//img').get_attribute("src") == 'https://static.xx.fbcdn.net/rsrc.php/v3/yV/r/EaDvTjOwxIV.png':
                           website = "\"" + checkItem.find_element_by_xpath('./div[@class = "_4bl9"]').text.replace("\"", "\"\"") + "\""
                       elif checkItem.find_element_by_xpath('./div[@class = "_4bl7 _3-90 _a8s"]//img').get_attribute("src") == 'https://static.xx.fbcdn.net/rsrc.php/v3/yc/r/84ZlKNyIrsW.png':
                           twitter = "\"" + checkItem.find_element_by_xpath('./div[@class = "_4bl9"]').text.replace("\"", "\"\"") + "\""
                       elif checkItem.find_element_by_xpath('./div[@class = "_4bl7 _3-90 _a8s"]//img').get_attribute("src") == 'https://static.xx.fbcdn.net/rsrc.php/v3/yy/r/vKDzW_MdhyP.png':
                           Email = "\"" + checkItem.find_element_by_xpath('./div[@class = "_4bl9"]').text.replace("\"", "\"\"")  + "\"" 
                   except:
                       test = ''
            except:
                test = ''
            FBPage = ''
            FBPage = "\"" + driver.current_url.replace("\"", "\"\"") + "\""
            finalText = FBPage + ',' + Address + ',' + website + ',' + twitter + ',' + instagram + ',' + Email + "\n"
            csvFile.write(finalText)
            print('Item # '+str(no)+' has been finished')
    except:
      test = ''
# Text File path
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = {"csv ?csv"})
txtpath = root.filename
root.destroy()
# Text File Output
PathColl = txtpath.split(os.sep)
txtOutput = PathColl[len(PathColl) -1].replace('.csv','') + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace('-','').replace(':','').replace(' ', '') + '.csv'
with open(txtpath, newline='') as csvfile:
    data = list(csv.reader(csvfile))
no = 0
driver = webdriver.Chrome()
csvFile = open(txtOutput, 'w+')
columnTitleRow = "Facebook Page Link, Address, Website, Twitter, Instagram, Email\n"
csvFile.write(columnTitleRow)
ListOfCompletedLinks = []
item = 0
for row in data:
    if no > 0:
        dataCollection = row[2].split(';')
        for link in dataCollection:
            if link and link.strip():
                if link not in ListOfCompletedLinks:
                    item = item + 1
                    driver.get(link)
                    GetDetails(csvFile, item)
                    ListOfCompletedLinks.append(link)
                    time.sleep(3)
    no = no + 1
csvFile.close()
os.startfile(txtOutput)
driver.close()