#!/usr/bin/env python
# coding: utf-8

import json
import requests
import xmltodict
import pandas as pd
import csv
import os


DATA_DIR=os.path.join(os.getcwd(),"Food Hygiene Ratings by Food Standard Agency ")

if not os.path.isdir(DATA_DIR):
   os.makedirs(DATA_DIR)


fhrsurl ="http://ratings.food.gov.uk/OpenDataFiles/FHRS5%xen-GB.xml"
a=list(range(1,34))
b = ["%02d" % n for n in a]
results=[]


for i in b:
    url = fhrsurl.replace("%x",str(i))
    response= requests.get(url)
    response.encoding= 'utf-8'
    JsonD = json.dumps(response.text)
    JsonL = json.loads(JsonD)
    mydict = xmltodict.parse(JsonL)
    a = list(list(mydict.items()))[0][1]['EstablishmentCollection']['EstablishmentDetail']
    locaut=a[0]['LocalAuthorityName']

    for i in list(range(0,len(a))):
        result = []
        add=[]
         
        try:
            result.append(a[i]['BusinessName'])
        except:
            result.append("No Business Name")
            
        try:
            result.append(a[i]['BusinessTypeID'])
        except:
            result.append("No Business type ID")

        try:
            result.append(a[i]['BusinessType'])
        except:
            result.append("No Business Type")

        try:
            result.append(a[i]["RatingValue"])
        except:
            result.append("No Score for FHRS Rating")

        try:
            result.append(a[i]["Geocode"]["Latitude"])
        except:
            result.append("NaN")
            
        try:
            result.append(a[i]["Geocode"]["Longitude"])
        except:
            result.append("NaN")
            
        try:
            AL1=(a[i]["AddressLine1"])
        except:
            AL1=''
        if AL1 is not '':
            AL1=AL1+','
            
        try:
            AL2=(a[i]["AddressLine2"])
        except:
            AL2=''
        if AL2 is not '':
            AL2=AL2+','
            
        try:
            AL3=(a[i]["AddressLine3"])
        except:
            AL3=''
        if AL3 is not '':
            AL3=AL3+','
            
        try:
            AL4=(a[i]["AddressLine4"])
        except:
            AL4=''
        if AL4 is not '':
            AL4=AL4+','
            
        add=AL1+AL2+AL3+AL4
        add=add[:-1]
        result.append(add)    
        results.append(result)

with open(os.path.join(DATA_DIR, "Hygiene Ratings Data "+".csv"), "w",newline="", encoding="utf-8") as fout:
    csv_writer = csv.writer(fout)
    csv_writer.writerow(['Business Name','Business Type ID','Business Type','FHRS Rating','Latitude','Longitude','Address'])
   
    for r in results:
        csv_writer.writerow(r)

