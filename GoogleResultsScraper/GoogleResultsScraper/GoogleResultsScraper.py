import json
import time
import datetime
import os
import pprint

from collections import OrderedDict
from os import listdir
from os.path import isfile, join
from datetime import datetime
from googleapiclient.discovery import build

def getService():
    service = build("customsearch", "v1",developerKey="AIzaSyBVdgqlFfhw-iRe1C81ywf1tP63-A-VAME")
    return service
def main():
    queryCount = 0
    pageLimit = 12
    service = getService()
    startIndex = 1
    response = []
    f = open('Mandatory.txt', 'r')
    list_of_websites = f.readlines()
    f.close()
    app_full_path = os.path.realpath(__file__)
    application_path = os.path.dirname(app_full_path)
    mypath = application_path + '/Categories'
    category_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for website in list_of_websites:
        for file in category_files:
            fC = open(mypath + '/' + file, 'r')
            list_of_category = fC.readlines()
            fC.close()
            result_file_name = 'results_' + file
            try:
                fresults = open(result_file_name, 'r')
            except IOError:
                fresults = open(result_file_name, 'w')
            for category in list_of_category:
                nCountLinks = 0 
                search_txt = website + ' ' + category
                queryCount = queryCount + 1
                if (queryCount > 100):
                    time.sleep(86400)
                    queryCount = 0
                for nPage in range(0, pageLimit):
                    try:
                        response.append(service.cse().list(q=search_txt, cx = '012470540989129520900:zthepeihzlk',start=startIndex).execute())
                        startIndex = response[nPage].get("queries").get("nextPage")[0].get("startIndex")
                    except:
                        break
                with open(result_file_name, 'a') as the_file:
                    for x in response:
                        for y in x["items"]:
                            nCountLinks =nCountLinks + 1
                            the_file.write(y["link"] + '\n')
                            if (nCountLinks >100):
                                break
                        if (nCountLinks > 100):
                            break
                del response[:]
main()



