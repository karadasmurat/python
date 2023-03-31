"""
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

    "t" - Text - Default value. Text mode
    "b" - Binary - Binary mode (e.g. images)

In simple terms, we use file.read() and file.write().

Python 2.5 introduced the WITH statement. 
The with statement is used with context managers to enforce conditions that occur before and after a block is executed. 
The open function also serves as a context manager 
"to ensure that a file is opened before the block is entered and that it is closed when the block is exited."

The csv module implements classes to read and write tabular data in CSV format. 
The csv module's reader and writer objects read and write sequences. 
Programmers can also read and write data in dictionary form using the DictReader and DictWriter classes.

"""


# Python has a built in module that allows you to work with JSON data.
import json
import csv
import os
import pandas as pd


# import domain         # domain.Car()
from domain import Car  # Car()
from domain import HogwartsStudent
from domain import HogwartsHouse
import util

FILENAME = "data/names.txt"
FILENAME_CSV = "data/cars.csv"
FILENAME_CSV_WITH_HEADER = "data/grades.csv"


def main():

    path_basics()

    # write_to_file_older_approach()

    # Write
    # print("Please provide details to save: ")
    # name = input("Name? ")
    # write_to_file(FILENAME, name)
    # print(f"Saved: {name} to {FILENAME}.")

    # Read the entire contents of the file:
    # names = read_file_at_once(FILENAME)
    # print(names)

    # names = read_file(FILENAME)
    # print(names)

    # Read csv file using csv reader
    # read_file_csv_reader(FILENAME_CSV)     # FileNotFoundError if No such file or directory

    # Read csv file using csv DictReader(), and construct class instances (each line will be a dict)
    # with open("data/houses.csv") as csvfile:
    #     reader = csv.DictReader(csvfile)    # returned object is an iterator - when we iterate over reader, each row will be of type dict.
    #     for row in reader:                  # each row is a dictionary
    #         house = HogwartsHouse.from_dict(row)
    #         print(house)

    # Read csv file using csv DictReader()
    # houses = read_file_csv_dictreader("data/houses.csv")
    # print("List of students from csv file: ", students)

    # Read csv using pandas
    read_file_csv_pandas(FILENAME_CSV_WITH_HEADER)

    # Write a class instance to a file as a line - each attribute seperated by comma:
    # name = input("Enter name: ")
    # house = input("Enter house: ")
    # student = HogwartsStudent(name, house)

    # filepath = "data/houses.txt"
    # print(f"Appending {student} to {filepath}")
    # with open(filepath, "a") as file:
    #     file.write(student.to_csv() + "\n")

    # Serialize object as a JSON formatted stream to a file
    make = input("Make? ")
    model = input("Model? ")
    year = input("Year? ")

    car = Car(make, model, year)
    print(car.to_JSON_str())    # dictionary to string: json.dumps(dict)
    write_to_file_json("data/cars.json", car.to_dict())


def write_to_file_older_approach():
    file = open("data/countries.txt", "w")   # relative path from which python interpreter executed!
    # i.e. run "$ python files.py" under basisc folder
    # "$ python basics/files.py" gives different relative paths!
    file.write("Italy\n")
    file.write("Germany\n")
    file.close()


def write_to_file(fname, content, mode="a"):
    with open(fname, mode) as file:
        file.write(f"{content}\n")


def write_to_file_json(fname, content, mode="w"):
    with open(fname, mode) as file:
        json.dump(content, file)  # Serialize obj as a JSON formatted stream to fp


def read_file_at_once(fname):
    ''' Return the contents of the file.'''

    with open(fname) as file:   # open() opens file and returns a stream
        # The read() method returns the specified number of bytes from the file.
        # Default is -1 which means the whole file.
        # it’s your problem if the file is twice as large as your machine’s memory.
        data = file.read()

    return data


def read_file(fname, mode="r"):
    ''' Return a list where items are the lines of the file.'''

    if mode == "r":     # Reading text file
        names = []
        with open(fname) as file:   # open() opens file and returns a stream
            # For reading lines from a file, you can loop over the file object.
            # This is memory efficient, fast, and leads to simple code:
            for line in file:
                names.append(line.strip())
        return names

    elif mode == "rb":    # Reading binary file
        pass


# The csv module implements classes to read and write tabular data in CSV format.
# The csv module’s reader and writer objects read and write sequences.
# Programmers can also read and write data in dictionary form using the DictReader and DictWriter classes.
def read_file_csv_reader(fname):
    print(f"Using csv.reader() to read file: {fname} ...")
    with open(fname) as csvfile:
        reader = csv.reader(csvfile)    # returned object is an iterator - when we iterate over reader, each row will be of type dict.
        for row in reader:              # each row is a list of strings:
            print(row)                  # i.e. Volkswagen,T-ROC,2023  ->  ['Volkswagen', 'T-ROC', '2023']


def read_file_csv_dictreader(fname, delimiter=','):
    ''' Using csv module, return a list of dictionaries (object notation) by auto unpacking each line

    name,team
    Jordan,Bulls     -->   {"name": "Jordan", "team":"Bulls"} 

    '''
    print(f"Using csv.DictReader() to read file: {fname} ...")

    students = []
    with open(fname) as file:
        reader = csv.DictReader(file, delimiter=delimiter)  # returned object is an iterator - when we iterate over reader, each row will be of type dict.
        for row in reader:
            print(row)                                # each row is a dictionary
            # append each row (dict) to a list.
            students.append(row)

            # print(type(row) ,row)    # <class 'dict'> {'Lastname': 'Alfalfa', 'Firstname': 'Aloysius', 'SSN': '123-45-6789', 'Test1': '40.0', 'Test2': '90.0', 'Test3': '100.0', 'Test4': '83.0', 'Final': '49.0', 'Grade': 'D-'}
            # The first row of csv is containing column names - column names are the keys.
            # To print a cell, row['column_name']
            # print(row['Lastname'])

    return students


def read_file_csv_custom(fname):
    ''' Return a list of dictionaries (object notation) by splitting each line and assigning to related keys.
    Jordan, Bulls -> {"name": "Jordan", "team":"Bulls"}    
    '''
    print(f"Reading from file: {fname} ...")

    students = []
    with open(fname) as file:
        for row in file:    # each row contains a comma separated values
            # Create a dict (object notation) from each line and append to a list.
            name, house = row.strip().split(',')
            students.append({"name": name, "house": house})

    return students


def read_file_csv_pandas(fname):
    print(f"Using pandas to read file: {fname} ...")

    df = pd.read_csv(fname)
    print(df)


def parse_JSON_str(json_str):
    '''return a dictionary from JSON string'''
    return json.loads(json_str)


def path_basics():

    util.printTitle("Path Basics")
    # absolute path of this script's directory: /Users/mk/dev/python/basics
    print("Absolute path of this script's directory: ", os.getcwd())

    # absolute path of this script: /Users/mk/dev/python/basics/modules_and_packages.py
    current_path = os.path.abspath(__file__)
    print("Current path of this script: ", current_path)


if __name__ == '__main__':
    main()
