# Nathan Reid
# Aug. 25th, 2022 
# Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary and store one to three
# favorite places for each person. To make this exercise a bit 
# more interesting, ask some friends to name a few of their favorite 
# places. Loop through the dictionary, and print each person's name and their favorite places.


# dictionary
favorite_places = {
    'Nate': 'Bora Bora',
    'Shantae': 'Hawaii',
    'Lavon': 'Brazil',
}

# loop through list and print each key and value
for key, value in favorite_places.items():
    print(key + "'s favorite place is " + value + ".")