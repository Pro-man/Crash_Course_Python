
"""A set of classes used to represent a Restaurant."""

class Restaurant():
    """Describe a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Simulate describe the restaurant."""
        print("This restaurant's name is " + self.restaurant_name + ".")
        print("The food that is served here is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """Simulate the restaurant opening."""
        print(self.restaurant_name.title() + " is now open.")

    def set_number_served(self, patron):
        """Set the number of customers that have been served."""
        self.number_served = patron

    def increment_number_served(self, patron):
        """Add the given amount to the odometer reading."""
        self.number_served += patron

# create child class
class IceCreamStand(Restaurant):
    """Create Icre cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine_type attributes."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'chocolate', 'vanilla', 'cookies n cream']

    def display_flavors(self):
        """Show the flavors of ice cream a customer can have."""
        print("These are the list of ice cream flavors " + self.restaurant_name +  " have:")
        for flavor in self.flavors:
            print(" - " + flavor.upper())