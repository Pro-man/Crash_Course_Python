# Nathan Reid
# Sept. 5th, 2022
# Create three different instances from the class, and 
# call describe_restaurant() for each instance. 

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

# instances
customer_1 = Restaurant("Crepes", "French")
customer_2 = Restaurant("Cava", 'Mediterraanean')
customer_3 = Restaurant("Leone's", "Italian")


customer_1.describe_restaurant()
customer_1.open_restaurant()
print("\n")
customer_2.describe_restaurant()
customer_2.open_restaurant()
print("\n")
customer_3.describe_restaurant()
customer_3.open_restaurant()