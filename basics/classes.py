# Classes provide a means of bundling data and functionality together. 
# One definition of “Object-Oriented Programming” is using structures 
# to group together data (state) and methods (functions to alter state)

# Creating a new class creates a new type of object, allowing new instances of that type to be made. 
# Generally when people say object they mean an instance of a class.

# As in Modula-3, there are no shorthands for referencing the object’s members from its methods: 
# the method function is declared with an explicit first argument representing the object, 
# which is provided implicitly by the call. 

# “Private” instance variables that cannot be accessed except from inside an object DON'T exist in Python.
# However, there is a convention that is followed by most Python code: 
# a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API 
# (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.


# DUNDER methods
# Start (and end) with double underscores (Double UNDERscores). 
# “Dunder add” is one way to say __add__, “the add magic method” is another.
# Special methods determine what happens under the covers when operations are performed on an object. 
# For example, when you use the + or % operator on a string, the .__add__ or .__mod__ method is invoked respectively. 
# When you start implementing your own classes and want them to react to operations such as + or %, you can define them.
class Car:

    wheels = 4      # class variable shared by all instances

    def set_a_field(car_instance, year):
        car_instance.year = year

class Person:

    # Many classes like to create objects with instances customized to a specific initial state. 
    # Therefore a class may define a special method named __init__()
    # The attributes that are unique to an instance are put in the constructor.
    def __init__(self, name, surname): # signature is like a function out of this class
        self.name = name        # instance variable unique to each instance
        self.surname = surname

    def say_hi():
        return "Hi!"

# INHERITANCE
# 
# class DerivedClassName(BaseClassName):

def main():
    car1 = Car()
    car2 = Car()

    print(type(car1))       # <class '__main__.Car'>

    # we can bind any attribute to any instance
    car1.make = "Volkswagen"

    # the other instance may have another variable
    car2.model = "Sorento"

    print(car1.make, car1.wheels)
    car1.wheels = 6;
    print(car1.make, car1.wheels)
    print(car2.model, car2.wheels)
    # print(car1.model)     # AttributeError: 'Car' object has no attribute 'model'

    car3 = Car()
    set_variables(car3, "Volvo", "XC60") # not a method in the a class definition!
    print(car3.make, car3.model)

    car4 = Car()
    Car.set_a_field(car4, 2022) # a method in the class definition, called by class name and instance as argument
    print(car4.year)

    car5 = Car()
    car5.set_a_field(2007)  # as the method is called on instance, the first variable is automatically assigned as that instance, car5. 
    print(car5.year)

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


# a setter function, outside of class definition, that takes an instance and set its variable
def set_variables(car_instance, make, model):
    car_instance.make = make
    car_instance.model = model


if __name__ == '__main__':
    main()