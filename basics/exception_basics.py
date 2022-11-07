# Look before you leap (LBYL)
# The idea is to check for exceptional cases before performing an action.
# “Look before you leap is not always a guarantee of success. 
# If you check that a file exists before you open it (looking before leaping), 
# that does not mean that the file will still be around later. 
# In multi-threaded environments, this is known as a race condition.

# Easier to ask for forgiveness (EAFP)
# Another option for dealing with exceptions to always perform the operation inside of a try block. 
# If the operation fails, the exception will be caught by the exception block.


# When defining your own exception, you should subclass from Exception or below.
class MKError(Exception):
    def __init__(self, msg):
        self.msg = msg


def main():
    divide(5, 1)  
    # divide(5, 0)            # division by zero
    divide (5, "one")       # unsupported operand type(s) for /: 'int' and 'str'

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        # handle specific
        print("ZeroDivisionError", e)
        
        # If invalid input is passed into your function and you know that you will not be able to handle it, 
        # you may raise an exception.
        raise e
        # return None

    except Exception as e:
        # handle others
        print("Exception", e)
        raise MKError("Important Error")
        # return None
    else:
        # Executed when no exception is raised
        print("Success!")
    finally:
        # The finally always executes. 
        # Usually, the purpose of the finally clause is to cleanup external resources.
        # “These resources should be freed regardless of whether an operation was successful or not.
        # CONSIDER USING CONTEXT MANAGER

        print("Cleanup, wheter successful or not")
    
    return res

if __name__ == "__main__":
    main()