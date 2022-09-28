# Nathan Reid
# Sept. 9th, 2022
# The module random contains functions that generate random numbers in a variety of ways.
# The function randint() returns an integer in the range you provide.
# The following code returns a number between 1 and 6.

# from random import randint
# x = randint(1,6)

# Make a class Die with one attributes called sides, which has a default value of 6.
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
# Make a 6 sided die and roll it 10 times.
# Make a 10 sided die and a 20 sided die. Roll each die 10 times.

# import
from random import randint

# create class
class Die():
    """Create random number generator."""

    def __init__(self):
        """Initialize attribute to get random number."""
        self.sides = 6 

    def roll_die(self,sides):
        """Print the random number."""
        # for loop
        for num in range(1,11):
            x = randint(1, self.sides)
            print("#" + str(num) + " - " +  str(x))

# create instance
dice = Die()

print("\n6 sided")
print("--------")
dice.roll_die(6)

# modify attribute sides amount
dice.sides = 10
print("\n10 sided")
print("--------")
dice.roll_die(10)

# modify attribute sides amount
dice.sides = 20
print("\n20 sided")
print("--------")
dice.roll_die(20)

