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

Python 2.5 introduced the WITH statement. 
The with statement is used with context managers to enforce conditions that occur before and after a block is executed. 
The open function also serves as a context manager to ensure that 
a file is opened before the block is entered and that it is closed when the block is exited.
"""



# Python has a built in module that allows you to work with JSON data. 
import json

import csv

FILENAME = "data/names.txt"
FILENAME_CSV = "data/grades.csv"

def main():

    # write_to_file_older_approach()
    
    # Write
    # print("Please provide details to save: ")
    # name = input("Name? ")
    # write_to_file(FILENAME, name)
    # print(f"Saved: {name} to {FILENAME}.")
    
    # Read
    # names = read_file(FILENAME)
    # print(names)

    # Write a dictionary formatted info to a file in a csv format:
    # name = input("Enter name: ")
    # house = input("Enter house: ")
    # student = {"name":name, "house":house}
    # append_dict_to_file("data/houses.txt", student)

    # Read from a csv formatted file, each line into a dictionary
    # students = get_dict_from_csv_formatted_file("data/houses.txt")
    # print(students)

    # Read from a csv file with header, each line into a dictionary, using csv module
    # students = read_csv(FILENAME_CSV)
    # for s in students:  # list of dictionaries
    #     print(s)              

    # first dict in the list, value for the key 'Project' = first row, Project column
    # print(type(students[0]['Project']), students[0]['Project'])     # <class 'str'> 40.0 


    # Serialize object as a JSON formatted stream to a file
    make = input("Make? ")
    model = input("Model? ")
    year = input("Year? ")

    car = {"make": make, "model": model, "year": year}
    write_to_file_json("data/cars.json", car)


def write_to_file_older_approach():
    file = open("data/countries.txt","w")   # relative path from which python interpreter executed! 
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
        json.dump(content, file) # Serialize obj as a JSON formatted stream to fp

def append_dict_to_file(fname, content):
    print(f"Appending {content} to {fname}")
    with open(fname, "a") as file:
        file.write(f"{content['name']},{content['house']}\n")


def read_file(fname, mode="r"):
    ''' Return a list where items are the lines of the file.'''

    if "r" == mode:     # Reading text file
        names=[]
        with open(fname) as file:
            # In Python, it is easy to iterate over the lines in a file
            for line in file:
                names.append(line.strip())
        return names
    
    elif "r" == "rb":    # Reading binary file
        pass

def get_dict_from_csv_formatted_file(fname):
    ''' Return a list of dictionaries (object notation) by splitting each line and assigning to related keys.
    Jordan, Bulls -> {"name": "Jordan", "team":"Bulls"}    
    '''
    print(f"Reading from file: {fname} ...")

    students = []
    with open(fname) as file:
        for row in file:    # each row contains a comma separated values
            # Create a dict (object notation) from each line and append to a list.
            name, house = row.strip().split(',')
            students.append({"name":name, "house":house})

    return students

def read_csv(fname, delimiter=','):
    ''' Using csv module, return a list of dictionaries (object notation) by auto unpacking each line
    
    name,team
    Jordan,Bulls     -->   {"name": "Jordan", "team":"Bulls"} 

    '''
    print(f"Reading from csv file: {fname} ...")

    students = []
    with open(fname) as file:
        reader = csv.DictReader(file, delimiter=delimiter)   # when we iterate over reader, each row will be of type dict.
        for row in reader: 
            # print(type(row) ,row)    # <class 'dict'> {'Lastname': 'Alfalfa', 'Firstname': 'Aloysius', 'SSN': '123-45-6789', 'Test1': '40.0', 'Test2': '90.0', 'Test3': '100.0', 'Test4': '83.0', 'Final': '49.0', 'Grade': 'D-'}
            # The first row of csv is containing column names - column names are the keys.
            # To print a cell, row['column_name']
            # print(row['Lastname'])
            
            # append each row (dict) to a list.
            students.append(row)

    return students

def parse_JSON_str(json_str):
    '''return a dictionary from JSON string'''
    return json.loads(json_str)
            


if __name__ == '__main__':
    main()

