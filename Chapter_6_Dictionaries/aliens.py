# Nathan Reid
# Aug. 25, 2022
# Nesting Dictionaries

# NOTE - You can nest a set of dictionaries inside a list, a list of items inside a dictionary
# or even a dictionary inside another dictionary

# Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# list
aliens = [alien_0, alien_1, alien_2]

# for list to loop through the list
for alien in aliens:
    print(alien)

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens.
# use range() to control how many loops
for alien_number in range(30):
    # run dictionary
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    # list.append put new alien in list
    aliens.append(new_alien)

# change the values of three aliens with a slice and if statement to compare green value
for alien in aliens[:3]:
# conditional to compare values
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    # change yellow aliens to red
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show first 5 aliens. Use list slice
for alien in aliens[:5]:
    print(alien)
print("...")

# see how many aliens have been created and are in list
print("Total number of aliens: " + str(len(aliens)))

# NOTE - Common to store a number of dictionaries in a list when each dictionary
# contains many kinds of information about one object.