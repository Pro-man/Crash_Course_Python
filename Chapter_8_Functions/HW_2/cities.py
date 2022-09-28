# Nathan Reid
# Aug. 29th, 2022
# Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as Reykjavik is in Iceland. 
# Given the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.


# create function with paramenters
def describe_city(city, country='iceland'):
    # docstring
    """Display a simple sentence with a city 
    and country."""
    print(city.title() + " is in " + country.title() + ".")

# call function with positional arguments
describe_city('reykjavik')
describe_city('san juan', 'coasta rica')

describe_city('london')



