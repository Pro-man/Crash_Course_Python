# Nathan Reid
# Aug. 24th, 2022 
# Use favorite languages.py
# Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already taken the poll, 
# print a message thanking them for responding. If they have not yet taken the poll,
# print a message inviting them to take the poll.

# dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# list
pollsters = ['tammy', 'ken', 'Cathy', 'Jerry']

# who should take the poll?
for key in favorite_languages.keys():
    print(key.title() + ", thank you for taking the poll.")

# conditional tests to see if user took the poll
if 'lewis' not in favorite_languages:
    print('Lewis, please take our poll.')

if 'tom' not in favorite_languages:
    print('Tom, please take our poll.')

# for loop to compare items in list to keys in dictionary
for pollster in pollsters:
    if pollster not in favorite_languages:
        print(pollster.title() + ", please take our poll. - - ")