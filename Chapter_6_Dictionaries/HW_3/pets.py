# Nathan Reid
# Aug. 25th, 2022 
# Make serveral dictionaries, where the name of each dictionary is the name of a pet.
# In each dictionary, include the kind of animal and the owner's name. 
# Store these dictionaries in a list called pets.
# loop through your list and as you do print everything you know about each pet. 

# make dictionaries
prince = {
    'animal': 'dog',
    'owner': 'Nate',
    'name': 'prince',
}

midnight = {
    'animal': 'dog',
    'owner': 'A.C.',
    'name': 'midnight',
}

blue = {
    'animal': 'dog',
    'owner': 'Shantae',
    'name': 'blue',
}

# put dictionaries in list
pets = [prince, midnight, blue]

# for loop through the list
for pet in pets:
    # print information in the list
    print(pet['name'].title())
    print(pet['animal'].title())
    print(pet['owner'].title())