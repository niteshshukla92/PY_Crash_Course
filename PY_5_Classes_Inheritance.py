# Object-oriented programming --> Most effective technique to write software
# classes that represent real-world things and situations, and you create objects based on these classes
# Making an object from a class is called instantiation, and you work with instances of a class
# A function that’s part of a class is a method

# Creating and using a class
class Dog:
    """Attempt to model a dog"""
    def __init__(self,name,age):
        """Initialising age and name attribute"""
        self.name=name
        self.age=age
    def sit(self):
        """Simulate a dog sitting in response to command"""
        print(f"{self.name} is now sitting")
    def roll_over(self):
        """simulate rolling over in response to command"""
        print(f"{self.name} rolled over")
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling Methods
my_dog.sit()
my_dog.roll_over()

####new example
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(f"The restaurant is {self.restaurant_name}")
        print(f"The cuisine served is {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is 'Open' ")
    def set_number_served(self):
        print("Enter the number of customers that you served")
        self.number_served=input()




restaurant=Restaurant('Truffles','American')
print(f"The restaurant is {restaurant.restaurant_name}.")
print(f"The restaurant type is {restaurant.cuisine_type}.")
print(f"The restaurant has served {restaurant.number_served} customer.")

restaurant.number_served = 23
print(f"The restaurant has served {restaurant.number_served} customer.")
restaurant.set_number_served()
print(f"The restaurant has served {restaurant.set_number_served()} customer.")


restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant1=Restaurant('Pizza Bakery','Italian')
restaurant2=Restaurant('Tandoori Taal','Mughlai')
restaurant3=Restaurant('Zaitoon','Afghani')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

class Users:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def describe_user(self):
        print(f"The name is {self.first_name} {self.last_name}")
        print(f"Age is {self.age}")
    def greet_user(self):
        print(f"Welcome !!! {self.first_name}")
user=Users('Priya','Sharma',29)
user.describe_user()
user.greet_user()

# Working with Classes and Instances
class Car:
    """An attempt to represent a car"""
    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name=f"{self.make} {self.model} {self.year}"
        return long_name.title()
    def read_odometer(self,mileage):
        """Print a statement showing the car's mileage."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to odometer reading"""
        self.odometer_reading+=miles

my_new_car=Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_used_car=Car('subaru','outback',2015)
print(my_new_car.get_descriptive_name())
my_used_car.increment_odometer(23_500)
my_used_car.read_odometer()

# *****************************************
# **************Inheritance****************
# *****************************************
# Instances as Attributes
class Battery:
    """A simple attempt to model battery for an electrical car"""
    def __init__(self,battery_size=75):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"This is a EC with {self.battery_size} -kwh battery")


# Let's create a class electric car
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self,make,model,year):
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        # self.battery_size = 75
        self.battery=Battery()

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")



    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla=ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()

# Importing Multiple Classes from a Module
# module_name.ClassName
# from module_name import *



# Python Standard Library
from random import randint
print(randint(1,6))

from random import choice
players=['clarles','dick','harry']
first_up=choice(players)
print(first_up)