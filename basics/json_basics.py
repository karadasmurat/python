"""
Python has a built-in package called json, which can be used to work with JSON data.

If you have a Python object, you can convert it into a JSON string by using the "json.dumps()" method.
If you have a JSON string, you can parse it by using the "json.loads()" method. The result is a Python dictionary.
"""

import json


def main():
    # Sample JSON string:
    # (key and value strings enclosed in double quotes, by convention)
    jordan_json_str = '{"name": "Michael", "surname": "Jordan", "hobbies": ["basketball", "acting"]}'
    print(f"{jordan_json_str=}")

    # Parse a JSON string, and return a Python dictionary:
    mj_dict = json.loads(jordan_json_str)
    print(f"{mj_dict=}")

    # a Python object (dict) to string:
    x = { "name": "John", "age": 30, "city": "New York"}
    print(f"{x=}")
    x_json_str = json.dumps(x)  # string
    print(f"{x_json_str=}")
    x_json_str_pretty = json.dumps(x, sort_keys=True, indent=4)
    print(f"{x_json_str_pretty=}")

    # Note that x and x_json_str prints almost the same (x_json_str prints keys with double quotes)

    # create a dict from user input
    make = input("Make? ")
    model = input("Model? ")
    year = input("Year? ")

    car = {"make": make, "model": model, "year": year}

    # save into a file
    # with open("data/cars.json", "a") as file:
    #     json.dump(car, file)
    write_to_file_json("data/cars.json", car)

    data_dict = read_file_json("users.json")
    print("Type:", type(data_dict))

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
