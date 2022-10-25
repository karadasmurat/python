def main():

    print("__name__ : ", __name__)
    
    print("C:\some\name")  # here \n means newline!
    print(r"C:\some\name") # raw strings

    operator_basics()
    string_basics()

    str="hello, there!"
    str = replaceFirstChar(str, '@')
    print(str)


    list_basics()
    dict_basics()
    
def operator_basics():

    x, y = 2, 6
    # use the ** operator to calculate power
    print(f"{x} ** {y}: {x**y}")

    x = 17 / 3
    y = 17 // 3 # floor division discards the fractional part
    print(f"17/3: {x}, 17//3: {y}")


def string_basics():
    # Strings can be concatenated (glued together) with the + operator, and repeated with *
    eff = 3 * 'A' + '+'
    print(eff)
    
    # Strings can be indexed, with the first character having index 0. 

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   
#-6  -5  -4  -3  -2  -1

# Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error
    
    word = "Python"
    print("First char:", word[0], "Last char:", word[-1])

# For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.
    print("slice using [1:3]:", word[1:3]) # yt

def list_basics():
    #List Lists might contain items of different types, but usually the items all have the same type.
    squares = [1, 4, 9, 16, 25]
    print(squares)
    
    # lists can be indexed and sliced:
    print("Element at index 0:", squares[0])
    
    # The built-in function len() also applies to lists:
    print("Length:", len(squares))

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

    
# Q: replace the first letter with '_' character
def replaceFirstChar(str, c):
    return c + str[1:]


# When a Python interpreter reads a Python file, it first sets a few special variables. 
# Python files are called modules and they are identified by the .py file extension. 
# A module can define functions, classes, and variables.
# So when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.
# But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.
if __name__ == "__main__" :
    main()
