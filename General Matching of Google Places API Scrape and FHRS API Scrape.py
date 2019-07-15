#!/usr/bin/env python
# coding: utf-8

import csv
import pandas as pd

dfh1=pd.read_csv('Your first Google ratings results of the region.csv')
#dfh2=pd.read_csv('Your second Google ratings results of the region.csv')
#dfh3=pd.read_csv('Your third Google ratings results of the region.csv')
dfh=pd.concat([dfh1,dfh2,dfh3],ignore_index=True)

dfg=pd.read_csv('Your hygiene ratings results of the region.csv')
dfg.set_index('Business Type ID',inplace=True)
dfg=dfg.loc[['input integers that you are interested in(see read me for more information)']]
dfg.reset_index(inplace=True)

dfh.drop('Unnamed: 0',axis=1,inplace= True)
dfh.drop_duplicates(inplace=True)
dfh.reset_index(inplace=True)
dfh.drop('index',axis=1,inplace=True)

df1=dfh.fillna('0')
df1=df1[df1['Address']!='0']
df2=dfg.fillna('0')
df2=df2[df2['Address']!='0']

adddf1=df1['Address']
adddf2=df2['Address']
addit=[]
for i in adddf1:
    addit.append(i.replace('Rd','Road'))
adddf1=addit
df1['Address']=adddf1

c=[]
d=[]
address=[]

latitude=[]
longitude=[]

name=[]
GoogleRating=[]
HygieneRating=[]
pricelevel = []
BusinessName=[]
for r in adddf1:
    a=r.split(',')[0]
    for j in adddf2:
        if a in j:
            c=df1.index[df1['Address']==r]
            d=df2.index[df2['Address']==j]
            if len(c) is not 1:
                if len(d) is not 1:
                    for ii in c:
                        for jj in d:
                            if abs(float(df1.loc[ii,'Latitude'])-float(df2.loc[jj,'Latitude']))<0.01:
                                if abs(float(df1.loc[ii,'Longitude'])-float(df2.loc[jj,'Longitude']))<0.01:
                                    address.append(r)
                                    latitude.append(df1.loc[ii,'Latitude'])
                                    longitude.append(df1.loc[ii,'Longitude'])
                                    name.append(df1.loc[ii,'Name'])
                                    GoogleRating.append(df1.loc[ii,'Rating'])
                                    pricelevel.append(df1.loc[ii,'Price Level'])
                                    HygieneRating.append(df2.loc[jj,'FHRS Rating'])
                                    BusinessName.append(df2.loc[jj,'Business Name'])


                else:
                    for ii in c:
                            if abs(float(df1.loc[ii,'Latitude'])-float(df2.loc[d[0],'Latitude']))<0.01:
                                if abs(df1.loc[ii,'Longitude']-float(df2.loc[d[0],'Longitude']))<0.01:
                                    address.append(r)
                                    latitude.append(df1.loc[ii]['Latitude'])
                                    longitude.append(df1.loc[ii]['Longitude'])
                                    name.append(df1.loc[ii]['Name'])
                                    GoogleRating.append(df1.loc[ii]['Rating'])
                                    pricelevel.append(df1.loc[ii]['Price Level'])
                                    HygieneRating.append(df2.loc[d[0]]['FHRS Rating'])
                                    BusinessName.append(df2.loc[d[0],'Business Name'])


            elif len(d) is not 1:
                for jj in d:
                    if abs(float(df1.loc[c[0],'Latitude'])-float(df2.loc[jj,'Latitude']))<0.01:
                        if abs(float(df1.loc[c[0],'Longitude'])-float(df2.loc[jj,'Longitude']))<0.01:
                            address.append(r)
                            latitude.append(df1.loc[c[0]]['Latitude'])
                            longitude.append(df1.loc[c[0]]['Longitude'])
                            name.append(df1.loc[c[0]]['Name'])
                            GoogleRating.append(df1.loc[c[0]]['Rating'])
                            pricelevel.append(df1.loc[c[0]]['Price Level'])
                            HygieneRating.append(df2.loc[jj]['FHRS Rating'])
                            BusinessName.append(df2.loc[jj,'Business Name'])


            else:
                if abs(float(df1.loc[c[0],'Latitude'])-float(df2.loc[d[0],'Latitude']))<0.01:
                    if abs(float(df1.loc[c[0],'Longitude'])-float(df2.loc[d[0],'Longitude']))<0.01:
                        address.append(r)
                        latitude.append(df1.loc[c[0]]['Latitude'])
                        longitude.append(df1.loc[c[0]]['Longitude'])
                        name.append(df1.loc[c[0]]['Name'])
                        GoogleRating.append(df1.loc[c[0]]['Rating'])
                        pricelevel.append(df1.loc[c[0]]['Price Level'])
                        HygieneRating.append(df2.loc[d[0]]['FHRS Rating'])
                        BusinessName.append(df2.loc[d[0],'Business Name'])

dfnew=pd.DataFrame({'Latitude':latitude,'Longitude':longitude,'Address':address,'Business Name':BusinessName,'Name':name,'Google Rating':GoogleRating,'Price Level':pricelevel,'Hygiene Rating':HygieneRating})
dfnew.drop_duplicates(inplace=True)
dfnew.reset_index(inplace=True)
dfnew.drop('index',axis=1,inplace=True)

indexes=[]
for i in range(0,len(dfnew)):
    b=dfnew.loc[i,'Business Name'].lower()
    a=dfnew.loc[i,'Name'].lower()
    c=a.split()
    try:
        c.remove('the')
    except:
        pass
    try:
        c.remove('restaurant')
    except:
        pass
    try:
        c.remove('&')
    except:
        pass
    for r in c:
        if r in b:
            logic=True
            break
        else:
            logic=False
    if logic==False:
        indexes.append(i)
dfnew.drop(indexes,inplace=True)
dfnew.reset_index(inplace=True)
dfnew.drop('index',axis=1,inplace=True)

dfnew.to_csv('Your_FileName.csv')





