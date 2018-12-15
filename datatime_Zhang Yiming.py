# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:31:39 2018

@author: Zhang Yiming
"""

import pandas as pd
import datetime 

datetime_raw = pd.read_csv(r'D:\AFPD\Projects\My code\4. Datetime\data\ukpound_exchange.csv')
date_selected = pd.DataFrame(columns = list(datetime_raw))

#This part change all the string under column Date to datetime for future comparsion#
time_set = []
for i in datetime_raw['Date']:
    time_set.append(datetime.datetime.strptime(i, "%m/%d/%Y"))

#This part sort the dateframe so that it is now in ascending order# 
datetime_raw['Date'] = time_set
datetime_sorted = datetime_raw.sort_values(by = ['Date'])

#This part find all the date for month 1 - 12 expect for the last entry#   
for counter in range(len(time_set)-1):
    if time_set[counter].month < time_set[counter+1].month:
        tem = pd.DataFrame([datetime_sorted.loc[counter]], columns = list(datetime_raw))
        date_selected = pd.concat([date_selected, tem])
    elif time_set[counter].year < time_set[counter+1].year:
        tem = pd.DataFrame([datetime_sorted.loc[counter]], columns = list(datetime_raw))
        date_selected = pd.concat([date_selected, tem])

#This Part adds the last entry to the dataframe because in any situation the last entry is the lastest date#   
tem = pd.DataFrame([datetime_sorted.loc[len(time_set)-1]], columns = list(datetime_raw))
date_selected = pd.concat([date_selected, tem])
date_selected.reset_index(drop = True, inplace = True)


#This part set the time format of selected dataframe to original#
time_set_new = []
for i in date_selected['Date']:
    time_set_new.append(i.strftime("%m/%d/%Y"))
date_selected['Date'] = time_set_new

date_selected.to_csv(r'D:\AFPD\Projects\My code\4. Datetime\data\output.csv')

