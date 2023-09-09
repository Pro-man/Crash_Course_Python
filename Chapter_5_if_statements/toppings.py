# Nathan Reid
# Aug. 18th, 2022 
# checking for inequality 

# NOTE - to determine whether two values are not equal, you can 
# combine an exclamation point and an equal sign(!=)

# set a value in a variable
requested_topping = 'mushrooms'
# conditional test - check to see if not equal
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# NOTE - to check all of the conditions of interest, use
# a series of simple if statements with no elif or else blocks.
# Use when more than one condition could be True and you want to 
# act on every condition that is True. 

# list
requested_toppings = ['mushrooms', 'extra cheese']
# conditionals
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza.")

# NOTE - You can watch for special values that need to be treated differently than other values in the list.

# list
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for loop to iterate through list
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# NOTE - Check for special items in list **********

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for loop to iterate through list
for requested_topping in requested_toppings:
#    add if statement to search for special item
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
