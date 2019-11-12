import time
import os
import selenium
from selenium import webdriver
import csv
def CheckChar(text):
    textTOarr = text.split(' ')
    for st in textTOarr:
        if st:
            if '\\uf0' in st:
                text.replace(st, '-')
    return text
print ('############## Task Started ###############')
webDriver =  webdriver.Chrome()
txtOutput = 'Output-essaybri.csv'
firstLine = "post_type,post_status,post_content,post_title\n"
csvFile = open(txtOutput, "a", encoding="utf-8")
#csvFile.write(firstLine)
writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
webDriver.get('http://essaybri.info/page/71/')
while True:
    try:
        for ArticleElement in webDriver.find_elements_by_xpath("//article"):
            post_title = ''
            try:
                post_title = ArticleElement.find_element_by_xpath('.//h2[@class = "entry-title"]').text.replace('"', '\"')
            except:
                pass
            post_content = CheckChar(ArticleElement.find_element_by_xpath('.//div[@class = "entry-content"]').text.replace('"', '\"').replace("&nbsp;", ""))
            writer.writerow(["post", "publish", post_content, post_title])
        time.sleep(2)
        webDriver.find_element_by_xpath('//a[@class = "next page-numbers"]').click()
            #csvFile.write("post, publish, " + "\"" + post_content+"\"" +"," + "\"" + post_title+"\"" + "")
    except Exception as e:
        print(str(e))
        break
csvFile.close()