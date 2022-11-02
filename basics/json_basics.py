import json


def main():
    # assign a JSON string to a variable
    # (property name enclosed in double quotes)
    mj_str = '{"name": "Michael", "surname": "Jordan", "hobbies": ["basketball", "acting"]}'
    print(f"{mj_str=}")

    # json.loads() return a dictionary from JSON string
    mj_dict = json.loads(mj_str)
    print(f"{mj_dict=}")

    # mj_dict and mj_str prints almost the same
    # mj_str prints mj_dict in between quotation marks ! Well, it is a string :)

    # create a dict from user input
    make = input("Make? ")
    model = input("Model? ")
    year = input("Year? ")

    car = {"make": make, "model": model, "year": year}

    # save into a file
    with open("cars.json", "w") as file:
        json.dump(car, file)

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


def read_file_json(fname):
    ''' Using json module, return file contents as a dictionary '''
    print(f"Reading from json file: {fname} ...")
    with open(fname) as file:
        data = json.load(file)  # whole contents of file as a dict type.

    return data


if __name__ == "__main__":
    main()
