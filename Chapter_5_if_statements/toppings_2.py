# Nathan Reid
# Aug. 18th, 2022 
# checking that a list is not empty

# NOTE - It is useful to check whether a list is empty before running a for loop.

# create empty list
requested_toppings = []
# conditional test
if requested_toppings:
    # for loop
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# Using Multiple Lists

# list 1# this could be a tuple
available_toppings = ['mushrooms', 'olives', 'green peppers',
                        'pepperoni', 'pineapple', 'extra cheese']

# list 2#
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for loop - loop though the second list
for requested_topping in requested_toppings:
    # if topping in first list and second list print
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")