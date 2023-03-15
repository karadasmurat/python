"""
Python is a powerful object-oriented programming language.

https://docs.python.org/3/

Interpreted languages do not compile directly to machine code, 
instead, there is a layer above, an interpreter that performs this function.
There are pros and cons to this approach. As you can imagine, on the fly translating can be time
consuming. Interpreted code like Python programs tend to run on the order of 10–100 times slower than C
programs. On the flip side, writing code in Python optimizes for developer time.


Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
Other programming languages often use curly-brackets for this purpose.

In other words, Python, unlike those other languages, uses two things to denote blocks:
    * a colon (:)
    * indentation

    # If statement, without indentation (will raise an error):
    if b > a:
    print("b is greater than a")    # you will get an error

    if b > a:
        print("b is greater than a")


"""
# The import system
# You can think of packages as the directories on a file system and modules as files within directories - but don’t take this analogy too literally.
# Python code in one module gains access to the code in another module by the process of importing it.
#
# Method 1. Import the entire file:
#
#   import file as fl
#
# Method 2. Import the specific function(s) you want from file.py:
#  
#   from file import function

# Global Variable
my_global_var = 100

def main():

    print_basics()

def global_variables():
    
    # Global variables are created outside of a function. They can be used by everyone, both inside of functions and outside.
    # To change the value of a global variable inside a function, refer to the variable by using the global keyword:
    global my_global_var 
    my_global_var = 111

def print_basics():

    print(my_global_var)

    x = "Python"
    y = "is awesome!"
    m = 11
    n = 22

    print(x + y)    # Pythonis awesome!
    print(m + n)    # 33
    # print(x + m)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

    # In the print() function, you output multiple variables, separated by a comma:
    print(x, y)  # Python is awesome!


if __name__ == "__main__" :
    main()  # calling main function here, declared at the top!