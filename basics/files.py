# Python 2.5 introduced the WITH statement. 
# The with statement is used with context managers to enforce conditions that occur before and after a block is executed. 
# The open function also serves as a context manager to ensure that 
# a file is opened before the block is entered and that it is closed when the block is exited.




# Python has a built in module that allows you to work with JSON data. 
import json

import csv

FILENAME = "names.txt"
filename_csv = "data/grades.csv"

def main():
    
    # print("Please provide details to save: ")
    # name = input("Name? ")
  
    # print(f"Saving {name} to {FILENAME} ..")
    # write_to_file(FILENAME, name)
    
    # names = read_file("names.txt")
    #print(names)

    # create a dictionary with key value pairs
    # student = {"name":name, "house":house}
    # append_dict_to_file("houses.txt", student)

    #students = read_dict_from_file("houses.txt")

    # Read from a csv file using csv module
    students = read_csv(filename_csv)
    # print(students)               # list of dictionaries

    # first dict in the list, value for the key 'Project' = first row, Project column
    print(type(students[0]['Project']), students[0]['Project'])     # <class 'str'> 40.0 

  
def write_to_file(fname, content, mode="a"):
    with open(fname, mode) as file:
        file.write(f"{content}\n")

def append_dict_to_file(fname, content):
    print(f"Appending {content} to {fname}")
    with open(fname, "a") as file:
        file.write(f"{content['name']},{content['house']}\n")


def read_file(fname, mode="r"):
    ''' Return a list of each line'''
    if "r" == mode:     # Reading text file
        names=[]
        with open(fname) as file:
            # In Python, it is easy to iterate over the lines in a file
            for line in file:
                names.append(line.strip())
        return names
    elif "r" == "rb":    # Reading binary file
        pass

def read_dict_from_file(fname):
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

