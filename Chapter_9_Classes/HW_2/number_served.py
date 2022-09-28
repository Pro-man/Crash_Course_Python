# Nathan Reid
# Sept. 5th, 2022
# Add an attribute called number_served with a default of 0.
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, 
# and then change this value and print it again.

# Add a method called set_number_served() that lets you set the number
# of customers that have been served.
# Call this method with a new number and print value again.

# Add a method called increment_number_served() that lets you increment 
# the number of customers who've been served.
# Call this method with any number you like that could represent 
# how many customers were served in, say, a day of business.

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
        print(self.restaurant_name + " is now open.")

    def set_number_served(self, patron):
        """Set the number of customers that have been served."""
        self.number_served = patron

    def increment_number_served(self, patron):
        """Add the given amount to the odometer reading."""
        self.number_served += patron


# instance withing a variable with positional arguments
customers = Restaurant('Vintage Kitchen', 'French')
print("We have served " + str(customers.number_served) + " so far.")
# 1 Set
customers.number_served = 22
print("We have now served " + str(customers.number_served) + " by noon.")
# 2 Modify using a method with argument
customers.set_number_served(100)
print("We have now served " + str(customers.number_served) + " by happy hour.")
# 3 increment method with argument
customers.increment_number_served(500)
print("We served " + str(customers.number_served) + " by the end of business.")
