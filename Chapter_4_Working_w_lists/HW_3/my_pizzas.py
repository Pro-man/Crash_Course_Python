# Nathan Reid
# Aug. 17th, 2022
# Make a copy of the list of pizzas, and call it friend_pizzas.

# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# Print the message, My favorite pizzas are:, and then use a for loop
# to print the first list. 
# Print the message, My friend's favorite pizzas are:, and then use a 
# for loop to print the second list. 

# list
pizzas = ['supreme', 'chicken', 'cheese']

# copy the list
friend_pizzas = pizzas[:]

# Add a new pizza to each list to prove 
# the lists are not the same
pizzas.append('pepperoni')
friend_pizzas.append('hawaiian')

# display the lists
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)