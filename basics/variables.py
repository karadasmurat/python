def main():

    print("__name__ : ", __name__)

    # Rules and conventions for naming in Python come from a document named “PEP 8 – Style Guide for Python Code” 8.
    # PEP stands for Python Enhancement Proposal, which is a community process

    # A variable should not have the name of a keyword.
    import keyword
    print(keyword.kwlist)

    # break = 'foo' # SyntaxError: invalid syntax

    # “not start with numbers”
    # 1st_num = 0 # SyntaxError

    # A. Identity
    name1 = "MK"
    print("name1:", id(name1))

    # It is possible for two variables to refer to the same object. 
    # When you bind a variable to an existing variable. They both point to the same object. “Running id on either of the two variables will return the same id. 
    # Note that this DOESN'T COPY the object the variable points to!
    name2 = name1
    print("name2:", id(name2))

    # “The 'is' operator checks for identity equality
    if name1 is name2:              # True
        print("name1 is name2")

    assert id(name1) == id(name2)   # OK

    # you can take a variable and point it to a new object. 
    # You will see that the identity of the variable has changed. But first is still the same 
    # (NOT LIKE C POINTERS!, the case is only about assigning a variable to another)
    name1 = "MSL"
    print(f"{name1=} {name2=}")     # name1='MSL' name2='MK'


    # B. Type
    print(type(name1)) # <class 'str'>

    # C. Mutability
    # Mutable objects can change their value in place.
    # In other words, you can alter their state, but their identity stays the same.
    # Objects that are immutable do not allow you to change their value. 
    # Instead, you can change their variable reference to a new object, but this will change the identity of the variable as well.
    # In Python, dictionaries and lists are mutable types. 
    # Strings, tuples, integers, and floats are immutable types.

    score = 90
    id_initial = id(score)
    score += 1
    try:
        assert id_initial == id(score)
    except AssertionError:
        print("Incrementing an int CHANGES its identity.")

    scores = [85, 95]
    id_old = id(scores)
    scores.append(90)
    if id_old == id(scores):        # True
        print("Appending to a list does not change its identity.")

    # Coercion
    # If you have an operation involving two numerics, coercion generally does the right thing. 

    # For operations involving an integer and a float, the integer is coerced to a float. 
    x = 10
    y = 0.5
    z = x + y
    print(f"{x=} type: {type(x)}")
    print(f"{y=} type: {type(y)}")
    print(f"{z=} type: {type(z)}")

    # If the left operand is a string and you use the multiplication operator, *, Python performs repetition
    x = "money"
    print(3 * x)


    # string_basics()
    # number_basics()
    # bool_basics()

    # list_basics()
    # tuple_basics()
    set_basics()
    # dict_basics()


def string_basics():

    name = "MK"
    print(type("MK"))

    #length of a string
    print(f"The length of string {name=} is {len(name)}")


    x = 123456
    x_str = str(x)
    print(f"{x=} {x_str=}")     # x=123456 x_str='123456'

    # number of digits of an int
    print("Number of digits,", x, ":", len(str(123456)))

    print("\"Yes\", they said.")

    print("C:\some\name")       # here \n means newline!
    print(r"C:\some\name")      # raw strings



    # Strings can be concatenated (glued together) with the + operator, and repeated with *
    eff = 3 * 'A' + '+'
    print(eff)
    
    # Strings can be indexed, with the first character having index 0. 

    #  +---+---+---+---+---+---+
    #  | P | y | t | h | o | n |
    #  +---+---+---+---+---+---+
    #   0   1   2   3   4   5   
    #  -6  -5  -4  -3  -2  -1

    # Python strings cannot be changed — they are immutable. 
    # Therefore, assigning to an indexed position in the string results in an error
    
    word = "Python 3"
    print("First char:", word[0], "Last char:", word[-1])

    # slicing
    # characters from position 1 (included) to 3 (excluded)
    # For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.
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

    # split and unpack
    full_name = "Jordan,Michael"
    surname, name = full_name.split(",")
    print(f"split {full_name=}: {name=} {surname=}")

    # split and use the index
    price_tag = "USD 55"
    currency = price_tag.split(" ")[0]
    print(f"split {price_tag=}: {currency=}")


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

    # Common Methods

    # endswith() & startswith()
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

    # join()
    # Oftentimes you have a list of items and need to insert something between them.
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


# Q: replace the first letter with '_' character
def replaceFirstChar(arg, c):
    return c + arg[1:]

def number_basics():

    # Do integers and floats have methods? Yes, again, everything in Python is and object and objects have methods. 
    # dir() lists all the attributes of the object passed into it.
    # This is easy to verify by invoking dir on an integer (or a variable holding an integer):”
    print("\ndir(<int>):\n", dir(100))

    f = 2.66666
    f_int = int(f);         # 2
    f_round = round(f);     # 3
    f_round2 = round(f, 2); # 2.67

    print(f, type(f), f_int, f_round, f_round2) # 2.66666 <class 'float'> 2 3 2.67

    x = 10      # <class 'int'>
    y = x / 1   # <class 'float'>
    print(f"{x=}, {type(x)}, {y=}, {type(y)}")

def bool_basics():
    # In Python parlance, it is common to hear of objects behaving as “truthy” or “falsey” — 
    # that means that non-boolean types can implicitly behave as though they were booleans.

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

    # There are two ways to create empty lists
    names = []
    surnames = list()

    # If you want to have prepopulated lists, you can provide the values in between the square brackets, using the literal syntax:
    members = ['Fred', 'Charles']

    #List Lists might contain items of different types, but usually the items all have the same type.

    # Note that range does not materialize the list, but rather gives you an iterable that will return those numbers when iterated over. 
    # By passing the result into list you can see the numbers it would generate:
    # The “up to but not including” construct is more formally known as the "half-open interval" convention.
    nums = range(5)     
    print( type(nums), len(nums), list(nums) )     # <class 'range'> 5 [0, 1, 2, 3, 4]

    even = list(range(0, 11, 2))
    print(even)     # [0, 2, 4, 6, 8, 10]

    squares = [1, 4, 9, 16, 25]
    
    # lists can be indexed and sliced:
    # A list is one of the sequence types in Python. Sequences hold ordered collections of objects.
    # Counting beginning with zero is called "zero-based indexing".
    print("squares[0]:", squares[0])

    # List insertion and deletion
    # To append items to the end of a list use the .append method:
    squares.append(36)
    members.append('Amy')

    # To remove an item, use the .remove method
    members.remove('Charles')
    
    # The built-in function len() also applies to lists:
    print("Length:", len(squares))

    # lists can be indexed and sliced:
    print(squares[2:]) # [9, 16, 25, 36]

    fruits = ["banana", "apple", "strawberry", "grapes"]
    vegetables = ["Spinach", "Carrots", "Broccoli"]

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


    # SORTING
    # The .sort() method sorts the list in place. 
    # It DOESN'T return a new, sorted copy of the list, rather it updates the list with the items reordered
    # list.sort(reverse=True|False, key=myFunc)
    # Parameter 'key' is Optional. A function to specify the sorting criteria(s) (run for every item in the list)

    members.sort()      # ascending by default.
    print(members)

    # Sort descending
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



    # Nested lists.
    # If the elements of a list are themselves type list, then we call this a nested list.
    # Think of them as list of names, where name is a list of chars: 
    # class[0] = first name (list of chars), the first element is the first list
    # class[1] = second name (list of chars), the second element is the second list
    # class[0][0] = first char of first name
    # matris halini de, aralarda '\n' olan isim listesi gibi düşün - a name in each row.
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

    odd = [1, 3, 5, 7, 9]
    print(*odd)     # 1 3 5 7 9

    # List unpacking - only first and second element. Remaining all elements to be captured in a list
    num = [2, 4, 6, 8, 10]
    a, b, *c = num
    print(f"{a=} {b=} {c=}") # a=2 b=4 c=[6, 8, 10]

    # Unpacking range object
    a, b, c = range(0, 3)
    print(f"{a=} {b=} {c=}") # a=0 b=1 c=2


def tuple_basics():

    # Tuples are IMMUTABLE sequences. You should think of them as ordered records. 
    # Once you create them, you CANNOT CHANGE them.

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

    """
    Why the distinction between tuples and lists?
        * The main difference between the objects is mutability. As tuples are immutable, they are able to serve as keys in dictionaries.
        * Tuples are used for returning multiple items from a function. 
        * Tuples are often used to represent a record of data such as the row of a database query, which may contain heterogeneous types of objects.
            person = ('Matt', '123 North 456 East', 24)
        * Tuples also use less memory than lists. If you have sequences that you are not mutating, consider using tuples to conserve memory.
    """

def set_basics():
    # A set is an UNORDERED collection that DOESN'T contain duplicates.
    # Therefore, a set is great for removing duplicates, and
    # if the order is important, a set is not the data type to use.
    
    
    # A set can be created with a literal syntax using { }
    digit_set = {0, 1, 2 ,3 ,4, 6, 7, 8, 9}

    # Sets can be specified by passing in a sequence into the set class
    digits = [0, 1, 4, 2, 3, 3, 7, 5, 6, 9, 0, 8, 9]
    digit_set = set(digits)
    print(digit_set)    # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    # To check for membership, use the in operation
    if 9 in digit_set:
        print(f"9 is in {digit_set}")

    # “Sets provide set operations, such as union (|), intersection (&), difference (-), and xor (^).
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
   #think of a dictionary as key:value pairs. A pair of braces creates an empty dictionary: {}

    #A. think as a collection
    born = {"MK":81, "MSL":14, "BK":83 }

    #B. think as the representation of a simple object 
    car = {"year":2019, "make": "Volkswagen", "model": "T-ROC"}

    print(car)

    # extracting the value given the key
    print(car["model"])

    # iterate over keys
    for byear in born:
        print(byear, ":", born[byear])

    # list of dicts
    cars = [
         {"year":2019, "make": "Volkswagen", "model": "T-ROC"},
         {"year":2007, "make": "Kia", "model": "Sorento"}
    ]

    for car in cars:
        print(car["model"])

    



# When a Python interpreter reads a Python file, it first sets a few special variables. 
# Python files are called modules and they are identified by the .py file extension. 
# A module can define functions, classes, and variables.
# So when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.
# But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.
if __name__ == "__main__" :
    main()
