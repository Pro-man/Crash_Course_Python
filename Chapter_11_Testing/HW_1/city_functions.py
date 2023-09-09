# Nathan Reid
# Sept 18, 2022


# def location(city,country):
#     """Return the location of a city, and country."""
#     place = city.title() + "," + country.title()
#     return place
    
# setting = location('Santiago','Chile')
# print(setting)


def location(city,country, population = ''):
    """Return the location of a city, and country."""
    if population:
        place = city.title() + "," + country.title() + " - population " +  str(population)
    else:
        place = city.title() + "," + country.title()
    
    return place
    
setting = location('Santiago','Chile',500000)
print(setting)