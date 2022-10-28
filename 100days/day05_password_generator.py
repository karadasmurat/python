#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_v1 = ''
for i in range(nr_letters):
    password_v1 += random.choice(letters)

for i in range(nr_symbols):
    password_v1 += random.choice(symbols)

for i in range(nr_numbers):
    password_v1 += random.choice(numbers)

print("Here is your password:", password_v1)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

tmp = list(password_v1)     # string to list
random.shuffle(tmp)         # shuffle mutates the input list!
password_v2 = ''.join(tmp)  # list to string pytonic way. we could iterate list and append a stringbuffer conventionally.
print("Here is the shuffled version:", password_v2)
