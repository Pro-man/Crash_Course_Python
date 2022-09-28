# Nathan Reid
# Sept. 5th, 2022
# Make a class called Restaurant.
# The _init__() method for Restaurant should store two attibutes:
    # a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information,
#  and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. 
# Print the two attributes individually, and then call both methods.


# create a class
class Restaurant():
    """Describe a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Simulate describe the restaurant."""
        print("This restaurant's name is " + self.restaurant_name + ".")
        print("The food that is served here is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """Simulate the restaurant opening."""
        print(self.restaurant_name + " is now open.")


# instance
my_food = Restaurant('Mango Mango', 'soul food')

my_food.describe_restaurant()
my_food.open_restaurant()
