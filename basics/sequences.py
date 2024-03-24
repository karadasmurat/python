from domain.Wizard import Wizard


def basics():
    print("Sequence Basics")
    print("---------------")

    # list_basics()
    list_iteration()
    #  count_item()
    # set_basics()
    # tuple_basics()


def list_basics():
    print("List Basics")
    print("-----------")
    # There are two ways to create empty lists
    names = []
    surnames = list()

    # You can provide the values in between the square brackets, using the literal syntax:
    members = ['Fred', 'Charles']

    # List might contain items of different types, but usually the items all have the same type.
    hybridList = ["abc", 34, True, "male"]

    # Initialize a list with any size and a default value:
    frequencies = [0] * 10
    print("Frequencies initialized: ",
          frequencies)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # lists can have items with the same value:
    scores = [70, 85, 70, 90, 70]
    # number of times x appears in the list.
    print(f"#70: {scores.count(70)}")  # 3

    # The number of items in a container - the built-in function len() also applies to lists
    print("The number of scores:", len(scores))  # 5

    # Some other built-in functions for iterables: min, max, sum
    print(f"{max(scores)=}, {min(scores)=}, {sum(scores)=}")

    # You can generate a list of sequential numbers with range().
    # Note that range does not materialize the list, but rather gives you an iterable that will return those numbers when iterated over.
    # By passing the result into list you can see the numbers it would generate:
    # The “up to but not including” construct is more formally known as the "half-open interval" convention.
    nums = range(5)
    # <class 'range'> 5 [0, 1, 2, 3, 4]
    print(type(nums), len(nums), list(nums))

    even = list(range(0, 11, 2))
    print(even)  # [0, 2, 4, 6, 8, 10]

    # Accessing Elements
    squares = [1, 4, 9, 16, 25]
    # You can refer to an element by its index (subscript) - uses "zero-based indexing"
    print("squares[0]:", squares[0])
    # print("squares[100]:", squares[100])    # IndexError: list index out of range

    # Negative indexing means start from the end
    # -1 refers to the last item, -2 refers to the second last item etc.
    print(f"The last item: {squares[-1]}")  # 25

    # Insert item to the END of a list:
    squares.append(49)  # [1, 4, 9, 16, 25, 49]
    # squares = squares.append(49)  # WRONG!

    # INSERT an item at the specified index, and shift the rest:
    squares.insert(5, 36)  # [1, 4, 9, 16, 25, 36, 49]
    print(squares[5])  #

    # REMOVE value:
    # remove the first ocurrence of value: (Find and erase) raise ValueError if the value is not present
    members.remove('Charles')
    # members.remove('NotAMember')    # ValueError: list.remove(x): x not in list

    # The + operator concatenates lists:
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]

    # note that this is not an item by item addition! This is concatenation.
    d = a + b
    print(f"{a} + {b} is: {d}")  # [1, 2, 3] + [4, 5, 6] is: [1, 2, 3, 4, 5, 6]

    a += b
    print(f"{a=}")  # [1, 2, 3, 4, 5, 6]

    # Append elements from any other iterable to the current list:
    c.extend(b)  # Note that a is modified. [7, 8, 9, 4, 5, 6]
    print(f"Extended list: {c}")

    # list_of_objects()
    # list_as_stack()
    # list_as_queue()
    # process_list()
    score_frequencies()


def list_iteration():
    scores = [30, 40, 50, 60, 70, 80, 90]

    # v1
    for score in scores:
        print(score + 1)

    # v2 - enumeration
    # Sometimes you want to know the index of the element you are accessing in the list.
    # Python has a built-in function, enumerate, which returns a sequence of (i, value) tuples
    for i, v in enumerate(scores):
        print(i, v)


def tuple_basics():
    print("Tuple Basics")
    print("------------")

    # Using the tuple() built-in: tuple() or tuple(iterable)
    empty1 = tuple()
    print(type(empty1), empty1)  # <class 'tuple'> ()

    # Create a tuple from a list
    scores_list = [90, 80, 100]
    scores_tuple = tuple(scores_list)
    print(type(scores_tuple), scores_tuple)  # <class 'tuple'> (90, 80, 100)

    t = (1, 7, 2)
    print(type(t), t)  # <class 'tuple'> (1, 7, 2)

    # If there are multiple items separated by commas, then Python treats them as a tuple:
    t = (3,)
    print(type(t), t)  # <class 'tuple'> (3,)

    # Note that it is actually the comma which makes a tuple, not the optional parentheses
    x = 1, 2, 3
    print(type(x), x)  # <class 'tuple'> (1, 2, 3)

    # unpacking tuple
    x, y, z = (1, 2, 3)
    print(x + y + z)  # 6

    person = (1, "John", "Smith", "Male", "New York",
              "USA", "123-456-7890", "@johnsmith",)
    a, b, *rest = values

    # Tuples are often used to represent a record of data such as the row of a database query
    person = ('Matt', '123 North 456 East', 24)  # Heterogeneous


def list_of_objects():
    wizards = []
    wizards.append(Wizard("Harry", "Gryffindor"))
    wizards.append(Wizard("Ron", "Gryffindor"))
    wizards.append(Wizard("Draco", "Slytherin"))
    wizards.append(Wizard("Hermione", "Gryffindor"))

    print(wizards)

    wizards.sort(key=lambda w: w.name)
    print(wizards)


def list_as_stack():
    fruits = []
    fruits.append("apple")
    fruits.append("banana")
    fruits.append("cherry")

    print(fruits)  # ['apple', 'banana', 'cherry']

    last_fruit = fruits.pop()
    print(f"Last fruit: {last_fruit}")  # Last fruit: cherry
    print(fruits)  # ['apple', 'banana']


def list_as_queue():

    myqueue = []
    myqueue.append("first")
    myqueue.append("second")
    myqueue.append("third")

    print(myqueue)

    first_in = myqueue.pop(0)
    print(f"First in: {first_in}")
    print(myqueue)


def process_list():

    scores = [30, 40, 50, 60, 70, 80, 90]
    print(f"Scores: {scores}")

    # 10 points bonus to scores which are below 50

    # v1 list comprehension
    bonus_1 = [x + 10 for x in scores if x < 50]  # [40, 50]

    # v2 built-in map function
    bonus_2 = map(lambda x: x + 10
                  if x < 50 else x, scores)  # [40, 50, 50, 60, 70, 80, 90]

    # simple filter: filter failed scores
    # v1 - lambda: anonymous function
    fails_1 = filter(lambda x: x < 50, scores)  # [30, 40]
    # v2 - filter using an existing function
    fails_2 = filter(has_passed, scores)  # [30, 40]

    print(list(bonus_1))
    print(list(bonus_2))

    print(f"fails_1 {list(fails_1)}")
    print(f"fails_2 {list(fails_2)}")


def has_passed(score):
    return score < 50  # return a boolean expression


def score_frequencies():
    scores = [30, 40, 40, 50, 60, 70, 70, 70, 80, 80, 90]

    freq = {}
    for score in scores:
        # KeyError if you ask for a key that’s not in the dictionary
        try:
            freq[score] += 1
        except KeyError:
            freq[score] = 1

    print(freq)  # {30: 1, 40: 2, 50: 1, 60: 1, 70: 3, 80: 2, 90: 1}


def count_item():
    scores = [30, 40, 40, 50, 60, 70, 70, 70, 80, 80, 90]

    # v1
    cnt_40 = scores.count(40)
    print(f"cnt_40: {cnt_40}")

    # v2 - use list comprehension to filter
    list_40 = [x for x in scores if x == 40]
    print(f"list_40: {len(list_40)}")


def set_basics():
    print("Set Basics")
    print("-----------")

    # Create a set
    cities = set()
    print(cities)  # set()

    cities.add("London")
    cities.add("Paris")
    cities.add("London")

    print(len(cities), cities)  # 2 {'Paris', 'London'}
