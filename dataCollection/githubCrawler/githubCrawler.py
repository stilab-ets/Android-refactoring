# coding: utf-8

import httplib2
import lxml
from lxml import etree
from lxml import html
import cssselect
import csv
import time
import math
import random
import pandas as pd
from datetime import datetime



dates=pd.date_range(start="#startDate",end="enDate")
dates_num_results = [979, 996, 994, 997, 999, 997, 983, 982, 996, 27]
dates_start_index = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


url_fragment_1 = 'https://github.com/search?p='
url_fragment_2 = '&q=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3D+in%3Areadme+created%3A'
url_fragment_3 = '&ref=searchresults&type=Repositories&utf8=%E2%9C%93'

for dates_index, current_date in enumerate(dates):
    print('Fetching for dates: ' + current_date)
    filePath = 'repos' + str(dates_index) + '.csv'

    page_index = dates_start_index[dates_index]
    to_page_index = math.ceil(dates_num_results[dates_index] / 10.0)

    print("Page index =", page_index, ", to_page=", to_page_index)

    rows = []
    append = True

    if(append):
        f = open(filePath, 'a')
    else:
        f = open(filePath, 'w')
        rows = [['Repository']]

    writer = csv.writer(f)

    while(page_index <= to_page_index):
        waitingTime = random.randrange(1, 10)
        url = url_fragment_1 + str(page_index) + url_fragment_2 + current_date + url_fragment_3
        response, payload = httplib2.Http().request(url)
        rootHtml = lxml.html.fromstring(payload)

        
        elements = rootHtml.cssselect('.repo-list h3 a') 

        rows = []
        if len(elements) != 0:
            for elem in elements:
                rows.append([elem.text])
            writer.writerows(rows)
            print('Fetched GitHub page: ' + str(page_index))
            page_index = page_index + 1
        else:
            print("Error while fetching page: " + str(page_index))
        print("Sleeping for " + str(waitingTime) + " seconds")
        time.sleep(waitingTime)
    print('Finished to fetch for dates: ' + current_date)
print('Finished fetching.')
