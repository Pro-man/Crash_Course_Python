# Nathan Reid
# Aug. 24th, 2022 
# Make a dictionary containing three major rivers and the country each river runs through.
# Loop to print a sentence about each river
# Loop to print the name of each river 
# Loop to print the name of each country

# dictionary about rivers
rivers = {
    "Zaire": "Congo",
    "Amazon": "Peru",
    "Mississippi": "America",
}

# three sets of loops

# sentence loop
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")


# river name loop
for river in rivers.keys():
    print(river)


# country name loop
for country in rivers.values():
    print(country)