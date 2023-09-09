# Nathan Reid
# Aug. 25th, 2022 
# Make two new dictionaries representing different people, and store all
# three dictionaries in a list called people. 
# Loop through your list of people. 
# As you loop through the list, print everything you know about each person.

# dictionary 1
person_0 = {
    'first name': 'Lavon',
    'last name': 'Armstrong',
    'age': 38,
    'city': 'Virginia Beach',
}

# dictionary 2
person_1 = {
    'first name': 'A.C.',
    'last name': 'Reid',
    'age': 44,
    'city': 'Chesapeake',
}

# dictionary 3
person_2 = {
    'first name': 'Larry',
    'last name': 'Breithewait',
    'age': 38,
    'city': 'Alexandria',
}

# put dictionaries in list
people = [person_0, person_1, person_2]

# loop through the list and print everything about the person
for person in people:
    print(person)
