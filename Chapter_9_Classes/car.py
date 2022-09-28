# Nathan Reid
# Sept. 5th, 2022
# Working with Classess and Instances

# NOTE - The first thing to do is modify the attributes of an instance directly or write methods
# that update attributes in specific ways. 

"""A class that can be used to represent a car."""

# Create a class
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # empty attribute that does not need a parameter
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    # values of attributes are the parameter
    def update_odometer(self, mileage):
        # """Set the odometer reading to the given value."""
        # self.odometer_reading = mileage
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles 



# put class in variable, the order of the positional arguments does not matter
my_new_car = Car('audi', 'a4', 2016)
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
# variable.function
print(my_new_car.get_descriptive_name())
# You can change the value directly through an instance (easiest way)
# the attribute has to come before the function call
my_new_car.odometer_reading = 23
# method takes in a mileage value and stores it
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# NOTE - Every attribute in a class needs an initial value, even if that value is 0 or an empty string.
# You do not have to include a parameter for this attribute.

# Modifying Attribute Value
# 1 - You can change the value directly through an instance (easiest way)
# 2 - Set the value through a method
# 3 - Increment the value through a method