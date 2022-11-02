import csv

def main():
    # name=input("Name? ")
    # house=input("House? ")
  
    #print(f"Saving.. {name}")
    #append_content_to_file("names.txt", name)
    
    #names = read_file("names.txt")
    #print(names)

    # create a dictionary with key value pairs
    # student = {"name":name, "house":house}
    # append_dict_to_file("houses.txt", student)

    #students = read_dict_from_file("houses.txt")

    # Read from a csv file using csv module
    students = read_file_csv("Hogwarts.csv")

    print(students)
 

  
def append_content_to_file(fname, content):
    with open(fname, "a") as file:
        file.write(f"{content}\n")

def append_dict_to_file(fname, content):
    print(f"Appending {content} to {fname}")
    with open(fname, "a") as file:
        file.write(f"{content['name']},{content['house']}\n")


def read_file(fname):
    ''' Return a list of each line'''
    names=[]
    with open(fname) as file:
        for line in file:
            names.append(line.strip())
    return names

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

def read_file_csv(fname):
    ''' Using csv module, return a list of dictionaries (object notation) by auto unpacking each line
    Jordan, Bulls -> {"name": "Jordan", "team":"Bulls"}    
    '''
    print(f"Reading from csv file: {fname} ...")

    students = []
    with open(fname) as file:
        reader = csv.DictReader(file)   # when we iterate over reader, each row will be of type dict.
        for row in reader: 
            # if we know csv column names in first row, unpack column names (keys) directly   
            # Create a dict (object notation) from each line and append to a list.
            students.append({"name":row['name'], "home":row['home']})

    return students
            


if __name__ == '__main__':
    main()

