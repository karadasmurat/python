"""
Python has a built-in package called json, which can be used to work with JSON data.

The process of encoding JSON is usually called serialization. 
This term refers to the transformation of data into a "series of bytes" (hence serial) to be stored or transmitted across a network. 

if you have a dictionary, 
    * json.dump(dict) method for writing data to files. 
    * json.dumps() method (pronounced as “dump-s”) for writing to a Python string.


            --- serialization   -- to_dict()  -->               -- json.dumps(dict) -->
    OBJECT                                          DICTIONARY                            STRING
            <-- deserialization -- from_dict() --               <-- json.loads(str) --

    
* If you have a JSON string, you can parse it by using the "json.loads()" method. The result is a Python dictionary.



"""

import json
from domain import Author, Book
from domain import Car


def main():
    # Sample JSON string:
    # (key and value strings enclosed in double quotes, by convention)
    jordan_json_str = '{"name": "Michael", "surname": "Jordan", "hobbies": ["basketball", "acting"]}'
    print(f"{jordan_json_str=}")

    # Example 1: JSON string to dict
    # Parse a JSON string, and return a Python dictionary:
    mj_dict = json.loads(jordan_json_str)
    print(f"{mj_dict=}")


    # Example 2: JSON string to dict
    json_string = """
                {
                    "researcher": {
                        "name": "Ford Prefect",
                        "species": "Betelgeusian",
                        "relatives": [
                            {
                                "name": "Zaphod Beeblebrox",
                                "species": "Betelgeusian"
                            }
                        ]
                    }
                }
                """
    json_dict = json.loads(json_string)
    print("The first relative is:", json_dict['researcher']['relatives'][0]['name'])


    # Example 3: a Python object (dict) to string:
    person_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    print(f"{person_dict=}")
    person_json_str = json.dumps(person_dict)  # string
    print(f"{person_json_str=}")

    # Format
    x_json_str_pretty = json.dumps(person_dict, sort_keys=True, indent=4)
    print(f"{x_json_str_pretty=}")

    # Note that x and x_json_str prints almost the same (x_json_str prints keys with double quotes)

    # Serialize object as a JSON formatted stream to a file
    make = "Volkswagen" # input("Make? ")
    model = "T-ROC"     # input("Model? ")
    year = 2019         # input("Year? ")

    car = Car(make, model, year)
    print(car.to_JSON_str())    # dictionary to string: json.dumps(dict)
    write_to_file_json("data/cars.json", car.to_dict())


    # A class, which has an attribute of user defined type:
    author = Author("J. R. R. Tolkien")
    print(json.dumps(author.to_dict()))     # {"fullname": "J. R. R. Tolkien"}
    book = Book("Hobbit", author, "978-0261103344", ['fiction'])
    print(json.dumps(book.to_dict()))       # book -> dict -> str

    data_dict = read_file_json("users.json")
    print("Type:", type(data_dict))

    # Deserialization: From JSON formatted string to dictionary to Car object:
    # First, create a dict using json.loads(str), and then construct a Car object using this dictionary:
    car_json_str = '{"make": "Togg", "model": "T10X", "year": 2023}'
    my_car = Car.from_dict(json.loads(car_json_str)) 
    print("Object constructed from a JSON formatted string: ", my_car)

    # print() outputs a dict directly is a one line. To pretty print, use json.dumps()
    print(json.dumps(data_dict, indent=2))

    # filter a specific key, i.e second user's email
    print("The second users email: ", data_dict['users'][1]['email'])

    # iterate a list of dicts: [{},{},{}]
    for user in data_dict['users']:
        for phone in user['phones']:
            if phone['type'] == "mobile":
                print(user['email'], phone['number'])


def parse_JSON_str(json_str):
    '''return a dictionary from JSON string'''
    return json.loads(json_str)

def write_to_file_json(fname, content, mode="w"):
    with open(fname, mode) as file:
        json.dump(content, file) # Serialize obj as a JSON formatted stream to fp


def read_file_json(fname):
    ''' Using json module, return file contents as a dictionary '''
    print(f"Reading from json file: {fname} ...")
    with open(fname) as file:
        data = json.load(file)  # whole contents of file as a dict type.

    return data


if __name__ == "__main__":
    main()
