import matplotlib.pyplot as plt
import csv

year = [1950, 1970, 1990, 2010]
world_population = [2.519, 3.692, 5.263, 6.972]

plt.plot(year, world_population)      # line

plt.scatter(year, world_population)   # scatter
# Add axis labels and title
plt.xlabel("Year")
plt.ylabel("World population [billions]")
# Ticks
plt.yticks([0, 1, 2,3, 4, 5, 6, 7], ["zero", "one","two","three","four","five","six", "seven"])

# Show and clean up plot
# plt.show()
# plt.clf()

# A HISTOGRAM is an approximate representation of the distribution of numerical data.
# To construct a histogram, the first step is to "bin" (or "bucket") the range of values—that is, 
# divide the entire range of values into a series of intervals—
# and then count how many values fall into each interval. 

grades = ['A', 'B','B','C','C','C','D', 'A','B','A','B','B','B', 'D','F','C','B','C']
plt.hist(grades)    # histogram

# Show and clean up plot
# plt.show()
plt.clf()


filename = "data/population_tr.csv"

print(f"Reading from csv file: {filename} ...")

cities = []
with open(filename) as file:
    reader = csv.DictReader(file, delimiter=';')   # when we iterate over reader, each row will be of type dict.
    for row in reader:         
        # append each row (dict) to a list.
        cities.append(row)

data = cities[0]
print(f"{data['Province']} {int(data['2000']):_} {int(data['2021']):_}")  # format integers - Total 64_729_501 84_680_273

keys = [int(key) for key in data if key != "Province"]
values = [int(data[key]) for key in data if key != "Province"]
# print(values)

plt.scatter(keys, values)
plt.title("TR Population")
plt.xticks([2000, 2015, 2030], [2000, 2015, 2030])
plt.yticks([60000000, 70000000, 80000000, 90000000], ["60M", "70M", "80M", "90M"])
plt.grid(True)
plt.show()
