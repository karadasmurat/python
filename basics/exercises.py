import csv
from enum import Enum
from functools import reduce
import json
import math
import random

from domain import Book, Author


def main():

    exercise10_1()
    # printOnesDigit(1357)
    # printDigits(1357)
    # sumEvenNumbers_v0()
    # tipCalculator()
    # fizzBuzzGame()
    # generatePassword()

# Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. 
# Display the answer as "The result is [answer]".
def exercise0():
    a = int(input("Enter the first number "))
    b = int(input("Enter the second number "))
    c = int(input("Enter the multiplier "))
    print("The result is", (a + b) * c)

# Ask the user to enter a number between 10 and 20 (inclusive). 
# If they enter a number within this range, display the message “Thanks, 
# If not in range, or is not a number, display “Invalid Input”.
def exercise1():
    '''Try to parse user input to int, and then check the range.'''
    n = 0
    try:
        n = int(input("enter a number between 10 and 20 (inclusive)"))

        if 10 <= n and n <= 20:       # syntax like 10 < n < 20
            print("Thanks.")
        else:
            print("Input not in range.")
    
    except ValueError:
        print("Invalid Input.")


# Ask the user to enter their first name and then ask them to enter their surname in upper case.
# Join them together with a space between and display the name and the number of chars in the whole name (without spaces).
#   "Hi, <Surname> <Name>. You have <total> characters in your full name."
def exercise2():
    fname = input("What is your name? ")
    lname = input("What is your name? ")
    print(f"Hi, {lname.capitalize()} {fname.capitalize()}. You have {len(lname+fname)} characters in your full name.")



# Ask the user to type in their name and then tell them how many vowels are in their name.
def exercise2_1():
    vowels = ['a', 'e','i','o','u']
    vowel_cnt = 0
    name = input("Tell me your name, and I will tell you how many vowels it contains:  ").lower()
    for letter in name:
        if letter in vowels:
            vowel_cnt += 1
    
    print(f"Your name has", vowel_cnt, "vowels.")



# Create a program that will ask the user to enter a word and change it into Pig Latin. 
# Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. 
# If a word begins with a vowel you just add “way” to the end. 
# For example, banana becomes ananabay, and aadvark becomes aadvarkway. 
def exercise3():
    pig_latin_word = ""
    vowels = ['a', 'e','i','o','u']
    word = input("Enter a word, and I will translate it to Pig Latin: ")
    if len(word) == 0: 
        print("I need some characters to translate!")
    elif word[0] in vowels:
        pig_latin_word = word + "way"
    else:
        pig_latin_word = word[1:] + word[0] + "ay"

    print(pig_latin_word)
    return pig_latin_word


# Ask the user to enter the radius of a circle. Print out the area of the circle (π*radius2), rounded to 6 decimal places.
def exercise4():
    radius = float(input("Enter radius, and I will calculate the area: "))
    area = math.pi * radius ** 2
    print(round(area, 6))


# Ask the user to enter two numbers. Use whole number division to divide the first number by the second and also work out the remainder.
# Display the answer in a user-friendly, i.e. “7 divided by 2 is 3 with 1 remaining”.
def exercise5():
    a = int(input("Enter dividend (first number) "))
    b = int(input("Enter divisor (second number) "))

    quotient = a // b
    remainder = a % b

    print(f"{a} divided by {b} is {quotient} with {remainder} remaining")


# Ask the user to enter their name and display each letter in their name on a separate line.
def exercise6():
    name = input("What is your name? ")
    for letter in name:
        print(letter)

# Ask the user to enter a number between 1 and 10 and then display the times table for that number.
def exercise7():
    n = int(input("Enter a number, and I will give you times table for that number: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")


# Ask the user to enter a number and then enter another number. Add these two numbers together.
# Then ask if they want to add another number. 
# If yes, keep asking a new number and adding it to the sum. Display the total at the end.
def exercise8():
    print("Welcome to Mega Adder!")
    a = int(input("Enter the first number\t: "))
    b = int(input("Enter the second number\t: "))
    sum = a + b

    while True:
        c = input("Continue? [Y]es [N]o :")
        if c.lower() in ['y', 'yes']:
            x = int(input("Enter the next number\t: "))
            sum += x
        else:
            break

    print("\nDone. The sum is: ", sum)

def basket_info(items):
    print("Here is the basket: ", items)

def menu(menuItems):
    print()
    for index, value in enumerate(menuItems):
        print(f"[{index+1}] {value}")

    try:
        selected = int(input("\nEnter your choice: "))
        if selected < 1 or selected > len(menuItems):
            print("Invalid choice.")
            raise ValueError("Only integers in the menu are allowed.")

    except ValueError:
        print("Invalid choice.")
        raise ValueError("Only integers are allowed.")

    return menuItems[selected-1]

def auto_tune():
    return ['DMAX', 'TLC', 'TRT BELGESEL', 'Bloomberg', 'CNN International']

# Write a program to store tv channels list.
# The users can auto tune (reset) / Delete / Move / Rename a channel as much as they want.
def exercise9():
    channels = auto_tune()
    print(channels)

    while True:
        op = menu(['Auto Tune', 'Delete channel', 'Move a channel', 'Rename a channel', 'Quit'])

        if op == 'Auto Tune':
            channels = auto_tune()
            print("✅ Auto Tune complete. Channels:", channels)

        elif op == 'Delete channel':
            item_to_remove = input("\nWhich channel would you like to remove? ")
            if item_to_remove in channels:
                channels.remove(item_to_remove)
                print("✅ Deleted. Channels:", channels)
            else:
                print("Channel not Found. Did you spell it correctly?")

        if op == 'Move a channel':
            # Check if the name exists
            # To move, first remove the item (by pop or remove) and then insert into the new position.
            item_to_move = input("\nWhich channel would you like to move? ")
            if item_to_move in channels:
                new_index = int(input(f"\nEnter new number [1 - {len(channels)}]: "))
                channels.remove(item_to_move)               # remove the item
                channels.insert(new_index-1, item_to_move)  # insert into the new position (move)
                print("✅ Moved. Channels:", channels)

        elif op == 'Rename a channel':
            # Check if the name we want to update exists in the list using the in keyword or the index() method. 
            # If the name exists, we can update it by finding its current index, and setting the value at that index.
            item_to_rename = input("\nWhich channel would you like to rename? ")
            if item_to_rename in channels:
                new_name = input(f"\nEnter new name: ")
                i = channels.index(item_to_rename)  # find the index of the value
                channels[i] = new_name              # set value at the index
                print("✅ Renamed. Channels:", channels)

        elif op == 'Quit':
            break

# Write a program to organize books.
# The user can 'Browse Books', 'Add Book', 'Remove Book'
# Save information in a json formatted file.
def exercise10_1():
    print("Welcome to the Book List App")

    books = get_books()

    while True:
        op = menu(['Browse Books', 'Add Book', 'Remove Book', 'Search Title', 'Quit'])

        if op == 'Browse Books':
            books = get_books()
            for book in books:
                print(book)

        elif op == 'Add Book':
            title = input("\nTitle: ").capitalize()
            author = input("Author: ").capitalize()
            isbn = input("ISBN: ")
            g = input("Comma seperated list of Genres: ")
            genres = g.strip().split(',')   # Note that genres is List[str]
            book = Book(title, Author(author), isbn, genres)

            books = get_books()
            if book not in books:
                books.append(book)
                # construct a list of dicts, as books is a list of book instances.
                books_dicts = []
                for book in books:
                    # print("Book to save: ", book)
                    books_dicts.append(book.to_dict())

                save_books(books_dicts)

            else:
                print("We already have that book.")

        elif op == 'Remove Book':
            # In Python, it is not easy to directly delete a record from a .csv file. 
            # Instead we read the file into a temporary list, make the changes on this list 
            # and then overwrite the original file with the temporary list.

            q = input("\nISBN: ")

            books = get_books()
            # Linear search
            # iterate all the books, and look for their ISBN attribute
            found = False
            for book in books:
                if book.ISBN == q:
                    found = True
                    books.remove(book)
                    break

            # construct a list of dicts, as books is a list of book instances.
            books_dicts = []
            for book in books:
                # print("Book to save: ", book)
                books_dicts.append(book.to_dict())

            save_books(books_dicts)

            print("Removed book from the list.")

            if not found:
                print("This book is not in the list. Typo?")

        elif op == 'Search Title':
            books = get_books()
            q = input("Title: ").lower()
            # search_results = filter(lambda book: q in book.title.lower(), books)
            search_results = [book for book in books if q in book.title.lower()]
            if(len(search_results) > 0):
                print(len(search_results), "books found.")
                print(search_results)
            else:
                print(q, "not found.")

        
        elif op == 'Quit':
            break
        else:
            print("Not a valid menu option. Please try again.")

def get_books():
    with open("data/books.json") as file:
        books = []
        data = json.load(file)  # whole contents of file as a dict type, in this case [{book1}, {book2}]
        
        # return data 

        # construct a list of books from a list of dictionaries:
        for book_dict in data:
            book = Book.from_dict(book_dict)
            books.append(book)

        return books    
    
def find_book_by_ISBN(books, q):
    for book in books:
        if book['ISBN'] == q:
            return book


    
def save_books(data):
    with open("data/books.json", "w") as file:
        json.dump(data, file, indent=4)  # whole contents of file as a dict type.



# Write a program to store groceries list.
# The user can add/remove items as much as they want. 
# After they enter an item, ask them if they want to add/remove another. 
# If they do, allow them to add more names until they answer “no”.
# In the end, print the final list.
def exercise10():
    print("Welcome to the Groceries List App")

    shopping_list = []

    while True:
        basket_info(shopping_list)

        op = menu(['Add Item', 'Remove Item', 'Quit'])

        if op == 'Add Item':
            new_item = input("\nWhat do you need? ").capitalize()
            if new_item not in shopping_list:
                shopping_list.append(new_item)

        elif op == 'Remove Item':
            item_to_remove = input("\nWhat to remove? ").capitalize()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print("Removed {lfc} from the list.")

        elif op == 'Quit':
            break

        # Ask the user to continue, if 'no' then break
        # cont = input("Add / Remove another item? [Y]es [N]o :").lower()
        # if cont in ['n', 'no']:
        #     break

    shopping_list.sort()  # Note that .sort() returns None!
    print(shopping_list)
    print(f"🛒 You have {len(shopping_list)} items in the list: ", shopping_list)



# Make a maths quiz that asks five questions by randomly generating two whole numbers to make the question (e.g. [num1] + [num2]). 
# Ask the user to enter the answer. If they get it right add a point to their score. 
# At the end of the quiz, print the score
def exercise11():
    number_of_questions = 5
    score = 0

    for round in range(number_of_questions):

        question = get_question()
        # print(question)

        answer = int(input(question['q']))
        if answer == question['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f" Wrong, expected: {question['answer']}")

    print(f"\nYou got {score} out of {number_of_questions}")

def get_question():
        a = random.randint(1, 10)
        b = random.randint(1, 10)

        q = f"{a} * {b} = "

        return {'q': q, 'answer': a*b}

class Circle:
    simple_title = "Circle"

    def __init__(self, r):
        self.radius = r

    def update(self):
        self.radius = int(input("Enter radius: "))

    def area(self):
        return math.pi * self.radius ** 2
class Rectangle:
    simple_title = "Rectangle"

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def update(self):
        self.width = int(input("Enter width: "))
        self.height = int(input("Enter height: "))

    def area(self):
        return self.width * self.height

# Display a menu:
# Welcome to the generic area calculator!
#   [1] Circle
#   [2] Rectangle
# Enter your choice: 
# Depending on the choice, ask for dimensions of the shape, and display the area:
#   i.e. "The area of this Rectangle is : 6"

def exercise12():
    # menu = Enum('Menu', ['Circle', 'Rectangle'])
    # options = ['Circle', 'Rectangle']
    options = [Circle(0), Rectangle(0, 0)]
    selected_shape = print_options(options)
    selected_shape.update()
    area = selected_shape.area() # Note that there is no if-else here, we are using interface.
    print(f"The area of this {selected_shape.simple_title} is : {area}")

def print_options(option_list):
    print("\nWelcome to the generic area calculator!\n")
    selected = 0
    for index, value in enumerate(option_list):
        print(f"  [{index+1}] {value.simple_title}")
    try:
        selected = int(input("\nEnter your choice: "))
        if selected < 1 or selected > len(option_list):
            print("Invalid choice.")
            raise ValueError("Only integers in the menu are allowed.")

    except ValueError:
        print("Invalid choice.")
        raise ValueError("Only integers are allowed.")

    return option_list[selected-1]


#Write a program that prints ones digit of an n-digit number
def printOnesDigit(n):
    print(n % 10)

# Write a program that prints each digit of an n-digit number
def printDigits(n):
    ''' Convert the number into a string, and iterate over characters'''
    n_str = str(n)
    for digit in n_str:
        print(digit)

# Write a program to sum all the even numbers between 1 and 100
def sumEvenNumbers_v0():
    sum = 0
    for n in range(2, 101, 2):
            sum += n
    print(sum)

def sumEvenNumbers_v1():
    sum = 0
    for n in range(1, 101):
        if n % 2 == 0:
            sum += n
    print(sum)

def sumEvenNumbers_v2():
    ''' use built-in filter() to get even numbers, and use built-in sum() '''
    evens = filter(lambda x: x%2==0, range(1, 101))
    print(sum(evens))


# Write FizzBuzz Game
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
def fizzBuzzGame():
    for i in range(1, 101):
        if i % 15 == 0: 
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Write a program to split a bill among n people, with an optional tip.
def tipCalculator():
    print("Welcome to the tip calculator")

    bill = 0.0
    tip = 0
    people = 1

    while True:
        try:
            bill = float(input("\nWhat is the total bill? "))
            tip = int(input("Percentage Tip? [i.e 10] "))
            people = int(input("How many people to share? [i.e 2] "))
            break
        except ValueError:
            print("Invalid Input. Please try again.")


    share = round(((1+tip/100) * bill) / people, 2)

    print("Each person should pay", share)



# Write a password generator
def generatePassword():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    suggested_pwd = ""
    for i in range(nr_letters):
        suggested_pwd += random.choice(letters)
    for i in range(nr_numbers):
        suggested_pwd += random.choice(numbers)
    for i in range(nr_symbols):
        suggested_pwd += random.choice(symbols)

    print("Here is your password:", suggested_pwd)


    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    # We can first convert the string to a list of characters, 
    # shuffle the list using the shuffle() function from the random module, 
    # and then convert the shuffled list back to a string.
    pwd_list = list(suggested_pwd)  # list of chars
    random.shuffle(pwd_list)        # shuffle the list IN PLACE, and return None.
    pwd_str = "".join(pwd_list)     # join chars in the list back into a string
    print("Here is shuffled:", pwd_str )





# write a function that checks whether if the number passed into it is a prime number or not.
# A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers.
# A prime number is a positive integer that has exactly two distinct whole number factors (or divisors), namely 1 and the number itself.
def prime_checker(number):
    if number < 2:
        print("It's not a prime number.")
        return

    is_prime = True
    for i in range(2, number//2 + 1):
        if number % i == 0:
            is_prime = False
            break   # break immediately after composite detection

    if is_prime: 
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



if __name__ == "__main__":
    main()