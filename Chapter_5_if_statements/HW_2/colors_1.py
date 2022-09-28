# Nathan Reid
# Aug. 20th, 2022
# Create a variable called alien_color and assign it a value of 
# 'green', 'yellow', or 'red'.
# Write an if statement to test whether the alien's color is green.
# If it is, print a message that the player just earned 5 points.
# Write one version of this program that passes the if test and another 
# that fails. 

alien_colors = ['green', 'yellow', 'red']
# set variable
alien_color = 'green'
# write conditional test to check for 'green'
if alien_color in alien_colors:
    print("The player just earned 5 points.")


alien_color = 'red'
# compare variable to if statement
if alien_color == 'green':
    print("The player just earned 5 points.")
if alien_color == 'red':
    print("-")

