"""

Variables do not need to be declared with any particular type, and can even change type after they have been set.

    x = 4           # x is of type int
    x = "Sally"     # x is now of type str

Rules and conventions for naming in Python come from a document named “PEP 8 – Style Guide for Python Code” 8.
PEP stands for Python Enhancement Proposal, which is a community process

"""

import random
import math
from util import printTitle
from util import is_positive, is_even

from functools import reduce

def main():

    # A variable name cannot be any of the Python keywords:
    # import keyword
    # print(keyword.kwlist)

    # break = 'foo' # SyntaxError: invalid syntax

    # “do not start with numbers”
    # 1st_num = 0 # SyntaxError


    # Note that variables do not need to be declared with any particular type, and can even change type after they have been set.
    x = 4               # variable x is int, Literal[4]
    print(x, type(x))   # 4 <class 'int'>

    x = "MK"            # variable x is now str, Literal['MK']
    print(x, type(x))   # MK <class 'str'>
 
    # intro()
    # string_basics()
    # number_basics()
    # bool_basics()

    # list_basics()
    # tuple_basics()
    # set_basics()
    dict_basics()

def intro():

    # Camel Case
    myVariableName = "Harry"
    # Pascal Case
    MyVariableName = "Hermione"
    # Snake Case
    my_variable_name = "Ron"


    # Create a variable named score and assign the value 50 to it.
    score = 50

    # You can assign the same value to multiple variables in one line:
    c1 = c2 = c3 = "Black Pink"

    # Assign values to multiple variables in one line:
    x, y, z = "Orange", "Banana", "Cherry";
    print(f"{x=} {y=} {z=}")    # x='Orange' y='Banana' z='Cherry'

    # A. Identity
    name1 = "MK"
    list1 = ["SAT", "SUN"]

    # It is possible for two variables to refer to the same object. 
    # When you bind a variable to an existing variable, they both point to the same object. 
    # Running id on either of the two variables will return the same id. 
    # Note that changing object through one variable is visible through the other this if the referred object is mutable
    name2 = name1
    list2 = list1
    list3 = list(list1)     # explicit copy, new object!

    print("name1:", id(name1), name1)   # name1: 4380654384 MK
    print("name2:", id(name2), name2)   # name2: 4380654384 MK
    print("list1:", id(list1), list1)   # list1: 4381154432 ['SAT', 'SUN']
    print("list2:", id(list2), list2)   # list2: 4381154432 ['SAT', 'SUN']
    print("list3:", id(list3), list3)   # list3: 4310155968 ['SAT', 'SUN']

    # “The 'is' operator checks for identity equality
    if name1 is name2:                  # True
        print("IDENTITY equality check: name1 IS name2")

    assert id(name1) == id(name2)       # OK - No AssertionError

    # you can take a variable and point it to a new object, or mutate the variable if it is mutable (i.e lists)
    # pointing to a new immutable, you will see that the identity of the variable changes. 
    # changing the state of a mutable (i.e. list.append() will not change the identity
    name1 = "MSL"           # str is immutable. name1 will refer a new object, changing identity.
    list1.append("FRI")     # list is mutable. identity will be the same.                 

    print("name1:", id(name1), name1)   # name1: 4380884912 MSL
    print("name2:", id(name2), name2)   # name2: 4380654384 MK  (not affected)
    print("list1:", id(list1), list1)   # list1: 4381154432 ['SAT', 'SUN', 'FRI']
    print("list2:", id(list2), list2)   # list2: 4381154432 ['SAT', 'SUN', 'FRI']   (affected!)


    # B. Type
    print(type(name1)) # <class 'str'>

    # C. Mutability
    # Mutable objects can change their value in place.
    # In other words, you can alter their state, but their identity stays the same.
    # Objects that are immutable do not allow you to change their value. 
    # Instead, you can change their variable reference to a new object, but this will change the identity of the variable as well.
    # In Python, dictionaries and lists are mutable types. 
    # Strings, tuples, integers, and floats are immutable types.
    

    code = "CODE01"
    id_v0 = id(code);
    print("code:", id_v0, code) # code: 4368368240 CODE01

    code = "CODE02"             # update the value of the variable
    id_v1 = id(code);
    print("code:", id_v1, code) # code: 4368368368 CODE02   (id changes!)

    assert id_v0 != id_v1;      # OK - No AssertionError
    

    #                    +--------+
    #     name +--xxx--> |  "MK"  |  (X) will be garbage collected if not referenced by other
    #          |         +--------+ 
    #          |
    #          |         +--------+
    #          +-------> | "MSL"  |
    #                    +--------+ 
    

    score = 90
    id_initial = id(score)
    score += 1                  # update the value of the variable
    try:
        assert id_initial == id(score)      # NOK
    except AssertionError:
        print("Incrementing an int CHANGES its identity.")

    scores = [85, 95]
    id_old = id(scores)
    scores.append(90)
    if id_old == id(scores):                # True
        print("Appending to a list does not change its identity.")


    
    # Do integers and floats have methods? Yes, again, everything in Python is and object and objects have methods. 
    # dir() lists all the attributes of the object passed into it.
    # This is easy to verify by invoking dir on an integer (or a variable holding an integer):”
    print("\ndir(<int>):\n", dir(100))


def string_basics():
    """
    Text Sequence Type — str
    Textual data in Python is handled with str objects, or strings. 
    Strings are immutable sequences of Unicode code points.

    String literals are written in a variety of ways:

        Single quotes: 'allows embedded "double" quotes'
        Double quotes: "allows embedded 'single' quotes".
        Triple quoted: Three single quotes and Three double quotes (may span multiple lines)

    Strings may also be created from other objects using the str constructor.



    """

    printTitle("Strings")

    # String variables can be declared either by using single or double quotes:
    name = "Harry"
    house = 'Gryffindor'
    print(name, ":", type(name))    # MK : <class 'str'>

    # String concatenation - operator+ is overloaded
    z = name + "," + house          # Harry,Gryffindor

    # You can insert a variable into a string using f-strings.
    std = f"Hi! This is {name}, from {house}."    # Hi! This is Harry, from Gryffindor.
    print(std)

    #length of a string
    print(f"The length of string {name=} is {len(name)}")
    
    # number of digits, as the length of a string
    x = 123456
    x_str = str(x)  # casting (think of it as a constructor)
    digits = len(str(x))
    print(f"{x=} {x_str=} {digits=}")     # x=123456 x_str='123456' digits=6  

    # unicode
    # https://unicode.org/charts/nameslist/index.html
    print('\N{UPSIDE-DOWN FACE}')
    print("\U0001F60E")


    print("\"Yes\", they said.")

    # “Windows paths use \ as a separator, which can be problematic. ”
    print("C:\test\new_folder")         # here \t \n means tab and newline!
    print(r"C:\test\new_folder")        # raw strings C:\test\new_folder


    # Strings can be concatenated (glued together) with the + operator, and repeated with *
    eff = 3 * 'A' + '+'
    print(eff)
    
    # Strings can be indexed, with the first character having index 0. 

    #  +---+---+---+---+---+---+
    #  | P | y | t | h | o | n |
    #  +---+---+---+---+---+---+
    #   0   1   2   3   4   5   
    #  -6  -5  -4  -3  -2  -1

    # Python strings CAN'T be changed — they are immutable. 
    # Therefore, assigning to an indexed position in the string results in an error
    
    word = "Python 3"
    print("First char:", word[0], "Last char:", word[-1])

    # slicing
    # characters from position 1 (included) to 3 (excluded)
    # For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. 
    # For example, the length of word[1:3] is 2.
    print("slice using [1:3]:", word[1:3]) # yt
    #First 3 chars
    print("First 3 chars:", word[:3]) # Pyt
    #Drop first 2 chars
    print("Drop first 2 chars:", word[2:]) # thon

    greet = "hello, there!"
    greet = replaceFirstChar(greet, '@')
    print(greet)

    # Iterate over characters of a string
    name = "Bingo"
    for letter in name:
        print(letter)

    # split - return a list from a string, using a delimiter:
    nums_str = "one two three four five"
    nums = nums_str.split() # Return a list of the words in the string, using sep=None as the delimiter string.
    print(nums)     # ['one', 'two', 'three', 'four', 'five']

    # Notice that 'District of Columbia' has spaces
    states_str = 'Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, District of Columbia, Florida, Georgia, Hawaii'
    states = states_str.split(sep = ',')
    print(states)

    full_name = "Jordan-Michael"
    surname, name = full_name.split('-')
    print(f"split {full_name=}: {name=} {surname=}")

    # split and use the index
    price_tag = "USD 55"
    currency = price_tag.split()[0]
    print(f"{currency=}")


    # A nice benefit of using triple-quoted strings is that you can embed single and double quotes inside it without escaping them
    msg="""This string has double " and single quotes ' inside of it"""
    print(msg)


    # Empty String
    # Since an empty string behaves as falsey, you can test whether the string has content
    some_str = ""
    if not some_str:     # check empty string
        print(f"{some_str=} Missing str value")

    if not bool(some_str): 
        print(f"{some_str=} Missing str value")

    if len(some_str) == 0: 
        print(f"{some_str=} Missing str value")

    # Common String Methods
    # str.count()
    w = "internationalization"
    print(f"Count of 'a' in {w}: {w.count('a')}")     # Count of 'a' in internationalization: 3

    # str.endswith() & startswith()
    # If you have a variable holding a filename, you might want to check the extension.
    xl = 'Oct2000.xls'
    if xl.endswith('.xls'):         # True
        print("xls file")

    fname="202206_rec.dat"
    if fname.startswith("202206"):  # True
        print("June records")

    # The .find() method allows you to find substrings inside other strings. 
    # It returns the index (offset starting at 0) of the matched substring. If no substring is found it returns -1:
    print("great".find("eat"))      # 2

    # JOIN - Concatenate any number of strings. The string whose method is called is inserted in between.
    # Oftentimes you have a list of items and need to insert something between them.
    # see shuffle_characters_of_a_string()
    family = ["MK", "MSL", "BK"]
    fstr = " & ".join(family)
    print(type(fstr), fstr)    # <class 'str'> MK & MSL & BK

    # lower() & upper()
    # The .lower method returns a copy of the string converted to lowercase.
    print("MK".lower(), "MK".upper())    # mk MK

    # strip()
    # The .strip method returns a new string that removes preceding and trailing whitespace (spaces, tabs,newlines).
    input_str=" Jordan\nM. \n"
    print(input_str, len(input_str))
    print(input_str.strip(), len(input_str.strip()))

    shuffle_characters_of_a_string("Hagrid")


# Q: replace the first letter with '_' character
def replaceFirstChar(arg, c):
    return c + arg[1:]

def shuffle_characters_of_a_string(arg):
    ''' We can first convert the string to a list of characters, shuffle the list using the shuffle() function from the random module, and then convert the shuffled list back to a string. '''
    char_list = list(arg)               # list of chars
    random.shuffle(char_list)           # shuffle the list IN PLACE, and return None.
    arg_shuffled = "".join(char_list)   # join chars in the list back into a string
    print(arg_shuffled)

def number_basics():

    printTitle("Numbers")

    # Do integers and floats have methods? Yes, again, everything in Python is and object and objects have methods. 
    # dir() lists all the attributes of the object passed into it.
    # This is easy to verify by invoking dir on an integer (or a variable holding an integer):”
    # print("\ndir(<int>):\n", dir(100))

    x = 1234        # int
    print(f"{x=}, {type(x)=}")              # x=1234, type(x)=<class 'int'>

    f = 2.66666     # float

    print(f"{f=}, {type(f)=}")              # f=2.66666, type(f)=<class 'float'>
    print(f"{int(f)=}, {math.floor(f)=}")   # int(f)=2, math.floor(f)=2
    print(f"{round(f)=}, {round(f, 2)=}")   # round(f)=3, round(f, 2)=2.67

    x = 10      # <class 'int'>
    y = x / 1   # <class 'float'>
    print(f"{x=}, {type(x)}, {y=}, {type(y)}")

    #casting
    one_str = "1"               # str
    one_int = int(one_str)      # int
    print(f"{one_str=}, {type(one_str)}, {one_int=}, {type(one_int)}")

    # number of digits, as the length of a string
    x = 123456
    x_str = str(x)  # casting (think of it as a constructor)
    digits = len(str(x))
    print(f"{x=} {x_str=} {digits=}")     # x=123456 x_str='123456' digits=6  


    # Formatting Integers, local unaware
    fnum = 1_234_567        
    print(fnum)         # 1234567

    num = 1000000
    print(f"{num:,}")   # 1,000,000

    # Formatting Floats
    x = 12345.789
    print(f"{x:.2f}")         # 12345.79      - 2 decimals + dot = 3 digits for decimal, 8 - 3 = 5 digits for whole part
    print(f"{x:012.2f}")      # 000012345.79  - 12 digits including dot, 2 decimals and prefix padding 0.

    import locale
    locale.setlocale(locale.LC_ALL, "en_US")
    print(locale.format_string('%.2f', x, grouping=True))   # 12,345.79

    # Formatting currency
    print(locale.currency(x, grouping=True))                # $12,345.79


def bool_basics():
    # In Python parlance, it is common to hear of objects behaving as “truthy” or “falsey” — 
    # that means that non-boolean types can implicitly behave as though they were booleans. 
    # In other words, Python lets you use any value where it expects a Boolean. 
    # The following are all “falsy”: 
        # False
        # None
        # []    (empty list)
        # {}    (empty dict)
        # ""    (empty string)
        # set()
        # 0
        # 0.0

    print('bool("")', bool(""))             # bool("") False - an empty string is “falsey”
    print('bool("0")', bool("0"))           # bool("0") True - non-empty string behaves as "truthy"
    print("bool('False')", bool('False'))   # bool('False') True - non-empty string behaves as "truthy"


    # For numbers, zero coerces to False while other numbers have “truthy” behavior
    print("bool(0)", bool(0))               # bool(0) False
    print("bool(-1)", bool(-1))             # bool(-1) True

    # Since an empty string behaves as falsey, you can test whether the string has content
    some_str = ""
    if not some_str:     # check empty string
        print(f"{some_str=} Missing str value")

    # if you have a list and need to distinguish between an empty and non-empty list, this is sufficient:
    members = []
    if not members:                         # True - check empty list
        print(f"{members=} List is empty")  # members=[] List is empty

def list_basics():

    # A list is one of the sequence types in Python. Sequences hold ordered collections of objects.

    printTitle("List Basics")

    # There are two ways to create empty lists
    names = []
    surnames = list()

    # You can provide the values in between the square brackets, using the literal syntax:
    members = ['Fred', 'Charles']

    # lists can have items with the same value:
    scores = [70, 85, 70, 90, 70]
    # number of times x appears in the list.
    print(f"#70: {scores.count(70)}")   # 3

    # The number of items in a container - the built-in function len() also applies to lists
    print("The number of scores:", len(scores)) # 5

    # Some other built-in functions for iterables: min, max, sum
    print(f"{max(scores)=}, {min(scores)=}, {sum(scores)=}")    # max(scores)=90, min(scores)=70, sum(scores)=385


    #List might contain items of different types, but usually the items all have the same type.
    hybridList = ["abc", 34, True, "male"]

    # Note that range does not materialize the list, but rather gives you an iterable that will return those numbers when iterated over. 
    # By passing the result into list you can see the numbers it would generate:
    # The “up to but not including” construct is more formally known as the "half-open interval" convention.
    nums = range(5)     
    print(type(nums), len(nums), list(nums))     # <class 'range'> 5 [0, 1, 2, 3, 4]

    even = list(range(0, 11, 2))
    print(even)     # [0, 2, 4, 6, 8, 10]

    squares = [1, 4, 9, 16, 25]
    
    # Accessing Elements
    # You can refer to an element by its index (subscript) - uses "zero-based indexing"
    print("squares[0]:", squares[0])
    # print("squares[100]:", squares[100])    # IndexError: list index out of range

    # Negative indexing means start from the end
    # -1 refers to the last item, -2 refers to the second last item etc.
    print(f"The last item: {squares[-1]}"); # 25

    
    # ADD item to the END of a list:
    squares.append(49)      # [1, 4, 9, 16, 25, 49]

    # INSERT an item at the specified index, and shift the rest:
    squares.insert(5, 36)   # [1, 4, 9, 16, 25, 36, 49]
    print(squares[5])       # 36

    
    fruits = ["banana", "apple", "strawberry", "grapes"]
    tropical = ["mango", "pineapple"]

    # Append elements from any other iterable to the current list:
    fruits.extend(tropical) # ['banana', 'apple', 'strawberry', 'grapes', 'mango', 'pineapple']
    print(fruits)   


    members.append('Amy')

    # REMOVE the first ocurrence of value: (Find and erase)
    members.remove('Charles')

    # Remove and return a specific index (default -1, the last)
    poppedFruit = fruits.pop();  
    print(f"Removed: {poppedFruit}, fruits: {fruits}")  # Removed: pineapple, fruits: ['banana', 'apple', 'strawberry', 'grapes', 'mango']
    poppedFruit = fruits.pop(2);
    print(f"Removed: {poppedFruit}, fruits: {fruits}")  # Removed: strawberry, fruits: ['banana', 'apple', 'grapes', 'mango']

    # The del keyword also removes the specified index:
    del fruits[0]   # ['apple', 'grapes', 'mango']
    print(fruits)

    # Remove all items from the list. - The list still remains, but it has no content.
    # Equivalent to del mylist[:]
    vegetables = ["Spinach", "Carrots", "Broccoli"]
    vegetables.clear()
    assert len(vegetables) == 0     # OK

    # lists can be sliced:
    print(squares[2:]) # [9, 16, 25, 36]



    # empty list
    empty_list = []

    # Option 1: evaluating empty list object to False
    if not empty_list:
        print(f"checked 'not <list_name>' -> empty: {empty_list=}")  

    # Option 2: Checking whether the list size is equal to 0
    if len(empty_list) == 0:
        print(f"checked 'len(<list_name>) -> empty: {empty_list}")

    # Option 3: using the __len__() function
    if empty_list.__len__() == 0:
        print(f"checked '<list_name>.__len__() -> empty: {empty_list}")


    # Search for an item
    q_key = 'grapes'
    # q_key = 'aVeryDifferentFruit'
    # v1 - Membership Operator (in)
    if q_key in fruits: 
        print(f"{q_key} is IN {fruits}")

    # v2 - index()
    # return the index of the first occurrence, raises a ValueError if there is no such item.
    try:
        found_index = fruits.index(q_key)
        print(f"Index of first ocurrence {q_key} in {fruits}: {fruits.index(q_key)}") 
    except ValueError:
        print(f"Value not found: {q_key}")

    # total number of occurrences
    multi_n = [1, 2, 1, 3, 1, 4, 2, 1, 3]
    print(f"Total num. of ocurrences '1' in {multi_n}: {multi_n.count(1)}")     # 4

    # SORTING
    # --------
    # Every Python list has a sort method that sorts it in place. 
    # If you don’t want to mess up your list, you can use the sorted function, which returns a new list.
    # The list.sort() method sorts the list IN PLACE. 
    # It DOESN'T return a new, sorted copy of the list, rather it updates the list with the items reordered
    #
    # list.sort(reverse=True|False, key=myFunc)
    # Parameter 'key' is Optional. A function to specify the sorting criteria(s) (run for every item in the list)

    x = [4, 1, 2, 3]
    y = sorted(x)     # y is [1, 2, 3, 4], x is unchanged
    x.sort()          # x is [1, 2, 3, 4]

    members.sort()      # ascending by default.
    print(members)

    # Sort descending
    # If you want elements sorted from largest to smallest, you can specify a reverse=True parameter.
    cars = ['Ford', 'BMW', 'Mitsubishi', 'Volvo']
    print( cars.sort(reverse = True) ) # prints None! (but mutates the list anyway) 
    print(cars)         # ['Volvo', 'Mitsubishi', 'Ford', 'BMW']

    # Sort the list by the length of the values:
    cars.sort(key = lambda x: len(x))
    print(cars)         # ['BMW', 'Ford', 'Volvo', 'Mitsubishi']

    # Sort a list by dict value, i.e. newest to oldest
    cars = [
        {'car': 'Ford', 'year': 2005},
        {'car': 'Mitsubishi', 'year': 2000},
        {'car': 'BMW', 'year': 2019},
        {'car': 'VW', 'year': 2011}
    ]
    cars.sort(key = lambda x : x['year'], reverse=True)
    print(cars)     # [{'car': 'BMW', 'year': 2019}, {'car': 'VW', 'year': 2011}, {'car': 'Ford', 'year': 2005}, {'car': 'Mitsubishi', 'year': 2000}]


    # A more general option for sorting sequences is the sorted function. 
    # The sorted function works with any sequence. It returns a NEW list that is ordered
    old = [5, 3, -2, 1]
    nums_sorted = sorted(old)
    print(f"sorted({old}): {nums_sorted}")



    # Nested lists:
    # If the elements of a list are themselves type list, then we call this a nested list.
    #
    #   [[first_row], [second_row], [third_row]]    # members are like the rows of a 2-d matrix
    #
    #   [[first_row], 
    #    [second_row], 
    #    [third_row]]
    #
    #
    #   [[00,01,02], [11,12,13], [21,22,23]]
    #   
    #   [[00,01,02], 
    #    [11,12,13], 
    #    [21,22,23]]
    #
    #    nested_list[0] is the first row.
    #    nested_list[0][0] is the first member of the first row.
    #   
    # To simplify, think of them as list of names, where name is a list of chars: [Harry, Hermione, Ron]  
    # class[0] = Harry (list of chars), the first element is the first list
    # class[1] = Hermione (list of chars), the second element is the second list
    # class[0][0] = H (first char of first name)
    # matris halini de, aralarda '\n' ile basılmış isim listesi gibi düşün - an item in each row:

    nested = [fruits, vegetables]
    print(f"{nested=}")         # [['banana', 'apple', 'strawberry', 'grapes'], ['Spinach', 'Carrots', 'Broccoli']]
    print(f"{nested[0]=}")      # ['banana', 'apple', 'strawberry', 'grapes']
    print(f"{nested[0][0]=}")   # 'banana'

    # Looping over a NESTED LIST
    for row in nested:
        print(row)  # yoklama defterindeki ogrenci isim listesi gibi, once satırlar, sonra harfler.
        for column in row:
            print(column)

    # Iterable Unpacking. 
    # Assign values to multiple variables from a single expression
    a, b, c = [10, 20, 30]
    print(f"{a=} {b=} {c=}")    # a=10 b=20 c=30

    team_info = ["Chicago Bulls", "Chicago"]
    team_name, team_city = team_info
    print (f"{team_name} from {team_city}") # "Chicago Bulls from Chicago"


    # Send a list as an input to a function with arbitrary arguments *args:
    odd = [1, 3, 5, 7, 9]
    print(*odd)                 # *args vs *list_name       1 3 5 7 9
    arbitrary_arguments(*odd)   # arguments:  (1, 3, 5, 7, 9) -> unpack a list as a tuple ?

    # List unpacking - only first and second element. Remaining all elements to be captured in a list
    num = [2, 4, 6, 8, 10]
    a, b, *c = num
    print(f"{a=} {b=} {c=}") # a=2 b=4 c=[6, 8, 10]

    # Unpacking range object
    a, b, c = range(0, 3)
    print(f"{a=} {b=} {c=}") # a=0 b=1 c=2

    values = [10, 20, 30]
    print(*values)     

    # Iterate over a list:
    iterate_list()   

    # Functional programming style processing
    processList_FP()

    # list comprehension:
    list_comprehension()  


def iterate_list():
    students = ["Harry", "Hermione", "Ron"]

    # v1 - no access to indexes
    print("no access to indexes")
    for s in students:
       print(s)

    # v2 - access to indexes
    print("access to indexes - using enumerate(list)")
    for index, value in enumerate(students):
        print(f"{index=} {value=}")

    # v3 - older approach
    print("access to indexes - older approach using range(len(list)): ")
    for i in range(len(students)):
        print(i+1, students[i])

def processList_FP():
    """
    In functional programming, computations are done by combining functions that take arguments and return a concrete value (or values) as a result. 
    These functions don’t modify their input arguments and don’t change the program’s state. They just provide the result of a given computation. 
    These kinds of functions are commonly known as pure functions.

    Functional programming typically uses lists, and other iterables to represent the data along with a set of functions that operate on that data and transform it. 
    When it comes to processing data with a functional style, there are at least three commonly used techniques:
    
    1. Mapping consists of applying a "transformation function" to an iterable to produce a "new iterable".
    Items in the new iterable are produced by calling the transformation function on each item in the original iterable.
    
    2. Filtering consists of applying a predicate or Boolean-valued function to an iterable to generate a new iterable. 
    Items in the new iterable are produced by filtering out any items in the original iterable that make the predicate function return false.
    
    3. Reducing consists of applying a reduction function to an iterable to produce a single cumulative value.

    """

    printTitle("Functional Programming Style")

    numbers = [1, 2, 3, 4, 5]
    squared = []

    # v1 - loop over list, transform each item, append to a new list:
    for n in numbers:
        squared.append(n*n)
    
    print(squared)  # [1, 4, 9, 16, 25]

    # v2 - use built-in map function
    # Sometimes you might face situations in which you need to "perform the same operation on all the items" of an input iterable to build a new iterable. 
    # The quickest and most common approach to this problem is to use a Python for loop. However, you can also tackle this problem by using map()
    # The operation that map() performs is commonly known as a mapping because it maps every item in an input iterable to a new item in a resulting iterable.
    # The first argument to map() is a "transformation function". A common pattern is to use a lambda function as the first argument.
    # in Python 3.x, map() returns a map object, which is an iterator that yields items on demand - call list() to create the desired list object.
    cubed = map(lambda x: x**3, numbers)
    print("Numbers:", numbers)
    print("Mapped:",list(cubed))


    # Filtering
    # The first argument, function, must be a single-argument function. Typically, you provide a predicate (Boolean-valued) function to this argument. 
    # In other words, you provide a function that returns either True or False according to a specific condition.
    # This function plays the role of a decision function, also known as a "filtering function", because it provides the criteria to filter out unwanted values from the input iterable and to keep those values that you want in the resulting iterable. 
    # Note that the term unwanted values refers to those values that evaluate to false when filter() processes them using function.
    print(is_positive(-3));    # False - unwanted, will be filtered.

    numbers = [-3, -2, -1, 0, 1, 2, 3]
    positive_numbers = filter(is_positive, numbers) 
    print("Numbers:", numbers)
    print("Positives:", list(positive_numbers))


    # use lambda function as a filtering function:
    scores = [60, 40, 90, 80, 30, 70]
    passed = filter(lambda x: x>=60, scores)    # [60, 90, 80, 70]
    print("Scores:", scores)
    print("Passed:", list(passed))

    # Reduce
    # Python’s reduce() implements a mathematical technique commonly known as folding or reduction.
    # The idea behind Python’s reduce() is to take an existing function, apply it cumulatively to all the items in an iterable, and generate a single final value.
    # The first argument to Python’s reduce() is a two-argument function.
    # The call to reduce() in the this example applies lambda function to the first two items in numbers (1 and 2) and gets 3 as the result. 
    # Then reduce() calls lambda function using 3 and the next item in numbers (which is 3) as arguments, getting 6 as the result. 
    # The process is repeated until numbers runs out of items and reduce() returns a final result of 15.
    numbers = [1, 2, 3, 4, 5]
    total = reduce(lambda x,y: x+y, numbers)
    print("Numbers:", numbers)
    print("Total:", total)


def list_comprehension():

    printTitle("List Comprehension")

    # List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
    # Frequently, you’ll want to transform a list into another list by choosing only certain elements, by transforming elements, or both.  
    # The Pythonic way to do this is with list comprehensions

    scores = [33, 99, 44, 55, 88, 77, 22, 66]
    passed = [x for x in scores if x > 60]  # [99, 88, 77, 66]
    print(passed)

    even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]     (x For x in iF format)
    squares = [x * x for x in range(5)]                 # [0, 1, 4, 9, 16]

    print(f"{even_numbers=} {squares=} ")

    # Randomness
    # The random module actually produces pseudorandom (that is, deterministic) numbers 
    # based on an internal state that you can set with random.seed if you want to get reproducible results
    random.seed(123)  # this ensures we get the same results every time

    # Also, run a funtion n times and store results in a list
    four_uniform_randoms = [random.randint(1, 6) for _ in range(4)]     # [6, 6, 2, 3]

    print(f"{four_uniform_randoms=}")

    numbers = range(10)

    first_5 = [num for num in numbers if num < 5]
    print(*numbers)
    print(*first_5)     # *args *list_name

    results = [
        {"name":"Bob", "score":33},
        {"name":"Foo", "score":90},
        {"name":"Bar", "score":85},
        {"name":"Baz", "score":100}
    ]

    # filter the results
    # ------ version 1 ---------
    grades_A = []
    for result in results:
        if result['score'] >= 85:
            grades_A.append(result['name'])
    print(f"{grades_A=}")

    # ------ version 2 ---------
    grades_F = [result['name'] for result in results if result['score'] < 60]
    print(f"{grades_F=}")


def tuple_basics():

    """
    Why the distinction between tuples and lists?
        * The main difference between the objects is mutability. As tuples are immutable, they are able to serve as keys in dictionaries.
        * Tuples are used for returning multiple items from a function. 
        * Tuples are often used to represent a record of data such as the row of a database query, which may contain heterogeneous types of objects.
            person = ('Matt', '123 North 456 East', 24)
        * Tuples also use less memory than lists. If you have sequences that you are not mutating, consider using tuples to conserve memory.
    """

    printTitle("Tuples")

    # There are two ways to create an empty tuple: using either the tuple function or the literal syntax:
    empty = tuple()
    empty = ()
    print(empty) # ()
        
    # Create a tuple with one item in it:
    one = (1,)
    print(one) # (1,)

    # For tuples with only one item, you need to put a comma (,) following the item:
    d = (3)
    e = (3,)
    print(d, type(d))       # 3 <class 'int'>
    print(e, type(e))       # (3,) <class 'tuple'>

    # Because tuples are immutable you cannot append to them:
    # e.append(4)           # “AttributeError: 'tuple' object has no attribute 'append”

    one = 1
    two = 2

    # Tuple swap 
    (one, two) = (two, one)
    print(f"one: {one}, two: {two}")

    # Tuple swap, w/o paranthesis
    one, two = two, one
    print(f"one: {one}, two: {two}")


def set_basics():
    # Set represents a collection of DISTINCT elements. 
    # A set is an UNORDERED collection that DOESN'T contain duplicates.
    # Therefore, a set is great for removing duplicates, and
    # if the order is important, a set is not the data type to use.
    
    
    # A set can be created with a literal syntax using { }
    digit_set = {0, 1, 2 ,3 ,4, 6, 7, 8, 9}
    primes_below_10 = {2, 3, 5, 7}

    # However, that doesn’t work for empty sets, as {} already means “empty dict.” 
    # In that case you’ll need to use set()
    s = set()
    s.add(1)       # s is now {1}
    s.add(2)       # s is now {1, 2}
    s.add(2)       # s is still {1, 2}
    x = len(s)     # equals 2

    # find the distinct items in a collection
    # Sets can be specified by passing in a sequence into the set class
    digits = [0, 1, 4, 2, 3, 3, 7, 5, 6, 9, 0, 8, 9]
    print("A List can contain duplicates.", len(digits), digits) 
    digit_set = set(digits)
    print("A Set represents a collection of DISTINCT elements.", len(digit_set), digit_set)    # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    # To check for membership, use the in operation.
    # in is a very fast operation on sets.
    if 9 in digit_set:
        print(f"9 is in {digit_set}")

    # Sets provide set operations, such as union (|), intersection (&), difference (-), and xor (^).
    odd = {1, 3, 5, 7, 9}

    # difference (-)
    even = digit_set - odd
    print(f"{even=}")

    
    first_five = set(range(5))          # {0, 1, 2, 3, 4} 
    two_to_six = set([2, 3, 4, 5, 6])

    # union (|)
    union_ = first_five | two_to_six
    print(f" {first_five} | {two_to_six}: {union_}")   # {0, 1, 2, 3, 4, 5, 6}

    # intersection (&)
    intersect_ = first_five & two_to_six
    print(f" {first_five} & {two_to_six}: {intersect_}")   # {2, 3, 4}

    # Xor (^) returns a set of items that only are found in one set or the other, but not both
    in_one_or_the_other = first_five ^ two_to_six
    print(f"{in_one_or_the_other=}")    # {0, 1, 5, 6}






    # Because sets must be able to compute a hash value for each item in the set, 
    # sets can only contain items that are hashable. 
    # In Python, mutable items are not hashable. 
    # This means that you cannot hash a list or dictionary. 


def dict_basics():

    """
    It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are UNIQUE (within one dictionary). 

    A pair of braces creates an empty dictionary: {}
    Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary:

        tel = {'jack': 4098, 'guido': 4139}

    Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, (subscript icinde rakam yerine 'key' kullan)
    which can be any immutable type; strings and numbers can always be keys, whereas a list cannot be a key!
    Keys are UNIQUE and IMMUTABLE 

    You can compare a Python dictionary to an English dictionary. 
    An English dictionary has words and definitions. 
    The purpose of a dictionary is to allow fast lookup of the word in order to find the definition. 
    You can quickly lookup any word by doing a binary search 
    (open up the dictionary to the midpoint, and determine which half the word is in, and repeat).

    A Python dictionary also has words and definitions, but you call them keys and values respectively
    The purpose of a dictionary is to provide fast lookup of the keys.


    """
    # A pair of braces creates an empty dictionary: {}
    empty = {}
    print(f"{empty=}: {type(empty)}")   # empty={}: <class 'dict'>

    # A. think as the representation of a simple object (excel row)
    person = {'name': 'MK', 'born': 81, 'gender': 'M'}
    
    # B. think as a collection of data for ONE attribute, i.e. 1 excel column
    born = {"MK": 81, "MSL": 14, "BK": 83 }
    city_population = {"Antalya": 1430539, "Balikesir": 1069260, "Istanbul": 11076840, "Izmir": 3431204}


    car = {'year': 2019, 'make': 'Volkswagen', 'model': 'T-ROC', 'color': 'Orange'}
    print(car)

    # Access an item using the key by performing a lookup with an index operation:
    print( f"{car['model']=}" )

    # !!! if you try to access a key that does not exist, Python will throw an exception:
    # print( car['imaginary_key'])    # KeyError

    # Adding a NEW key-value pair
    car['horsepower'] = 130

    # Deleting keys
    del(car['color'])

    print("delete the key 'color' and add 'horsepower':", car)       # {'year': 2019, 'make': 'Volkswagen', 'model': 'T-ROC', 'horsepower': 130}

    # IN operator
    # check if a KEY is in the dictionary
    q_key = 'make'
    if q_key in car:       # True
        print("key found! corresponding value is:", car[q_key])

    # in also works with sequences. You can use the in statement with a list, set, or string to check for membership
    if 5 in [1, 2, 3, 4, 5]:
        print("value found!")



    # Iterate over a dictionary
    # Option 1:
    # By default, when you iterate over a dictionary, you get back the KEYS
    # Python will throw an Error, if you add to or remove from a dictionary while looping over it. 
    for key in person:
        print(key, person[key])
        # del person[key]     # RuntimeError: dictionary changed size during iteration
    
    # Option 2: 
    # The key and corresponding value can be retrieved at the same time using the items() method.
    for k, v in person.items():
        print(k, v)
    


    # NESTING Lists and Dictionaries
    # Sample 1 - list as a dict value {key: []}
    travel_log={
        "France": ["Paris", "Cannes"], 
        "Germany": ["Berlin", "Hamburg", "Köln" ]
    }
    print(travel_log["Germany"])    # ['Berlin', 'Hamburg', 'Köln']

    countries = ['United States', 'Australia', 'Japan', 'India', 'Russia']
    countries_dict = {'country': countries}
    print(countries_dict)       # {'country': ['United States', 'Australia', 'Japan', 'India', 'Russia']}
    
    # Sample 2 - dict as a dict value {key: {}}
    europe = { 
        'Spain': { 'capital':'madrid', 'population':46.77 },
        'France': { 'capital':'paris', 'population':66.03 },
        'Germany': { 'capital':'berlin', 'population':80.62 },
        'Norway': { 'capital':'oslo', 'population':5.084 } 
        }
    print(europe['Germany']['capital'])    # berlin

    # Sample 3 - A list of dicts: [{}, {}, {}]
    travel_list = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
    ]

    print(f"{travel_list[0]['cities']=}")   # ['Paris', 'Lille', 'Dijon']




    cars = [
         {"year":2019, "make": "Volkswagen", "model": "T-ROC"},
         {"year":2007, "make": "Kia", "model": "Sorento"}
    ]
    print(cars[0]['model'])     #T-ROC


    # create 2 lists from the keys and values of a dict:
    car = cars[0]
    print("Dictionary:", car)                               # {'year': 2019, 'make': 'Volkswagen', 'model': 'T-ROC'}
    print("List of keys:", [key for key in car])            # ['year', 'make', 'model']
    print("List of values:", [car[key] for key in car])     # [2019, 'Volkswagen', 'T-ROC']
    


def arbitrary_arguments(*args):
    print(f"arguments: ", args)



# When a Python interpreter reads a Python file, it first sets a few special variables. 
# Python files are called modules and they are identified by the .py file extension. 
# A module can define functions, classes, and variables.
# So when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.
# But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.
if __name__ == "__main__" :
    main()
