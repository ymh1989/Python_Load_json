# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:57:07 2016

@author: Minhyun Yoo
"""

"""
Created on Tue May 10 10:35:12 2016

@author: Minhyun
"""

import requests
import pandas as pd
    
def dataframe2Excel(target, filename):
    writer = pd.ExcelWriter(filename, engine = 'xlsxwriter');
    target.to_excel(writer, sheet_name = 'Sheet1');
    writer.save();
    
def getjson(url):
    resp = requests.get(url);
    json = resp.json();
    data = pd.DataFrame(json);
    return data;
    
def isnumeric(s):
    # check s is numeric
    try:
        float(s);
        return True;
    except:
        return False;
        
def convertData(target):
    # if target is list
    if isinstance(target, list):
        # if all of elements are numeric
        if (all(isnumeric(x) for x in target)):
            return [float(x) for x in target];
        else:
            return target;
    # if target is not list
    else:
        if (isnumeric(target)):
            return float(target);
        else:
            return target;

def dataGather(ELSDATA, REFERDATA):
    newData = {};
    for i in range(len(ELSDATA)):
        for j in REFERDATA:
            newData[j] = convertData(ELSDATA[j][i]);
            
    return newData;
          
def makeUrl(issuer_name, 
            issue_date_start='2016-01-01', 
            issue_date_end='2016-01-05'):
    dic = {'issuer_name' : issuer_name,
           'issue_date_start' : issue_date_start,
           'issue_date_end' : issue_date_end};
    url = '???';     
    for x in dic:        
        url += (x + '=' + dic[x] + '&');
        
    url = url[:-1];
    return url;
                
url = makeUrl('???', '2016-01-01', '2016-05-01');

# get data from json
elsdata = getjson(url);
#key = elsdata.keys()

# write dataframe to excel file
dataframe2Excel(elsdata, 'result.xlsx')

refData = ['barrier', 'exer_freq_num', 
           'initvalue_eval_date','exer_date', 'expiry_eval_date', 
           'knock_in', 'underly_code', 'yield_rate'];

newData = dataGather(elsdata, refData);

