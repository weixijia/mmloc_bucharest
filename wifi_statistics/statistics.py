# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 13:44:07 2020

@author: weixijia
"""

import pandas as pd
import numpy as np
import glob

# Edinburgh = pd.read_csv('edin.csv',dtype=np.float64, header=0)
# Bucharest = pd.read_csv('bucha.csv',dtype=np.float64)

# Bucharest_WiFi = Bucharest.iloc[:,3::]
# Edinburgh_WiFi = Edinburgh.iloc[:,18::]

# time_bucha=(Bucharest.iloc[-1]['t']-Bucharest.iloc[0]['t'])/1000/60 # format in minutes
# time_edin=(Edinburgh.iloc[-1][0]-Edinburgh.iloc[0][0])/1000/60 # format in minutes

# AP_bucha=Bucharest_WiFi.shape[1]
# AP_edin=Edinburgh_WiFi.shape[1]

# sum_RSS_bucha=Bucharest_WiFi.sum(axis=1) # ap0 starts from column 3
# sum_RSS_edin=Edinburgh_WiFi.sum(axis=1) # ap0 starts from column 18

# diversity_bucha=sum_RSS_bucha.unique().shape[0]/sum_RSS_bucha.shape[0] #diversity upon all the samples, calculate the percentage pf how many unique sum RSS values over all WiFi samples
# diversity_edin=sum_RSS_edin.unique().shape[0]/sum_RSS_edin.shape[0]

# RichInfo_bucha=(Bucharest_WiFi != 0).sum(axis=1)/AP_bucha # For the number of non-zeros in each row divided by total num of ap for each sample
# RichInfo_edin=(Edinburgh_WiFi != 0).sum(axis=1)/AP_edin

# RSSperAP_bucha=(Bucharest_WiFi != 0).sum(axis=0)/Bucharest_WiFi.shape[0] # get each AP RSS values among all samples (check how may non-zero values of each AP among each column)
# RSSperAP_edin=(Edinburgh_WiFi != 0).sum(axis=0)/Edinburgh_WiFi.shape[0]

# print('Bucharest Rich info: '+str(RSSperAP_bucha.mean() *100)+' %')
# print('Edinburgh Rich info: '+str(RSSperAP_edin.mean() *100)+' %') 

Bucharest = pd.read_csv('scenario1-1.csv',dtype=np.float64)
Bucharest_WiFi = Bucharest.iloc[:,3:-1]
Analyse_per_ap=Bucharest_WiFi.copy()
Analyse_per_loc=Bucharest_WiFi.copy()
Analyse_per_ap.replace(0, np.nan, inplace=True)
statistic=Analyse_per_ap.describe().T.assign(apear_rate = Analyse_per_ap.apply(lambda x : 1-(x.isnull().sum() / len(Bucharest_WiFi))))
# print(Bucharest_WiFi.describe())
#print(statistic)

weak_ap = statistic[(statistic['75%']<0.166667) | (statistic['apear_rate']<0.3)].index.tolist() #0.166667 represent normalised -90dBm | missing ratio 70% represents more than 0.7 of each ap are missing values

#describe(exclude=['Unnamed: 0','t','delta_t','match'])

# b=Bucharest_WiFi.columns[['ap0']:['ap43']]

# df.columns.difference(['b'])

# c=(df.columns.difference(['b'].tolist())
#Bucharest_WiFi.groupby(Bucharest_WiFi.columns.tolist()).value_counts().to_frame('count')

count=Analyse_per_loc.groupby(Analyse_per_loc.columns.tolist()).size()
print(count)
# print(Bucharest_WiFi.groupby(Bucharest_WiFi.columns.tolist()).size())

# bbb=Bucharest_WiFi.groupby(Bucharest_WiFi.columns.tolist())

ccc=Analyse_per_loc.groupby(Analyse_per_loc.columns.tolist()).size().reset_index().\
    rename(columns={0:'records'})