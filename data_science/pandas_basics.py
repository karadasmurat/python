# See pandas_demo.ipynb

# pandas is a Python package providing fast, flexible, and expressive data structures
# designed to make working with “relational” or “labeled” data both easy and intuitive.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Apply the default theme
sns.set_theme()


def construction():
    # Manually build DataFrame
    # Option 1 -
    # data, as a list of lists - each item in the list is a list representing a ROW
    country_codes = pd.DataFrame(
        [[90, 'Turkey', 'Ankara'], [44, 'United Kingdom', 'London'], [
            1, 'United States', 'Washington'], [81, 'Japan', 'Tokyo'], [86, 'China', 'Beijing']],
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
    emails = ['bo@example.com', 'gr@example.com',
              'jo@example.com', 'je@example.com', 'sm@example.com']
    usernames = ['booker12', 'grey07', 'johnson81', 'jenkins46', 'smith79']

    # A dictionary where keys are the "column names" and values are the lists:
    users_dict = {'LastName': lastnames,
                  'Email': emails, 'Username': usernames}

    # Create a DataFrame from a Python dict:
    # df = pd.DataFrame({'col1':[], 'col2':[]})
    df_users = pd.DataFrame(users_dict)
    print(df_users)


def data_import():
    # import a csv file, as a DataFrame
    # The DataFrame is one of Pandas' most important data structures.
    # df = pd.read_csv("data_science/data/brics.csv", index_col=0)
    df = pd.read_csv("data_science/data/employees_200.csv", index_col=0)

    print(df)
    print(df.info())          # summary of the dataframe
    print(df.shape)           # a tuple representing dimensionality
    print(df.head(2))         # The first n rows
    print(df.tail(2))         # The last n rows

    return df


def preprocess_data():

    print("Preprocess Data")
    print("---------------")

    # NaN values
    df = pd.DataFrame({
        "age": [5, 6, np.nan],
        "born":
        [pd.NaT,
         pd.Timestamp('1939-05-27'),
         pd.Timestamp('1940-04-25')],
        "name": ['Alfred', 'Batman', ''],
        "toy": [None, 'Batmobile', 'Joker']
    })

    print(df)
    # Return a boolean same-sized object indicating if the values are NA
    print(df.isna())

    df = pd.DataFrame({
        'name': [
            "Harry",
            "Ron",
            "Hermione",
            "Harry",
            "Ron",
            "Malfoy",
        ],
        'house': [
            "Gryffindor", "Gryffindor", "Gryffindor", "Gryffindor",
            "Gryffindor", "Slytherin"
        ]
    })

    print(df)
    print(df.shape)  # (6, 2)

    # Return boolean Series denoting duplicate rows.
    print(df.duplicated())

    # Filtering duplicates with Boolean Series
    print(df[df.duplicated()])

    # drop duplicates
    df_dropped = df.drop_duplicates()
    print(df_dropped)
    print(df_dropped.shape)  # (4, 2)


def explore_data():

    print("Explore Data")
    print("------------")

    df = pd.read_csv("data_science/data/car_sales.csv")
    print(df.info())

    # DataFrame.describe()
    print(df.describe())

    # Series.describe()
    print(df["mileage"].describe())

    # Series.describe(): NOMIAL Categories
    print(df["transmission"].describe())

    # Unique value counts
    print(df["transmission"].value_counts())

    # Count the number of males using value_counts()
    automatic_count = df['transmission'].value_counts()['automatic']
    print("Count of automatic transmissions:", automatic_count)

    # Histogram of a nominal column
    plt.hist(df["transmission"])
    plt.title("Transmission Type")
    plt.show()

    print(df.head())

    df = data_import()

    # aggregation on a column
    mean_salary = df["salary"].mean()
    median_salary = df["salary"].median()
    min_salary = df["salary"].min()
    max_salary = df["salary"].max()
    std_salary = df["salary"].std()

    print("Salary statistics: ")
    print(f"Mean : {mean_salary}")
    print(f"Standart Deviation : {std_salary}")
    print(f"Median : {median_salary}")
    print(f"Min : {min_salary}")
    print(f"Max : {max_salary}")


def chart_basics():
    # data = {"Temperature_Celcius": [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2], "IceCream_Revenue": [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]}
    # df = pd.DataFrame(data)

    # note that worldbank data contains ".." as missing values
    df = pd.read_csv(
        "data_science/data/worldbank_gdp_population_area.csv", na_values='..')

    # Drop outlier rows
    i = df[df["Country"] == "India"].index
    df = df.drop(i)

    i = df[df["Country"] == "China"].index
    df = df.drop(i)

    i = df[df["Country"] == "United States"].index
    df = df.drop(i)

    # df = df.fillna({"GDP": 0})
    # df["LandArea"] = df['LandArea'] / 1000
    # df["LandArea"] = df['LandArea'].round(2)
    # df.to_csv("data_science/data/worldbank_gdp_population_area.csv", index=False)

    print(df.info())

    print(df[df["CountryCode"] == "VGB"])

    # Scatter plot requires numeric columns for the x and y axes.
    plt.scatter(x=df["Population"], y=df["GDP"], s=df["LandArea"], alpha=0.5)

    plt.show()


def correlation():

    # Sample dataset - age vs price of cars
    data = {"age": [1, 3, 5, 7, 9], "price": [10000, 9000, 7000, 5000, 3000]}
    df = pd.DataFrame(data)

    # Calculate correlation coefficient
    # Note that np.corrcoef returns the correlation matrix: a two-dimensional array with the correlation coefficients.
    c1 = df["age"].corr(df["price"])
    c2 = df["price"].corr(df["age"])

    print("Correlation coefficient (pearson):", c1, c2)  # -0.9938

    c3 = df["age"].corr(df["price"], method="spearman")

    print("Correlation coefficient (spearman):", c3)  # -0.9999


def main():

    print("Pandas Basics")
    print("-------------")

    # construction()
    # df = data_import()

    # Single Column Access as a Series
    # Pandas Series format is not very convenient to print out.
    # col_name = "SALARY"
    # print(df[col_name])

    # Single Row Access
    # row_index = 0
    # print(df.iloc[row_index])

    # Data Preprocessing
    # preprocess_data()

    # Exploratory Data Analysis
    explore_data()

    # chart_basics()

    # correlation()

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
    # for index, row in brics.iterrows():
    #    print(index, row['capital'])


if __name__ == "__main__":
    main()
