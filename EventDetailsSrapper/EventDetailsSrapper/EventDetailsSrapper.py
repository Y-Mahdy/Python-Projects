from bs4 import BeautifulSoup, SoupStrainer
import time
from collections import OrderedDict
import datetime
import os
import urllib
from selenium import webdriver
import sys

from tkinter import filedialog
from tkinter import *

def GetDetails(csvFile, item):
    TicketLink = ''
    LocationAddress = ''
    LocationName = ''
    Test = ''
    Went = ''
    Share = ''
    Interested = ''
    Going = ''
    try:
        EventLink = ''
        EventLink = "\"" + driver.current_url.replace("\"", "\"\"") + "\""
        if EventLink not in CollectionOfCompletedLinks:
            Title           = "\""  + driver.find_element_by_xpath('//h1[@id = "seo_h1_tag"]').text.replace("\"", "\"\"") + "\"" 
            HostedByTagA    = driver.find_elements_by_xpath('//div[@data-testid="event_permalink_feature_line"]//a')
            hostByText = ''
            for hostbyElement in HostedByTagA:
                hostByText  += hostbyElement.get_attribute("href") + ';'
            hostByText = "\""  + hostByText[:-1].replace("\"", "\"\"") + "\"" 
            EventTime       =  "\""  + driver.find_element_by_xpath('//li[@id="event_time_info"]').find_element_by_xpath('//div[@class = "_2ycp _5xhk"]').text.replace("\"", "\"\"") + "\"" 
            try:
                TotalLocNode        = driver.find_elements_by_xpath('//li[@class = "_3xd0 _3slj"]//div//table//tbody//tr')
                for node in TotalLocNode:
                    try:
                        if 'pin\n' in node.text:
                            try:
                                node.find_element_by_xpath('.//a[@class = "_5xhk"]')
                                LocationName = "\""  + node.find_element_by_xpath('.//a[@class = "_5xhk"]').text.replace("\"", "\"\"") +"\"" 
                                node.find_element_by_xpath('.//div[@class = "_5xhp fsm fwn fcg"]')
                                LocationAddress = "\""  + node.find_element_by_xpath('.//div[@class = "_5xhp fsm fwn fcg"]').text.replace("\"", "\"\"") + "\""
                                break
                            except:
                                LocationAddress = ''
                                LocationName = ''
                            try:
                                node.find_element_by_xpath('.//span[@class = "_5xhk"]')
                                LocationAddress = "\""  + node.find_element_by_xpath('.//span[@class = "_5xhk"]').text.replace("\"", "\"\"") +"\"" 
                                LocationName = ''
                                break
                            except:
                                LocationAddress = ''
                    except:
                        Location = ''
            except:
                Location = ''
            try:
                TicketLink      = "\""  + driver.find_element_by_xpath('//li[@data-testid="event_ticket_link"]//a').get_attribute("href").replace("\"", "\"\"") + "\"" 
            except:
                TicketLink = ''
            try:
                #13 Going · 364 Interested 77 went · 188 interested
                All = driver.find_element_by_class_name('_5z74')
                if All:
                    AllSplit = All.text.split('·')
                    for stItem in AllSplit:
                        if 'interested' in stItem.lower():
                            Interested      = "\""  + stItem.replace('interested','').strip() + "\""
                        elif 'going' in stItem.lower():
                            Going      = "\""  + stItem.replace('going','').strip() + "\""
                        elif 'went' in stItem.lower():
                            Went      = "\""  + stItem.replace('went','').strip() + "\""
                        elif 'share' in stItem.lower():
                            Share      = "\""  + stItem.replace('share','').strip() + "\""
            except:
               Test = ''
            DetailsTagsList     = driver.find_elements_by_xpath('//ul[@class = "_63er"]//li')
            Tags = ''
            for detailsTagelement in DetailsTagsList:
                Tags = detailsTagelement.text + ';'
            Tags = "\""  + Tags[:-1].replace("\"", "\"\"") + "\"" 
            CollectionOfCompletedLinks.append(EventLink)
            finalText = EventLink + ',' + Title + ',' + hostByText + ',' + EventTime + ',' + LocationName + ','+ LocationAddress + ',' + TicketLink + ',' + Tags +',' + Interested +','+ Going + ',' + Went + ',' + Share + "\n"
            print (' >> Item # ' + str(item) + ' has been scrapped')
            csvFile.write(finalText)
    except Exception as e:
       print("Error in Item " + str(e))
# Text File path
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = {"txt ?txt"})
txtpath = root.filename
root.destroy()

# Event Links
# Text File Output
PathColl = txtpath.split(os.sep)
txtOutput = PathColl[len(PathColl) -1].replace('.txt','') +'_1stOutput_Links_'+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace('-','').replace(':','').replace(' ', '') + '.csv'
try:
    file = open(txtOutput, 'w+')
except IOError:
    file = open(txtOutput, 'w+')
CollectionOfPaths1 = []
print ('(Extracting links) Task from Text File is being processing .. ')
with open(txtpath, 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    for link in soup.find_all('a'):
        if link.has_attr('href') and '/events/' in link['href']: 
            if not ('www.facebook.com' + link['href'] in CollectionOfPaths1):
                file.writelines('www.facebook.com' + link['href'] + '\n')
                CollectionOfPaths1.append('www.facebook.com' + link['href'])
with open(txtOutput, 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
file.close()
f.close()
# Event Details
# Text File Output
txtOutput1 = PathColl[len(PathColl) -1].replace('.txt','')+'_2ndOutput_Details_' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace('-','').replace(':','').replace(' ', '') + '.csv'
CollectionOfPaths = []
print ('(Scraping Details from links) Task from CSV File is being processing .. ')
with open(txtOutput, 'r') as f:
    CollectionOfPaths = f.readlines()
f.close()
driver = webdriver.Chrome()
csvFile = open(txtOutput1, 'w+', encoding="utf-8")
columnTitleRow = "Event Link, Title, Hosted By, Event Time, Place Name, Location, Ticket Link, Tags, Interested, Going, Went, Share\n"
csvFile.write(columnTitleRow)
CollectionOfCompletedLinks = []
item = 0
for link in CollectionOfPaths:
    item = item + 1
    driver.get('http://' + link)
    GetDetails(csvFile, item)
    time.sleep(3)
csvFile.close()
os.startfile(txtOutput1)
driver.close()