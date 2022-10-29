class Car:
    def set_a_field(car_instance, year):
        car_instance.year = year

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

def main():
    car1 = Car()
    car2 = Car()

    # we can bind any attribute to any instance
    car1.make = "Volkswagen"

    # the other instance may have another variable
    car2.model = "Sorento"

    print(type(car1)) # <class '__main__.Person'>

    print(car1.make)
    print(car2.model)
    # print(car1.model) # AttributeError: 'Car' object has no attribute 'model'

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

    

# a setter function, outside of class definition, that takes an instance and set its variable
def set_variables(car_instance, make, model):
    car_instance.make = make
    car_instance.model = model


if __name__ == '__main__':
    main()
