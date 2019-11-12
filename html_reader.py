#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:44:29 2019

@author: FCRA
"""

#
#   
#print filter_mult    #List of all Job Titles of people in NYC gov state
#

#REDAING SECOND DATASET
#list pages of services
#see how many people go there
#see analytics of people going there
#see if same user accesses the pages? 
#see user goes form one page to the other

#
#df = pd.read_csv('NYC.gov_Web_Analytics.csv', delimiter = ',')
#serv_webpages = ["https://portal.311.nyc.gov/category/?id=311-121",     #Benefits & Support
#                 "https://portal.311.nyc.gov/category/?id=311-4",       #Culture & Recreation
#                 "https://portal.311.nyc.gov/category/?id=311-7",       #Environment
#                 "https://portal.311.nyc.gov/category/?id=311-10",      #Health
#                 "https://portal.311.nyc.gov/category/?id=311-13",      #Pets and WIldlife
#                 "https://portal.311.nyc.gov/category/?id=311-16",      #Sidewalks, streets & highways
#                 ]  #stupid to do it by hand



def get_info():
    f = open("services_html/NYCser_html_raw.txt","r")
    readlines = f.readlines()
    f.close()
    
    fltr = []
    urls = []
    sernam = []
    serdescr = []
    
    #cleaning
    for i in readlines:
        j = i.replace(" ", "").split("\r")
        fltr.append(j)
        
    #slicing 
    for j in range(len(fltr[0])):
        if fltr[0][j][:2]=='<a': 
            
                #formatting urls
                url = fltr[0][j].replace(fltr[0][j][0:9],
                          'https://portal.311.nyc.gov/').replace('">', '')
                urls.append(url)
                sernam.append(fltr[0][j+1])
                serdescr.append(fltr[0][j+3])
                
    return urls , sernam, serdescr


#urls = get_info()[0]
#sernam = get_info()[1]
#serdescr = get_info()[2]
#
#print urls, sernam




    




