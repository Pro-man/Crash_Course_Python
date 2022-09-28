# Nathan Reid
# Aug. 22nd, 2022

# NOTE - Dictionaires, allow you to connect pieces of related information.
# NOTE - Dictionaries can store an almost limitless amount of information.
# NOTE - A dictionary is a collection of key-value pairs. Each key is connected to a value,
# and you can use a key to access the value associated with that key.
# NOTE - A key's valuie can be a number, a string, a list, or even another dictionary.
# NOTE - You can use any object that you can create in Python as a value in a dictionary.
# NOTE - A dictionary wrapped in braces, {}, with a series of key-value pairs inside the braces.
# NOTE - Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.
# You can store as many key-value pairs as you want in a dictionary. 

# dictionary
alien_0 = {'color': 'green', 'points': 5}

# NOTE - To get the value associated with a key, give the name of the dictionary and 
# then place the key inside a set of square brackets.

# use the keys in the print statement to display the values
print(alien_0['color'])
print(alien_0['points'])

# set the value of the variable to a dictionary key
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# NOTE - Dictionaries are dynamic structures and you can add new key-value pairs to 
# a dictionary at any time. 

print(alien_0)

# add new keys and values to the current dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Python does not care about the order in which you store each key-value pair;
# it only cares about the connection between each key and its value. 


# empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)


# modify values in dictionary
# NOTE - give the name of the dictionary with the key in square berackets and then
#  the new value you want associated with that key.
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y-position': 25, 'speed': "medium"}
print("Original x-position: " + str(alien_0['x_position']))



if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


# NOTE - When you no longer need a piece of information that's stored in a dictionary
# you can use the del statement to permanently remove a key-value pair
# NOTE - del statement needs (name of dictionary and key)
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# delete key-value pair
del alien_0['points']
print(alien_0)