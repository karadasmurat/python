from functools import reduce
import random


def main():
    # exercise1()
    # printOnesDigit(1357)
    # printDigits(1357)
    # sumEvenNumbers_v0()
    # tipCalculator()
    # fizzBuzzGame()
    generatePassword()



# Write a program that asks user their name and prints the number of characters in a user's name. 
def exercise1():
    print(len(input("What is your name? ")))

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

if __name__ == "__main__":
    main()