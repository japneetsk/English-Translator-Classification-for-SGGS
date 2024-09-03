# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:14:04 2020

@author: Japneet
"""

import os
import sys
import os.path
from os import path

from urllib.parse import urlencode
from urllib.request import Request, urlopen
import sys

import pandas as pd
from pandas.io.json import json_normalize
import json

#filepath = r'Siri Guru Granth - English Translation UTF8 Sample.txt'
#filepathjson = r'Sri Guru Granth Sahib Ji\0001.json'

#with open(filepathjson, encoding = "utf8") as f:
#  data = json.load(f)
#
#print(data)


# Function to convert json files to csv
def convertjsontocsv(filepathjson,filenum):

    with open(filepathjson, encoding = "utf8") as f:
      data = json.load(f)
    
    email = 'craigslistjap@gmail.com'
#    json = data
    filename = filenum+'.csv'
        
    sys.stdout.write('Status: 200 OK\n')
    sys.stdout.write('Content-Type: text/csv; charset=utf-8\n')
    sys.stdout.write('Content-Disposition: attachment; filename=' + filename + '\n\n')
    
    url = 'https://json-csv.com/api/getcsv'
    post_fields = {'email': email, 'json': data}
    request = Request(url, urlencode(post_fields).encode())
    csv1 = urlopen(request).read().decode()
    
    csvfilepath = r'csv_output_files'+"\\"+filename

    with open(file = csvfilepath, mode = 'w', encoding = 'utf8') as file:
        for line in csv1.split('\r\n'):
            file.write(line)
            file.write('\n')

###
#cnt = 1429
#strcnt = str(cnt)
#strcnt.rjust(4,"0")


directory = r'Sri Guru Granth Sahib Ji'
cnt = 1
while cnt < 1431 :
    strcnt = str(cnt)
    jsonfilenum = strcnt.rjust(4,"0")
    fullpath = directory + "\\" + jsonfilenum +'.json'
    if path.exists(fullpath) == False:
        print("Does not exist: "+ strcnt)
    else:
        convertjsontocsv(fullpath,jsonfilenum)
    cnt += 1