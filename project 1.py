# -*- coding: utf-8 -*-
'''
Created on Mon Nov  9 11:18:33 2015

@author: graemestclair
'''


import pandas as pd

fn = '/Users/graemestclair/Documents/python/banklist.xlsx'
data = pd.read_excel(fn, sheetname=0)
df = pd.read_excel(fn, sheetname=0, index = data['CERT'])


#1
print('\nThe column names are: \n', df.columns.values)

year = pd.to_datetime(df['Closing Date'])
year = year.order()
count = year.count()

print('There were', count, 'bank closures between', year.iloc[0],'and', year.iloc[(count-1)])
year = df['Closing Date'].groupby(data['Closing Date'].map(lambda x: x.year)).count()
print(year)


#2 -- 
state = df['ST'].groupby(df['ST']).count()

print('\n\nBank Closures By State (Decending Order)\n\n', state.order(ascending = False))


print('\n\nStates that had no bank closures:\n\n')

states = ['AK','AL','AR','AZ','CA','CO','CT','DE','FL',
'GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME',
'MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV',
'NY','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VA','VT','WA','WI','WV','WY']
states.sort()
frame = df
frame = frame.drop_duplicates(subset=[frame.columns.values[2]])
frame = frame[[2]]
statelist = frame.values
statelist.sort()
for index in range(len(statelist)):
    if statelist[index] in states:
        states.remove(statelist[index])

print(states)


#3 -- 
city = df['City'].groupby(df['City']).count()

print('\n\nBanks Closures By City (Decending Order)\n\n', city.order(ascending = False))

#4 -- 

acquirer = df['Acquiring Institution'].groupby(df['Acquiring Institution']).count()

print('\n\nAcquiring Institution by number of Acquisitions (Decending Order)\n\n', acquirer.order(ascending = False))