# Nathan Reid
# Aug. 25, 2022
# List in a dictionary

# Store information about a pizza being ordered
# dictionary with a list in it
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza" + 
    " with the following toppings:")

# loop through list in dictionary
for topping in pizza['toppings']:
    print("\t" + topping)

# NOTE - You can nest a list inside a dictionary any time you want
# more than one value to be associated with a single key in a dictionary

# NOTE - *** You should not nest lists and dictionaries too deeply

