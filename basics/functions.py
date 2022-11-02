def main():
    greet()
    greet_with_name("MK")       # positional arguments
    greet_with_name(name="DJ")  # the same function signature, called using a keyword argument

# a function with no argument
def greet():
    print("Hi!")

def greet_with_name(name):
    print("Hi! This is", name)

if __name__ == '__main__':
    main()