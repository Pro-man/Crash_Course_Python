# Nathan Reid
# Aug. 30th, 2022
# Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted.  "Santiago, Chile"
# Call your function with at least three city-country pairs and print the value that's returned.


# create function with parameters
def city_country(city, country):
    """Return a city and its country."""
    location = city + ", " + country
    # to execute code return it
    return location.title()

# call function with positional arguments
place = city_country('santiago', 'chile')
print(place)
place = city_country('baltimore', 'usa')
print(place)
place = city_country('paris', 'france')
print(place)

