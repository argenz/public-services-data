#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:44:29 2019

@author: FCRA
"""

#READING Nyc website analytics
#list pages of services
#see how many people go there
#see analytics of people going there
#see if same user accesses the pages? 
#see user goes form one page to the other


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




    




