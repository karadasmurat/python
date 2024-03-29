"""
One way to think of a function is as a black box that you can send input to (though input is not required). 
The black box then performs a series of operations and returns output 
(it implicitly returns None if the function ends without return being called). 
Function is an abstraction, providing an interface hiding the implementation details.
An advantage of a function is that it enables CODE REUSE. Once a function is defined, you can call it multiple times.

The keyword "def" introduces a function definition. 
It must be followed by the function name and the parenthesized list of formal parameters.
Parameters are specified after the function name, inside the parentheseswant, separated with a comma.
A "parameter" is the variable listed inside the parentheses in the function definition.
 An "argument" is the value that is sent to the function when it is called.

    def greet_with(name, location):
        print(f"Hi! This is {name} from {location}")

    greet_with("Madagaskar", "Alex")                # wrong order of positional parameters by mistake!
    greet_with(location="Madagaskar", name="Alex")  # the same function signature, called using a keyword argument


To write the function body block, use : and indentation instead of {}.
Spaces are the preferred indentation method (over tabs) - Use 4 spaces for indentation

Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition. 
This way the function will receive a tuple of arguments.
You can access the tuple values via indexing or iteration in a for loop.

      def add_arbitrary_num_of_args(*args):
          print("unnamed args:", args)    # print tuple, i.e. (1,) or (1, 2, 3, 4)
          sum=0
          for arg in args:
              sum += arg

          return sum


Default Argument Values 
This function can be called in several ways: 
  giving only the mandatory argument: ask_ok('Do you really want to quit?') 
  giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
  or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

        def ask_ok(prompt, retries=4, reminder='Please try again!'):
            pass
            

Type Annotations
Python is a dynamically typed language. That means that it in general it doesn't care about the types of objects we use, as long as we use them in valid ways:
    
    def add(a, b):
        return a + b

    assert add(10, 5) == 15, "+ is valid for numbers"
    assert add([1, 2], [3]) == [1, 2, 3], "+ is valid for lists"
    assert add("hi ", "there") == "hi there", "+ is valid for strings"

    try:
        add(10, "five")
    except TypeError:
        print("cannot add an int to a string")

whereas in a statically typed language our functions and objects would have specific types.

Type annotations is valid Python 3.6. The "typing" module contains many types. 
However, these type annotations don't actually do anything. 
You can still use the annotated add function to add strings, and the call to add(10, "five") will still raise the exact same TypeError

    def add(a: int, b: int) -> int:
        return a + b

There are still (at least) four good reasons to use type annotations in your Python code:
  * Having to think about the types in your code forces you to design cleaner functions and interfaces.
  * Using types allows your editor to help you with things like autocomplete (Figure 2-1) and to get angry at type errors.
  * Types are an important form of documentation.
  * There are external tools (the most popular is mypy) that will inspect the type annotations, and let you know about type errors.


            
"""

# Global Scope
# In general, you should try to avoid global variables.
capacity = 10


def main():
    # Note that Python creates a new function object, then points a variable to it using the name of the function.
    # print(type(greet))     # <class 'function'>

    # invoke functions by adding parentheses following the function name:
    # greet()

    # greet_with("MK")       # TypeError: greet_with() missing 1 required positional argument: 'location'
    # greet_with("Madagaskar", "Alex")                # wrong order of positional arguments !
    # greet_with(location="Madagaskar", name="Alex")  # the same function signature, called using a keyword argument

    # scope_demo()

    # print(change_case("ThisIsCamelCased"))
    # print(change_case("ThisIsCamelCased", seperator="%"))

    # Arbitrary Arguments
    # sum_1 = add_arbitrary_num_of_args(1)            # unnamed args: (1,)
    # sum_4 = add_arbitrary_num_of_args(1, 2, 3, 4)      # unnamed args: (1, 2, 3, 4)
    # To pass a list of integers to this function,
    # you can use the * operator to unpack the list and pass each element as a separate argument to the function.
    # nums_to_sum = [1, 2, 3, 4, 5]
    # sum_5 = add_arbitrary_num_of_args(*nums_to_sum)

    # say_hi_to_all(mom="BK", dad="MK")   # keyword args: {'mom': 'BK', 'dad': 'MK'}

    # basic built-in functions (https://docs.python.org/3/library/functions.html)
    # ------------------------

    # scores = [80, 95, 99, 66, 88, 77]
    # print(f"{scores} LEN:{len(scores)}")
    # print(f"{min(scores)=}\t{max(scores)=}\t{sum(scores)=}")

    # Note The behavior of round() for example, round(2.675, 2) gives 2.67 instead of the expected 2.68
    # This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float.
    # num1, num2, num3 = [2.675, 0.5, -2.675]
    # print(num1, round(num1), round(num1, 2))    # 2.675     3       2.67
    # print(num2, round(num2), round(num2, 2))    # 0.5       0       0.5
    # print(num3, round(num3), round(num3, 2))    # -2.675    -3      -2.67

    # Default Argument Values
    # ask_ok("Close File?");

    # function as an input to another function
    # higher_order_executor(multiply, 10, 2)

    # lambda_basics()

    type_annotations()

    # Recursion
    # recursion_gone_wrong()  # RecursionError: maximum recursion depth exceeded
    # countdown(5)
    # countdown_recursive(5)
    # print(factorial(10))
    # print(factorial_recursive(5))
    # print(fibonacci(40))
    # print(fibonacci_memoization(40))


def type_annotations():
    '''
    Python is a dynamically typed language. 
    That means that it in general it doesn't care about the types of objects we use, as long as we use them in valid ways:
    '''
    print("add(x, y) is valid for integers: ", add(x=10, y=5))
    print("add(x, y) is valid for strings: ", add(x="ten ", y="five"))
    print("add(x, y) is valid for lists: ", add(x=[1, 2], y=[3]))

    # NOT valid for int and str args:
    # add(10, "five")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

    # Type annotations is valid Python 3.6. However, these type annotations don't actually do anything.
    # You can still use the annotated add function to add strings, and the call to add(10, "five") will still raise the exact same TypeError
    add_typeannotated(10, 5)            # 15
    add_typeannotated("ten", "five")    # tenfive
    # add_typeannotated(10, "five")     # TypeError: unsupported operand type(s) for +: 'int' and 'str'


# a function with no parameters
def greet():
    ''''''
    # a string immediately after the :, this string is called a DOCSTRING, used solely for documentation.
    # docstrings are invaluable to anyone trying to use your code -

    print("Hi!")

# a function with 2 parameters


def greet_with(name, location):
    print(f"Hi! This is {name} from {location}")


def add_typeannotated(a: int, b: int) -> int:

    # Type annotations is valid Python 3.6. However, these type annotations don't actually do anything.
    # You can still use the annotated add function to add strings, and the call to add(10, "five") will still raise the exact same TypeError

    print(a+b)
    return a + b


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

# accept a function object


def higher_order_executor(f, x, y):
    return f(x, y)  # call function parameter


def onSomething__higher_order_executor_noarg(f):
    return f()  # call function without any parameters


def scope_demo():
    # Variables defined inside of a function or method will be local.
    x = 5
    name = "MK"
    capacity = 111      # Python will allow you to override variables in the global
    print(locals())     # {'x': 5, 'name': 'MK', 'capacity': 111}

    # print(globals())
    global_variables = globals()
    for key in global_variables:
        print(key, global_variables[key])       # capacity printed as 10!


# Default parameters allow you to specify the default values for function parameters.
# The default parameters are then OPTIONAL.
# Note that “Default parameters must be declared after non-default parameters. Otherwise, SyntaxError
def change_case(camel, seperator="_"):
    '''Take camel case string and return each word seperated by seperator'''
    other_case = camel[:1].lower(
    )      # begin with the first letter lower case.
    for letter in camel[1:]:            # loop for letters from index 1 to the end
        if letter.isupper():
            other_case += seperator
        other_case += letter.lower()

    return str(other_case)


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments.
# You can access the tuple values via indexing or iteration in a for loop.
def add_arbitrary_num_of_args(*args):
    print("unnamed args:", args)    # print tuple, i.e. (1,) or (1, 2, 3, 4)
    sum = 0
    for arg in args:
        sum += arg

    print("The sum of arbitrary argument list:", sum)
    return sum

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments


def say_hi_to_all(**kwargs):
    print("keyword args:", kwargs)
    for key in kwargs:
        # print(key, kwargs[key])
        print(f"hi, {kwargs[key]}!")


# *args is used as a parameter to send a non-keyworded variable-length argument list to functions
# **kwargs is used to pass a keyworded, variable-length argument dictionary to functions
# names args and kwargs is conventionally used, though not enforced by the language
def magic(*args, **kwargs):
    print("unnamed args:", type(args), args)
    print("keyword args:", type(kwargs), kwargs)

    for k in kwargs:
        print(f"{k}={kwargs[k]}")


def lambda_basics():
    """

    In functional programming, computations are done by combining functions that take arguments and return a concrete value (or values) as a result. 
    These functions don't modify their input arguments and don't change the program's state. They just provide the result of a given computation. 
    These kinds of functions are commonly known as pure functions.

    Lambda expressions (sometimes called lambda forms) are used to create anonymous functions.

    The expression 

        lambda parameters: expression 

    yields a function object. The unnamed object behaves like a function object defined with:

        def <lambda>(parameters):
            return expression

    Lambda functions are similar to user-defined functions but without a name.

    Lambda functions are frequently used with higher-order functions, 
    which take one or more functions as arguments or return one or more functions.

    """
    printTitle("lambda basics")

    print(doubleIt(10))             # regular function call
    # define and then immediately call the lambda function
    print((lambda x: x * 2)(10))

    # As a lambda function is an expression, it can be named:
    # Note that this is not the main use, main use is anonymous in-place definition
    def f(x): return x * 2
    print(f(3))                     # call a named lambda expression

    # Multiple arguments
    # The definition of the lambda lists the arguments with no parentheses
    full_name = lambda first, last, title="Mr.": f"Full name: {title} {first.title()} {last.title()}"
    print(full_name("alan", "turing"))    # Mr. Alan Turing

    # how to pass a value to an event handler using lambda:
    # normally, we cannot pass an arg to handler, since we only use its name to pass it as an argument to onSomething listener.
    onSomething__higher_order_executor_noarg(
        handler)                        # Handling:  Default
    onSomething__higher_order_executor_noarg(
        lambda x='item1': handler(x))   # Handling:  item1


def handler(str="Default"):
    print("Handling: ", str)


def doubleIt(x):
    return x * 2

# Default Argument Values
# This function can be called in several ways:
#   giving only the mandatory argument: ask_ok('Do you really want to quit?')
#   giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
#   or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        resp = input(prompt + " [Yes / No]").lower()
        # print("Your response", resp)
        if resp in ('y', 'ye', 'yes'):
            return True
        if resp in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


def printTitle(title):
    print(f"\n{title}")
    print("-" * len(title))


# Recursion
# It is legal for one function to call another; it is also legal for a function to call itself.
# RecursionError: maximum recursion depth exceeded
def recursion_gone_wrong():
    x = 10
    recursion_gone_wrong()

# Recursion


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blastoff!")

# It is legal for one function to call another; it is also legal for a function to call itself.


def countdown_recursive(n: int):
    if n <= 0:          # base case - no more recursive calls here!
        print("Blastoff!")
        return
    else:
        print(n)                    # do something
        countdown_recursive(n-1)    # recursive call - get nearer to base case


def factorial(n: int):

    if n < 0:
        # print("Factorial is not defined for negative integers.")
        # return None
        raise ValueError("Factorial is not defined for negative integers.")

    if n == 0:
        return 1

    fact = 1
    for i in range(1, n+1):
        fact *= i

    return fact


def factorial_recursive(n: int):
    if n == 0:          # base case - no more recursive calls here!
        return 1
    else:
        return n * factorial_recursive(n-1)


def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

# we can improve the efficiency of the Fibonacci function by using memoization,
# which is a technique that involves storing the results of expensive function calls and returning the cached result when the same inputs occur again.


def fibonacci_memoization(n, memo={}):
    if n in memo:       # return the cached result when the same inputs occur again
        print(n, "found in cache, will not compute again.")
        return memo[n]

    elif n == 0:
        # store the result in the memo dictionary before returning it.
        memo[n] = 0
        return 0

    elif n == 1:
        # store the result in the memo dictionary before returning it.
        memo[n] = 1
        return 1

    else:
        result = fibonacci_memoization(
            n-1, memo) + fibonacci_memoization(n-2, memo)
        memo[n] = result
        return result


if __name__ == '__main__':
    main()
