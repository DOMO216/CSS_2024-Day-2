#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:49:24 2024

@author: thabangmolefi
"""
import pandas as pd

file = pd.read_csv('iris.csv')

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

file1 = pd.read_csv(url)

column_names = ['sepal_length','sepal_width','petal_length','petal_width','class']

file2 = pd.read_csv(url,header=None,names=column_names)

file3 = pd.read_excel('residentdoctors.xlsx')

file4 = pd.read_json('student_data.json')

df = pd.read_csv('Accelerometer_data.csv', names=['date_time','x','y','z'])


"""
Working with file 3
"""

print(file3.info())

"""
Data columns (total 9 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
dtypes: float64(5), int64(2), object(2)
memory usage: 11.4+ KB
None
"""


file3['LOWER_AGE'] = file3["AGEDIST"].str.extract('(\d+)-')
"""
The code above illustrates how we took the lower ages from the AGEDIST column 
to create a new column with just the lower numbers of the age intervals
"""

file3['LOWER_AGE'] = file3['LOWER_AGE'].astype(int)

"""
Working with dates
"""

df1 =  pd.read_csv('time_series_data.csv',index_col=0)

print(df1.info())

df1['Date'] = pd.to_datetime(df1['Date'], format = '%d-%m-%Y')

"""
df1['Date'] = pd.to_datetime(df1['Date'], format = '%d-%m-%Y')
*** ValueError: time data "2020-01-01" doesn't match format "%d-%m-%Y", at position 0. You might want to try:
    - passing `format` if your strings have a consistent format;
    - passing `format='ISO8601'` if your strings are all ISO8601 but not necessarily in exactly the same format;
    - passing `format='mixed'`, and the format will be inferred for each element individually. You might want to use `dayfirst` alongside this.
"""

"""
Introduce a new column
"""

df1['Date'] = pd.to_datetime(df1['Date'])

df1['Year'] = df1['Date'].dt.year

df1['Month'] = df1['Date'].dt.month

df1['Day'] = df1['Date'].dt.day

"""
Working with NANs and Wrong formats
"""

df2 = pd.read_csv("patient_data_dates.csv",index_col=0)

avg_cal = df2['Calories'].mean()

df2['Calories'].fillna(avg_cal, inplace = True)

df2.dropna(inplace=True)

df2['Duration'] = df2['Duration'].replace([450], 50)

"""
Applying Data Transormations

"""

file = pd.read_csv('iris.csv')

col_names = file.columns

file['sepal_length_sq'] = file['sepal_length']**2

file['sepal_length_sq_2'] = file['sepal_length'].apply(lambda x:x**2)

grouped = file.groupby('class')

mean_square_values = grouped['sepal_length_sq'].mean()

print(mean_square_values)


######################################

df3 = pd.read_csv('person_split1.csv')
df4 = pd.read_csv('person_split2.csv')

DF = pd.concat([df3,df4], ignore_index=True)

#####################################

df5 = pd.read_csv('person_education.csv')
df6 = pd.read_csv('person_work.csv')

"""
Inner join
"""

DF_merge_inner = pd.merge(df5, df6, on = 'id')

####################################

print(file)

file['class'] = file['class'].str.replace("iris", "")

file = file[file['sepal_length'] > 5]

file = file[file['class'] == 'virginica']


#################################

url1 = "https://raw.githubusercontent.com/alexandrehsd/Predicting-Pulsar-Stars/master/pulsar_stars.csv" 

df7 = pd.read_csv(url1)
 print(df7)






