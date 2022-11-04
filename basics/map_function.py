# Processing Iterables Without a Loop
# Apply a transformation function to each item in an iterable and transform them into a new iterable.map()


def main():
    grades = [75, 90, 55, 80]
    new_grades = map(times2, grades)

    print(f"{grades=}")
    # In Python 2.x, map() returns a list. This behavior changed in Python 3.x. 
    # Now, map() returns a map object, 
    print(list(new_grades))

    str_nums = ["4", "18", "6", "5"]
    int_nums = map(int, str_nums)   # convert all the items in the list from a string to an integer
    print(f"{str_nums=}")
    print(list(int_nums))

    # A common pattern is to use a lambda function as the first argument. 
    numbers = [1, 2, 3, 4, 5]
    cube = map(lambda num: num ** 3, numbers)
    print(f"{numbers=}")
    print(list(cube))

def times2(arg):
    return 2 * arg

if __name__ == "__main__":
    main()