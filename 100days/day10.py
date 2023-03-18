def main():
    result = higher_order_executor(multiply, 10, 2)
    print(result)

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

if __name__ == "__main__":
    main()