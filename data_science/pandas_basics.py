# pandas is a Python package providing fast, flexible, and expressive data structures
# designed to make working with “relational” or “labeled” data both easy and intuitive.

import pandas as pd

# Manually build DataFrame
# Option 1 -
# data, as a list of lists - each item in the list is a list representing a ROW
country_codes = pd.DataFrame(
    [[90, 'Turkey', 'Ankara'], [44, 'United Kingdom', 'London'], [1, 'United States', 'Washington'], [81, 'Japan', 'Tokyo'], [86, 'China', 'Beijing']],
    index=['TR', 'UK', 'US', 'JP', 'CN'],
    columns=['code', 'name', 'capital']
)
'''
    code            name     capital
TR    90          Turkey      Ankara
UK    44  United Kingdom      London
US     1   United States  Washington
JP    81           Japan       Tokyo
CN    86           China     Beijing
'''
print(country_codes)

# Option 2 -
# A seperate list representing each COLUMN
# person = {
#     "name"      : "value",
#     "lastname"  : "value"
#     }
# people = {
#     "name"      : ["value1","value2"],
#     "lastname"  : ["value1","value2"]
#     }
lastnames = ['Booker', 'Grey', 'Johnson', 'Jenkins', 'Smith']
emails = ['bo@example.com', 'gr@example.com', 'jo@example.com', 'je@example.com', 'sm@example.com']
usernames = ['booker12', 'grey07', 'johnson81', 'jenkins46', 'smith79']

# A dictionary where keys are the "column names" and values are the lists:
users_dict = {'LastName': lastnames, 'Email': emails, 'Username': usernames}

# Create a DataFrame from a Python dict:
# df = pd.DataFrame({'col1':[], 'col2':[]})
df_users = pd.DataFrame(users_dict)
print(df_users)

'''
{
    'LastName':['Booker', 'Grey', 'Johnson', 'Jenkins', 'Smith'],
    'Email': ['bo@example.com', 'gr@example.com', 'jo@example.com', 'je@example.com', 'sm@example.com'],
    'Username': ['booker12', 'grey07', 'johnson81', 'jenkins46', 'smith79']
}

  LastName           Email   Username
0   Booker  bo@example.com   booker12
1     Grey  gr@example.com     grey07
2  Johnson  jo@example.com  johnson81
3  Jenkins  je@example.com  jenkins46
4    Smith  sm@example.com    smith79
'''

# import a csv file, as a DataFrame
# The DataFrame is one of Pandas' most important data structures.
brics = pd.read_csv("data/brics.csv", index_col=0)

# print(brics.info())             # summary of the dataframe
# print(brics.shape)              # a tuple representing dimensionality
print(brics)
# print(brics.head(2))          # The first n rows
# print(brics.tail(2))          # The last n rows

# Single Column Access as a Series
# Pandas Series format is not very convenient to print out.
# print(brics['capital'])

# slice to get the first observation(row) from the DataFrame
# print(brics[0:1])

# Column Access as a DataFrame- Square brackets [[]]
# print(brics[['country', 'capital']])

# With DataFrame.loc and iloc you can do practically any data selection operation on DataFrames
# Row Access - loc (label-based)
# print(brics.loc[['RU', "CH"]])

# Column Acccess: loc (label-based)
# print(brics.loc[:, ['country', 'capital']])

# Row & Column Access
# print(brics.loc[['RU', 'CH'], ['country', 'capital']])

# Iterate over DataFrame rows as (index, Series) pairs.
for index, row in brics.iterrows():
    print(index, row['capital'])
