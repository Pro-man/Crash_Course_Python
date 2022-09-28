# Nathan Reid
# Aug. 22nd, 2022

# dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


# dictionary name[key]
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")


# for loop - name is the key and language is the value
for name, language in favorite_languages.items():
    print(name.title() + " 's favorite language is " 
    + language.title() + ".")
    

# keys() method is useful when you don't need to work with all of the values in a dictionary.
# keys() just print the keys in a dictionary
for name in favorite_languages.keys():
# for name in favorite_languages: -> does the same thing
    print(name.title())
    

# create list
friends = ['phil', 'sarah']
# loop through list
for name in favorite_languages.keys():
    print(name.title())
    # conditional test to see the name in the list and dictionary are the same
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + 
        favorite_languages[name].title() + "!")


# NOTE - prints the last value in the dictionary
print(favorite_languages[name] + "-----")


# dictionary
program_languages = {
    'jen': 'react',
    'sarah': 'c++',
    'edward': 'swift',
    'phil': 'python',
    'nate': 'python',
}

# conditional test
if 'erin' not in program_languages.keys():
    print("Erin, please take our poll!")


# NOTE - Use sorted() function to get a copy of the keys in ORDER.
for name in sorted(program_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


# NOTE - Use the values() method to return a list values without any keys
# This approach pulls all the values from the dictionary without checking for repeats.
# To see each language chosen without repetition, we can use a set


print("The following languages have been mentioned:")
for language in program_languages.values():
    print(language.title())


# NOTE - a set is similar to a list except that each item in the set must be unique.
# When you wrap set() around a list that contains duplicate items, Python identifies
# the unique items in the list and builds a set from those items. 
# The result is a nonrepetitive list of languages that have been mentioned.


print("The following languages have been mentioned:")
for language in set(program_languages.values()):
    print(language.title())

# NOTE - *** You should not nest lists and dictionaries too deeply

# dictionary
backend_languages = {
    'jen': ['react', 'javascript'],
    'sarah': ['c++', 'c'],
    'edward': ['swift', 'ruby'],
    'phil': ['python', 'go'],
    'nate': ['python', 'haskell'],
}

# loop through dictionary to get access to lists
for name, languages in backend_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    # loop through the list which is a value to get to the elements
    for language in languages:
        print("\t" + language.title())

