"""
Python is a powerful object-oriented programming language.

Python is a high-level, interpreted language developed in the late 1980s by Guido van Rossum 
at the National Research Institute for Mathematics and Computer Science in the Netherlands. 
The name Python, by the way, derives not from the snake, but from the British comedy troupe Monty Python’s Flying Circus, 
of which Guido was, and presumably still is, a fan.

https://docs.python.org/3/

Interpreted languages do not compile directly to machine code, 
instead, there is a layer above, an interpreter that performs this function.
There are pros and cons to this approach. As you can imagine, on the fly translating can be time
consuming. Interpreted code like Python programs tend to run on the order of 10–100 times slower than C
programs. On the flip side, writing code in Python optimizes for developer time.

Because Python code is interpreted and not compiled into native machine instructions, 
code written for one platform will work on any other platform that has the Python interpreter installed.

"""

"""  
On many systems Python comes pre-installed. 
Try running the python command to start the Python interpreter to check and see if it is already installed:
To open the interactive interpreter or REPL (Read Evaluate Print Loop) that you can use
to write small functions, to test out code samples, or even to function as a calculator:

        $ python
        Python 3.10.8 ...
        Type "help", "copyright", "credits" or "license" for more information.
        >>> 

        $ which python
        /usr/local/bin/python 

        $ which python3
        /Library/Frameworks/Python.framework/Versions/3.10/bin/python3

If you don't see this, you will need to install Python on your system.

To run the program:
        $ python helloworld.py 


Jupyter Notebooks
------------------
Jupyter Notebooks are a community standard for communicating and performing interactive computing.
They are a document that blends computations, outputs, explanatory text, mathematics, images, and rich media representations of objects.
JupyterLab is a next-generation web-based user interface for Project Jupyter.

    $ which jupyter
    /Library/Frameworks/Python.framework/Versions/3.10/bin/jupyter

Start JupyterLab:

    $ jupyter lab

# http://localhost:8889/lab




Creating Virtual Environments
------------------------------
Avoid System Pollution
Linux and macOS come preinstalled with a version of Python that the operating system uses for internal tasks.
If you install packages to your operating system’s global Python, these packages will mix with the system-relevant packages. 
This mix-up could have unexpected side effects on tasks crucial to your operating system’s normal behavior.

Sidestep Dependency Conflicts
Imagine you have an application that needs version 1 of LibFoo, but another application requires version 2. 
If you have only one place to install packages, then you can’t work with two different versions of the same library. 
How can you use both these applications? 

Python “Virtual Environments” allow Python packages to be installed in an isolated location for a particular application, 
rather than being installed globally.

    $ python3 -m venv /path/to/new/virtual/environment
    $ python3 -m venv /Users/mk/dev/python/environments/mkenv3.10

to activate
    $ source /path/to/venv/bin/activate
    (mkenv3.10) $ which python    (prompt changes)
    /Users/mk/dev/python/environments/mkenv3.10/bin/python

After creating and activating your virtual environment, you can now install any external dependencies that you need for your project:
Note: Before installing a package, look for the name of your virtual environment within parentheses just before your command prompt. 

    (mkenv3.10) $ python3 -m pip install <package-name>
    (mkenv3.10) $ python3 -m pip list

to deactivate
    (mkenv3.10) $ deactivate
    $
    


Syntax:
-------
* No Statement Terminators (;)
In many popular programming languages, you need to add a semi-colon at the end of every statement. 
Programmers with a background in Java, C++, and PHP habitually put a terminator at the end of every line.
But this is not true for Python.

* Colon (:) and Indentation
Spaces are the preferred indentation method (over tabs) - Use 4 spaces for indentation (PEP 8 Style Guide)
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
# Method 1. Import Module (the entire file)
#   import random           # dice1 = random.randint(1, 6)
#   import random as rnd    # dice1 = rnd.randint(1, 6)
#
#
# Method 2. Import the specific function(s) you want from file.py:
#  
#   from file import function


import random
import util

# Global Variable
my_global_var = 100

def main():
    print("__name__ : ", __name__)

    # print_basics()
    # input_basics()
    # operator_basics()
    random_basics()

    

def global_variables():
    
    # Global variables are created outside of a function. They can be used by everyone, both inside of functions and outside.
    # To change the value of a global variable inside a function, refer to the variable by using the global keyword:
    global my_global_var 
    my_global_var = 111

def print_basics():

    print(my_global_var)

    x = "Python"
    y = "is" 
    z = "awesome!"
    m = 11
    n = 22

    print(x + y + z)        # String concatenation: Pythonisawesome!
    print(x, y, z)          # *values: Python is awesome!
    print(x, y, z, sep="_") # Python_is_awesome!
    
    print(m + n)    # 33
    # print(x + m)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

    # In the print() function, you output multiple variables, separated by a comma:
    print(x, y)  # Python is awesome!

def input_basics():
    util.printTitle("Input Basics")

    name = input("What is your name? ")
    print(f"Hello, {name}!")

    # generate_band_name()
    # add_digits_of_2_digit_number()

    # x = input_int("\nHow old are you? ")


def generate_band_name():
    print("Welcome to the band name generator")

    city = input("What's the name of the city you grew up in? ")
    pet = input("What's your pet's name? ")

    print("Your band name could be", city + " " + pet)

def add_digits_of_2_digit_number():
    two_digit_number = input("Type a two digit number: ")
    print(int(two_digit_number[0]) + int(two_digit_number[1]))

def input_int(prompt):
    ''' Ask for a user input and try to cast it to an int. If can't, give an error messasge, and ask again.'''
    val = 0;

    while True:
        try:
            val = int(input(prompt)) 
            break
        except ValueError:
            print("Please input a valid integer.")
    
    return val


def operator_basics():

    # Mathematical Operators: + - * / // ** %
    a = 10
    b = 3   
    c = 2.0
    print(f"{a=}, {b=}, {c=}")
    print(f"{(a + c)=}")    # Type Promotion: 12.0     
    print(f"{(a / b)=}")    # Note: division always returns a float in Python
    print(f"{(a // b)=}")   # Floor division (returns the largest integer that is less than or equal to the result)
    print(f"{(a % b)=}")    # Modulus (returns the remainder of the division)
    print(f"{(a ** b)=}")   # Exponentiation


    # Membership Operators: IN, NOT IN
    fruits = ["banana", "apple", "strawberry", "grapes"]

    x = "banana" in fruits  # True
    print(x);   

    if "mango" not in fruits: print("Sorry, NOT IN fruits.")


    # Assignment Operators
    x = 55
    x += 1      # x = x + 1
    print(x)

    # Logical Operators: and, or, not
    if not(5 < x and x < 10):
        print("Not Between 5-10.")
    else:
        print("Between 5-10.")

def random_basics():

    # Randomness
    # The random module actually produces pseudorandom (that is, deterministic) numbers 
    # based on an internal state that you can set with random.seed if you want to get reproducible results
    # If a is omitted or None, the current system time is used.
    # random.seed(1234)  # this ensures we get the same results every time

    rf = random.random()                    # Return the next random floating point number in the range 0.0 <= X < 1.0

    grade1 = round(random.random() * 100, 2) 
    print(grade1)

    dice1 = random.randint(1, 6)            # Return a random integer N such that a <= N <= b
    print(dice1)

    # Choose a random element from a list:
    fruits = ["apple", "banana", "cherry"]  # Return a random element from the non-empty sequence
    rand_fruit = random.choice(fruits)
    print(rand_fruit)

    shuffle_characters_of_a_string("Hagrid")


def shuffle_characters_of_a_string(arg):
    ''' We can first convert the string to a list of characters, shuffle the list using the shuffle() function from the random module, and then convert the shuffled list back to a string. '''
    char_list = list(arg)               # list of chars
    random.shuffle(char_list)           # shuffle the list IN PLACE, and return None.
    arg_shuffled = "".join(char_list)   # join chars in the list back into a string
    print(arg_shuffled)

if __name__ == "__main__" :
    main()  # calling main function here, declared at the top!