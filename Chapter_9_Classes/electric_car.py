# Nathan Reid
# Sept. 5th, 2022
# Inheritance

# NOTE - When one class inherits from another, it automatically takes on 
# all the attributes and methods of the first class.
# The original class is called the parent class and the new class is the child class.
# The child class inherits every attribute and method from its parent class but
# is also free to define new attributes and methods of its own.

# Create a class
class Car(object):
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

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        # conditional test
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on full charge."
        print(message)

# child class - put parent class in parentheses
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    # give child class all of its parent class attributes
    def __init__(self, make, model, year):
        """Initialize attibutes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        # make the connection between parent and child class
        super().__init__(make, model, year)
    # NOTE - super function needs two arguments: reference to the child class and the self object
        # super(ElectricCar, self).__init__(make, model, year)
        # self.battery_size = 70
        self.battery = Battery()
        # Create a new instance of Battery and store that instance in the attribute self.battery

    # def describe_battery(self):
    #     """Print a statement describing the battery size."""
    #     print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

    # NOTE -  You can override any method from the parent class that 
    # doesn't fit what you're trying to model with the child class. To do this,
    # you define a method in the child class with the same name as the method you want to override
    # in the parent class. Python will only pay attention to the method you define in the child class.

# instance of child class
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

# instance.attribute.method
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# NOTE - Parent class must be apart of the current file and must appear before the child class.
# NOTE - Name of the parent class must be included in parentheses in the definition of the child class
# NOTE - super()function - is a special function that helps Python 
# make connections between the parent and child class.
# NOTE - __init__() method from ElectricCar's parent class, which gives an 
# ElectricCar instance all the attributes of its parent class.