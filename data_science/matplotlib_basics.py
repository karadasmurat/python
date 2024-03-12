from matplotlib import pyplot as plt
import csv


def plot_line():

    # Sample data
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    # create a line chart, years on x-axis, gdp on y-axis
    # plt.plot(years, gdp)
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

    # add a title
    plt.title("Nominal GDP")
    # add a label to the y-axis
    plt.ylabel("Billions of $")

    # Display the plot
    plt.show()


def plot_bar():
    movies = ["Annie Hall", "Ben-Hur",
              "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]

    # plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
    plt.bar(range(len(movies)), num_oscars)

    plt.title("My Favorite Movies")  # add a title
    plt.ylabel("# of Academy Awards")  # label the y-axis
    # label x-axis with movie names at bar centers
    plt.xticks(range(len(movies)), movies)

    # Display the plot
    plt.show()


def REFACTOR():
    year = [1950, 1970, 1990, 2010]
    world_population = [2.519, 3.692, 5.263, 6.972]

    plt.plot(year, world_population)      # line

    plt.scatter(year, world_population)   # scatter
    # Add axis labels and title
    plt.xlabel("Year")
    plt.ylabel("World population [billions]")
    # Ticks
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7], ["zero", "one",
                                          "two", "three", "four", "five", "six", "seven"])

    # Show and clean up plot
    # plt.show()
    # plt.clf()

    # A HISTOGRAM is an approximate representation of the distribution of numerical data.
    # To construct a histogram, the first step is to "bin" (or "bucket") the range of values—that is,
    # divide the entire range of values into a series of intervals—
    # and then count how many values fall into each interval.

    grades = ['A', 'B', 'B', 'C', 'C', 'C', 'D', 'A',
              'B', 'A', 'B', 'B', 'B', 'D', 'F', 'C', 'B', 'C']
    plt.hist(grades)    # histogram

    # Show and clean up plot
    # plt.show()
    plt.clf()

    filename = "data/population_tr.csv"

    print(f"Reading from csv file: {filename} ...")

    cities = []
    with open(filename) as file:
        # when we iterate over reader, each row will be of type dict.
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            # append each row (dict) to a list.
            cities.append(row)

    data = cities[0]
    # format integers - Total 64_729_501 84_680_273
    print(f"{data['Province']} {int(data['2000']):_} {int(data['2021']):_}")

    keys = [int(key) for key in data if key != "Province"]
    values = [int(data[key]) for key in data if key != "Province"]
    # print(values)

    plt.scatter(keys, values)
    plt.title("TR Population")
    plt.xticks([2000, 2015, 2030], [2000, 2015, 2030])
    plt.yticks([60000000, 70000000, 80000000, 90000000],
               ["60M", "70M", "80M", "90M"])
    plt.grid(True)
    plt.show()
