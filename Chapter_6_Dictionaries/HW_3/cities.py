# Nathan Reid
# Aug. 25th, 2022 
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about the city. 
# The keys for each city's dictionary should be something like country, population, and fact.
# Print the name of each city and all of the information you have stored about it. 

# dictionary with nested dictionaies
cities = {
    'houston': {
        'state': 'texas',
        'location': 'south',
        'country': 'America',
        'population': 6603000,
    },

    'atlanta': {
        'state': 'georgia',
        'location': 'south',
        'country': 'America',
        'population': 3744385,
    },

    'detroit': {
        'state': 'michigan',
        'location': 'north',
        'country': 'America',
        'population': 3521000,
    },

}

# loop through the dictionary to gain access to the keys, values
for city, city_info in cities.items():
    print(city.title() + ' facts are below:')
    # put the nested dictionaries keys in variables to use later
    zone_1 = city_info['state']
    zone_2 = city_info['population']
    zone_3 = city_info['location']

    print("This city is in " + zone_1.title() + " in the " + zone_3 + ".")
    print("The pop. is " + str(zone_2) + ".\n")

print("All cities are in " + city_info['country'] + ".")