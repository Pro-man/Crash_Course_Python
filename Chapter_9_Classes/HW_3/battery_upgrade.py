# Nathan Reid
# Sept. 7th, 2022
# Use the final version of electric_car.py.
# Add a method to the Battery class called upgrade_battery(). 
# This method should check the battery size and set the capacity to 
# 85 if it isn't already. Make an electric car with a default battery size, 
# call get_range() once, and then call get_range() a second time after 
# upgrading the battery. You should see an increase in the car's range. 

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

    def upgrade_battery(self):
        """Check the battery size and set the capacity to 85 if it isn't already."""
        # check battery size
        if self.battery_size != 85:
            # set the new capacity to new value
            self.battery_size = 85
            print("New battery size: " + str(self.battery_size))

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
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

climate = ElectricCar('lucid', 'air dream', 2022)
climate.battery.get_range()
climate.battery.upgrade_battery()
climate.battery.get_range()