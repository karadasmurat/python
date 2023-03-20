# Classes provide a means of bundling data and functionality together. 
# One definition of “Object-Oriented Programming” is using structures to group together data (state) and methods (functions to alter state)

# Creating a new class creates a new type of object, allowing new instances of that type to be made. 
# Generally when people say object they mean an instance of a class.

# As in Modula-3, there are no shorthands for referencing the object’s members from its methods: 
# the method function is declared with an explicit first argument representing the object, 
# which is provided implicitly by the call if called using an object ( object.method() )
#
#   def calculate_payroll(self):
#       return self.hours_worked * self.hour_rate

# Class names should normally use the CapWords convention. (Note that there is a separate convention for builtin names.)


# “Private” instance variables that cannot be accessed except from inside an object DON'T exist in Python.
# However, there is a convention that is followed by most Python code: 
# a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API 
# (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

# No privacy, so to set an attribute, we do not need a setter method. 
# Use instance.attribute = value
#
#       book1.hardcover = True

# DUNDER methods
# Start (and end) with double underscores (Double UNDERscores). 
# “Dunder add” is one way to say __add__, “the add magic method” is another.
# Special methods determine what happens under the covers when operations are performed on an object. 
# For example, when you use the + or % operator on a string, the .__add__ or .__mod__ method is invoked respectively. 
# When you start implementing your own classes and want them to react to operations such as + or %, you can define them.

# typing — Support for type hints (new in version 3.5)
#
#       def greeting(name: str) -> str:
#           return 'Hello ' + name


from abc import abstractmethod


class MyClass:
    pass

class Box:

    # Constructor
    def __init__(self, capacity):
        # define instance variables in the constructor body
        self.capacity = capacity    
        self.size = 0               # default initialization, not using constructor parameters.

    def load(self, amount):
        if self.size + amount <= self.capacity:
            # print("Loading", amount)
            self.size += amount

    # Called by str(object) and the built-in functions format() and print() 
    # to compute the “informal” or nicely printable string representation of an object.
    def __str__(self):
     return f"Box(capacity:{self.capacity} size:{self.size})"
    

class SimpleCar:

    wheels = 4      # class attribute: shared by all instances of this class

    def setYear(cls, year):
        cls.year = year        # Not defined over self?

class Person:

    # Many classes like to create objects with instances customized to a specific initial state. 
    # Therefore a class may define a special method named __init__()
    # The attributes that are unique to an instance are put in the constructor.
    def __init__(self, name, surname): # signature is like a function out of this class, taking self as argument
        self.name = name        # instance variable unique to each instance
        self.surname = surname

    def say_hi():
        return "Hi!"
    

# INHERITANCE
# Inheritance models what is called an IS-A relationship. 
# Inheritance is the mechanism you’ll use to create hierarchies of related classes. 
# These related classes will share a common interface that will be defined in the base classes. 
# Derived classes can specialize the interface by providing a particular implementation where applies.

# Let’s say you have a base class Animal and you derive from it to create a Horse class. 
# The inheritance relationship states that a Horse is an Animal. 
# This means that Horse inherits the interface and implementation of Animal, and Horse objects can be used to replace Animal objects in the application.
# This is known as the Liskov substitution principle.  (SOLID Principles)

# Composition is a concept that models a HAS-A relationship. 
# It enables creating complex types by combining objects of other types. 
# This means that a class Composite can contain an object of another class Component. 
# This relationship means that a Composite has a Component.

#       class DerivedClassName(BaseClassName):
#            pass

# When you derive one class from another, the derived class inherits both:
#   * The base class interface
#     The derived class inherits all the methods, properties, and attributes of the base class.
#   * The base class implementation
#     The derived class inherits the code that implements the class interface. "Use inheritance to reuse an implementation"

# Class Explosion Problem
# If you are not careful, inheritance can lead you to a huge hierarchical structure of classes that is hard to understand and maintain. 

# Python is one of the few modern programming languages that supports multiple inheritance. 
# Multiple inheritance is the ability to derive a class from multiple base classes at the same time. 
# Multiple inheritance has a bad reputation to the extent that most modern programming languages don’t support it. 
# Instead, modern programming languages support the concept of interfaces. 
# In those languages, you inherit from a single base class and then implement multiple interfaces, so your class can be re-used in different situations.

# Derived classes may override methods of their base classes. 
# (For C++ programmers: all methods in Python are effectively virtual.)

class Employee:
    '''Base class for all employee types.'''

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass

class SalaryEmployee(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name)          # superclass constructor
        self.weekly_salary = salary

    def calculate_payroll(self):
        return self.weekly_salary
    
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)          # superclass constructor
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate
    

# Duck Typing
class Duck:
    def swim(self):
        print("Duck swimming")

    def fly(self):
        print("Duck flying")

class Whale:
    def swim(self):
        print("Whale swimming")

class Human:
    def swim(self):
        print("Human swimming")




def main():

    obj = MyClass()
    # dir() returns a list of all the members in the specified object.
    print(dir(obj))     # We have not declared any members in MyClass, so where is the list coming from?
                        # This is because every class you create in Python implicitly derives from "object". 


    # Create a new instance of the class and assign this object to the local a variable box01.
    box01 = Box(10)
    box02 = Box(20)

    # Calling a method on a class
    # Option 1 - call the method on instance, the first variable is automatically assigned as that instance (box01) 
    box01.load(2)
    box01.load(1)
    print(box01)    # print() calls __str__(self)

    # Option 2 - a method in the class definition, call the method by "ClassName.method" and "instance as argument"
    Box.load(box02, 9)  
    print(box02)


    car1 = SimpleCar()
    car2 = SimpleCar()

    print(type(car1))       # <class '__main__.Car'>

    # we can bind any attribute to any instance
    car1.make = "Volkswagen"

    # the other instance may have another variable
    car2.model = "Sorento"

    print(car1.make, car1.wheels)   # Volkswagen 4
    car1.wheels = 6;
    print(car1.make, car1.wheels)   # Volkswagen 6
    print(car2.model, car2.wheels)  # Sorento 4
    # print(car1.model)     # AttributeError: 'Car' object has no attribute 'model'

    car3 = SimpleCar()
    function_from_outside_class(car3, "Volvo", "XC60") # not a method in the a class definition!
    print(f"{car3.make=}, {car3.model=}")   # Note that class definition does not mention make or model attributes!

    car4 = SimpleCar()
    car5 = SimpleCar()
    SimpleCar.setYear(car4, 2022) # Option 1 - a method in the class definition, called by "class name" and "instance as argument"
    car5.setYear(2007)      # Option 2 - as the method is called on instance, the first variable is automatically assigned as that instance, car5. 
    print(f"{car4.year=} {car5.year=}")

    # person1 = Person()    # Person.__init__() missing 2 required positional arguments
    person1 = Person("Michael", "Jordan")
    print(person1.surname) 

    # still bind any other variables to instances
    person1.anyothervar01 = "AOV1"
    print(person1.anyothervar01) 


    # Because everything is an object in Python, they will all have a __class__ attribute:
    print(person1.__class__)        # <class '__main__.Person'>
    print(person1.name.__class__)   # <class 'str'>
    print(person1.say_hi.__class__) # <class 'method'>



    # Duck Typing
    duck_typing()




# a function, outside of class definition, more like functional programming, 
# that takes an instance as argument instead of calling method on the instance with its state.
def function_from_outside_class(car_instance, make, model):
    car_instance.make = make
    car_instance.model = model


def expect_swimmer(somethingThatCanSwim):
    print("expect_swimmer: I can work with anything that can swim")
    somethingThatCanSwim.swim()


def duck_typing():
    """
    Duck typing in computer programming is an application of the duck test to determine whether an object can be used for a particular purpose:
        "If it walks like a duck and it quacks like a duck, then it must be a duck"
    
    """
    things = []
    things.append(Duck())
    things.append(Whale())
    things.append(Human())

    for t in things:
        expect_swimmer(t)
        



def inheritance_basics():
    s_employee = SalaryEmployee(1, 'John Sal', 1500)
    h_employee = HourlyEmployee(2, 'Jane Hr', 40, 15)

if __name__ == '__main__':
    main()