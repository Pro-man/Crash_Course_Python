# Nathan Reid
# Aug. 18th, 2022 
# if statements

# list
cars = ['audi', 'bmw', 'subaru', 'toyota']
# for loop - check to see if item is in list
for car in cars:
    # conditional tests 
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# NOTE - Every if statement is an expression that can be evaluated 
#  as True or False and is called a conditional test. 

# NOTE - Conditional test checks whether the value of a variable is equal 
# to the value of interest.

# equal sign SETS the value
car = 'bmw'
# double equal sign CHECKS the value (asks the question)
car == 'bmw'

# Testing for equality is case sensitive in Python
# If case matters to test the value of a variable,
# convert the variable's value to lowercase before doing the comparison.
car = 'Audi'
car.lower() == 'audi'
# store
# convert == compare

# When someone submits a new username, that new username is converted to lowercase
# versions of all existing usernames.