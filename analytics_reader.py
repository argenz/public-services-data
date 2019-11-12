#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:17:53 2019

@author: FCRA
"""


import pandas as pd
from html_reader import get_info

#getting info services on website
urls = get_info()[0]
sernam = get_info()[1]
serdescr = get_info()[2]

#getting website analytics 
df = pd.read_csv('NYC.gov_Web_Analytics.csv', delimiter = ',')
df = df.sort('Views', ascending=False)

#list of pages
pages = df.Page.tolist()



#PROBLEM: URLS IN THE ANALYTICS AND THE URLS LIST DO NOT MATCH
  

    