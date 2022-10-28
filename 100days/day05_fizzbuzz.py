# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# version 1
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz") 
    elif i % 5 == 0:
        print("Buzz") 
    else:
        print(i)

#version 2
# for i in range(1, 101):

#     divisible = False

#     if i % 3 == 0:
#         print("Fizz", end='') 
#         divisible = True
#     if i % 5 == 0:
#         print("Buzz", end='') 
#         divisible = True
#     if not divisible:
#         print(i, end='')

#     print() # newline