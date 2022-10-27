def main():

    print("__name__ : ", __name__)

    # string_basics()
    # number_basics()

    list_basics()
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

# Q: replace the first letter with '_' character
def replaceFirstChar(arg, c):
    return c + arg[1:]

def number_basics():
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

    # Nested lists.
    # Think of them as list of names, where name is a list of chars: 
    # class[0] = first name
    # class[0][0] = first char of first name
    nested = [fruits, vegetables]
    print(nested) # [['banana', 'apple', 'strawberry', 'grapes'], ['Spinach', 'Carrots', 'Broccoli']]
    print(nested[0])    # ['banana', 'apple', 'strawberry', 'grapes']
    print(nested[0][1]) # apple



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
