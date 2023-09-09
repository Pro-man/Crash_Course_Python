# Nathan Reid
# Sept. 19th, 2022
# Write a class called Employee. 
# The __init__() method should take in a first name, a last name, and an annual salary, and 
# store each of these as attributes.
# Write a method called give_raise() that adds $5000 to the annual salary by default but 
# also accepts a different raise amount.
# Write a test case for Employee. 
# Write two test methods, test_give_default_raise() and test_give_custom_raise().
# Use the setUp() method so you don't have to create a new employee instance in each test method. 
# Run your test case, and make sure both tests pass.

class Employee():
    """Create a employee profile."""

    def __init__(self, first_name, last_name, salary):
        """Store first name, last name, and an annual salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, increase = 5000):
        """Add to the employee salary."""
        self.salary += increase


