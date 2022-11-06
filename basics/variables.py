from xml.dom.minidom import Element


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
    print(f"{score=} id: {id(score)}")
    score += 1
    print(f"{score=} id: {id(score)}")

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

    # list_basics()
    # dict_basics()


def string_basics():

    name = "MK"
    print(type("MK"))

    #length of a string
    print(f"The length of string {name=} is {len(name)}")


    x = 123456
    x_str = str(x)
    print(f"{x=} {x_str=}") # x=123456 x_str='123456'

    # number of digits of an int
    print("Number of digits,", x, ":", len(str(123456)))

    print("\"Yes\", they said.")

    print("C:\some\name")  # here \n means newline!
    print(r"C:\some\name") # raw strings



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

    # Common Methods

    # “endswith
    # If you have a variable holding a filename, you might want to check the extension.
    xl = 'Oct2000.xls'
    if xl.endswith('.xls'):
        print("xls file")


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

def list_basics():
    #List Lists might contain items of different types, but usually the items all have the same type.
    squares = [1, 4, 9, 16, 25]
    print(squares)
    
    # lists can be indexed and sliced:
    print("squares[0]:", squares[0])

    # add new items at the end of the list
    squares.append(36)
    
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
