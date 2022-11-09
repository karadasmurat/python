# High level data manipulation built on NumPy

import pandas as pd

# Manually build DataFrame
# Option 1 - data, as a list of lists - each member list representing a row
country_codes = pd.DataFrame(
    [[90, 'Turkey', 'Ankara'], [44, 'United Kingdom', 'London'], [1, 'United States', 'Washington']], 
    index=['TR', 'UK', 'US'], 
    columns=['code', 'name', 'capital']
    )
'''
    code            name     capital
TR    90          Turkey      Ankara
UK    44  United Kingdom      London
US     1   United States  Washington
'''
print(country_codes)

# Option 2 - 
# A seperate list representing each column
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
# A dictionary where keys are the "column names" and values are the lists:
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }

# Create a DataFrame from a Python dict:
cars = pd.DataFrame(cars_dict)
# print(cars)

# import a csv file, as a DataFrame
# The DataFrame is one of Pandas' most important data structures. 
brics = pd.read_csv("data/brics.csv", index_col=0)
print(brics)

# slice to get the first observation(row) from the DataFrame
print(brics[0:1])

# Column Access - Square brackets [[]]
print(brics[['country', 'capital']])

# With DataFrame.loc and iloc you can do practically any data selection operation on DataFrames
# Row Access - loc (label-based)
print(brics.loc[['RU', "CH"]])

# Column Acccess: loc (label-based)
print(brics.loc[:, ['country', 'capital']])

# Row & Column Access
print(brics.loc[['RU', 'CH'], ['country', 'capital']])