from enum import Enum

# You can think of enumerations as collections of constants.
# Option 1: Creating Enumerations by Subclassing Enum
class Grade(Enum):
    A = 90
    B = 80
    C = 70
    D = 60

class Season(Enum):
    WINTER, SPRING, SUMMER, FALL = range(4)

class Size(Enum):
    XL = "Extra Large"
    L = "Large"
    M = "Medium"
    S = "Small"


def main():
    print( type(Size.XL) )      # <enum 'Grade'>

    # Option 2: Creating Enumerations With the Functional API
    HTTPMethod = Enum("HTTPMethod", ["GET", "POST", "PUSH", "PATCH", "DELETE"])
    print( type(HTTPMethod.GET), HTTPMethod.GET)
    
    # Iterating Through Enumerations
    for season in Season:
        # .name and .value attributes
        print(f"{season}, {season.name=}, {season.value=}") 
    
    # Without enums: create constants
    TYPE_A, TYPE_B, TYPE_C = range(3)

    some_function(TYPE_B)
    some_function(-1)   #you can call the function with any value, indeed.

    what_to_wear(Season.SUMMER)
    what_to_wear(-1)    # In python, types of parameters are not specified in function decleration, but others would prevent this!

def some_function(type):
    if type == 1:
        print("some_function> Type 1")
    else:
        print("some_function> NOT Type 1")

def what_to_wear(season):
    if season == Season.WINTER:
        print("what_to_wear> 🥶 You better take your coat")
    elif season == Season.SUMMER:
        print("what_to_wear> 😎 Do not forget your sunglasses")
    else:
        print("what_to_wear> Well, its complicated.")


if __name__ == "__main__":
    main()