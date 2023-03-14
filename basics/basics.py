# Global Variables
# created outside of a function, can be used by everyone, both inside of functions and outside.
my_global_var = 100

def main():

    # To change the value of a global variable inside a function, refer to the variable by using the global keyword:
    global my_global_var 
    my_global_var = 111
    print_basics()

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