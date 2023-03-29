"""
Python supports the usual logical conditions from mathematics:

Equals                      : a == b
Not Equals                  : a != b
Less than                   : a < b
Less than or equal to       : a <= b
Greater than                : a > b
Greater than or equal to    : a >= b

Syntax:
No (paranthesis), No {curly braces}
Use : and indentation

    # If statement
    if a > b and c > a:
        print("Both conditions are True")

    # One line if statement:
    if a > b: print("a is greater than b")


    # If-Else
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")

    
    # One line if-else expression, evaluating to a single value: 'cls' or 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

    # One line if-else:
    print("A") if a > b else print("B")




    While Loop: 
    -----------
    A while loop allows a block of code to be repeated (an unknown number of times) as long as a condition is being met.
    If the condition of a loop is always True, the loop runs for infinite times
    Basic syntax:

        while condition:
            # body of while loop

    Example:

        while not at_goal():
            if wall_in_front():
                jump()
            else:
                move()



"""

import os
import random

from util import printTitle

os.system("python --version")

def main():

    # ifBasics()
    
    # Generate a sequence of numbers
    # Syntax range([start,] stop [, step]) -> range object
    # x = range(5)
    # print(type(x), x, list(x))  # <class 'range'> range(0, 5) [0, 1, 2, 3, 4]

    capitals = {"TR":"Ankara", "UK":"London", "USA":"Washington"}

    # infinite_menu()
    loop_basics()
    # iterate_list()
    # iterate_dict(capitals)
    # askAndCheck()
    # print(square(5))
    # askAndCheckRange()

    # minx = min_of_three(110, 90, 99)
    # print("\nmin:", minx)

    # score = 65
    # res = passOrFail(score)
    # print(score, ":", res)

    # match_code("408")
    

    # print(sum_all_positive_numbers([1, 9, -5, 10, -1, 5]))  # 25
    # print(sum_all_positive_numbers(range(-4, 5)))           # 10

def ifBasics():
    resp = int(input("\n\nEnter a number: "))
    
    if resp < 0:
        print("why so negative?")
    elif resp == 0:
        print("zero? really?")
    else:
        print("positive vibes")

def infinite_menu():

    n = 0
    while True:
        n = int(input("Select an option [1-9]: "))
        #check for negatives to give a message.
        if n < 1 or n > 9:
            print("Not a valid option.")
        #break on the positive
        else:
            break
    
    for i in range(n):
        print("*", end='')


def square(x):
    return x**2



# one-liner for boolean return type
def is_positive(x):
    return x > 0        # boolean - if parantez icini direkt return edebilirsin (Comparison and Logical Operators)

# one-liner for boolean return type
def isEven(x):
    return x % 2 == 0   # return conditional itself

# one-liner for returning based on if-else
def passOrFail(score):
    return "Pass" if score >= 70 else "Fail"

# one-liner for assignment based on if-else
def coinFlip():
    x = 'Heads' if random.randint(0,1) == 1 else 'Tails'
    return x    # we could directly return x, this is just an example of assignment based on if-else

    
def askAndCheckRange():
    x = int(input("Enter Test Score: "))
    if 90 <= x <= 100:          # RANGE COMPARISON, instead of if score >= 90 and score <= 100:
        print("Congrats. A")
    else:
        print("Sorry, not an A")

def match_code(http_code):
    match http_code:
        case "200":
            print("OK")
        case "404":
            print("Not Found")
        case "500":
            print("Internal Server Error")
        # underscore symbol: default case
        case _:
            print(http_code, "Desc not found")

    
def loop_basics():

    printTitle("Loop Basics")
    
    for i in [1, 2, 3]:
        print("loop through a list", i)

    for i in range(3):          # 0, 1, 2
        print("loop in ange(3)", i)

    for i in range(10, 15):     # 10, 11, 12, 13, 14
        print("loop in range(10, 15)", i)

    for i in range(100, 110, 2):     # 100, 102, 104, 106, 108
        print("loop in range(100, 110, 2)", i)



    iterate_list()

    # Looping through a dictionary
    student_scores = { "Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62}
    iterate_dict(student_scores)

    # Iterate over characters of a string
    name = "Bingo"
    for letter in name:
        print(letter)


    # while loop
    i = 0
    while i < 5:
        print("while loop body", i)
        i += 1

    


def iterate_list():
    students = ["Harry", "Hermione", "Ron"]

    # v1 - no access to indexes
    for s in students:
       print(s)

    # v2 - access to indexes
    for index, name in enumerate(students):
        print(f"{index=} {name=}")

    # v3 - older approach
    for i in range(len(students)):
        print(i+1, students[i])

    # Nested loops:
    my_list = [1, 2, 3, 4, 5]
    for item1 in my_list:
        for item2 in my_list:
            print(item1, item2)

def iterate_dict(dctnry):
    # Option 1:
    # By default, when you iterate over a dictionary, you get back the KEYS
    # Python will throw an Error, if you add to or remove from a dictionary while looping over it. 
    for key in dctnry:
        print(key, dctnry[key])

    # Option 2: 
    # The key and corresponding value can be retrieved at the same time using the items() method.
    for k, v in dctnry.items():
        print(k, v)
    
def sum_all_positive_numbers(arg):
    '''summing all positive numbers in the sequence'''
    sum = 0
    for n in arg:
        if n < 0:
            continue        # Skipping over items in a loop
        sum += n

    return sum

def min_of_three(x, y, z):
    min=x
    if y < min:
        min=y

    if z< min:
        min=z

    return min



############
main()
