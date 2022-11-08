# One way to think of a function is as a black box that you can send input to (though input is not required). 
# The black box then performs a series of operations and returns output 
# (it implicitly returns None if the function ends without return being called). 
# Function is an abstraction, providing an interface hiding the implementation details.
# An advantage of a function is that it enables CODE REUSE. Once a function is defined, you can call it multiple times.




# Global Scope
# In general, you should try to avoid global variables.
capacity = 10

def main():
    # Note that Python creates a new function object, then points a variable to it using the name of the function.
    print (type(greet))     # <class 'function'>

    # invoke functions by adding parentheses following the function name.
    greet()

    # greet_with("MK")       # TypeError: greet_with() missing 1 required positional argument: 'location'
    greet_with("Madagaskar", "Alex")    # wrong order of positional arguments !
    greet_with(location="Madagaskar", name="Alex")  # the same function signature, called using a keyword argument

    scope_demo()

    print( change_case("ThisIsCamelCased") )
    print( change_case("ThisIsCamelCased", seperator="%") )


    # basic built-in functions (https://docs.python.org/3/library/functions.html)
    # ------------------------

    scores = [80, 95, 99, 66, 88, 77]
    print(f"{scores} LEN:{len(scores)}")
    print(f"MIN:{min(scores)}\tMAX:{max(scores)}")

    # Note The behavior of round() for example, round(2.675, 2) gives 2.67 instead of the expected 2.68
    # This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float. 
    num1, num2, num3 = [2.675, 0.5, -2.675]
    print(num1, round(num1), round(num1, 2))    # 2.675     3       2.67
    print(num2, round(num2), round(num2, 2))    # 0.5       0       0.5
    print(num3, round(num3), round(num3, 2))    # -2.675    -3      -2.67

# a function with no argument
def greet():
    ''''''
    # a string immediately after the :, this string is called a DOCSTRING, used solely for documentation.
    # docstrings are invaluable to anyone trying to use your code - 

    print("Hi!")

def greet_with(name, location):
    print(f"Hi! This is {name} from {location}")

def scope_demo():
    x = 5               # Variables defined inside of a function or method will be local.
    name = "MK"
    capacity = 111      # Python will allow you to override variables in the global
    print(locals())     # {'x': 5, 'name': 'MK', 'capacity': 111}

    #print(globals()) 
    global_variables = globals()
    for key in global_variables:
        print(key, global_variables[key])       # capacity printed as 10!


# Default parameters allow you to specify the default values for function parameters. 
# The default parameters are then OPTIONAL.
# Note that “Default parameters must be declared after non-default parameters. Otherwise, SyntaxError
def change_case(camel, seperator = "_"):
    '''Take camel case string and return each word seperated by seperator'''
    other_case = camel[:1].lower()      # begin with the first letter lower case.
    for letter in camel[1:]:            # loop for letters from index 1 to the end
        if letter.isupper():
            other_case += seperator
        other_case += letter.lower()

    return str(other_case)



if __name__ == '__main__':
    main()