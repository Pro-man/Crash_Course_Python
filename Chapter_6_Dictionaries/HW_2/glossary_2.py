# Nathan Reid
# Aug. 24th, 2022 
# Replace your code in glossary.py by using a loop that runs
# through the dictionary's keys and values. Add five more terms to the new glossary.

# dictionary
glossary = {
    'list': 'a collection of items in a particular order.',
    'integer': 'a whole number without decimals.',
    'float': 'any number with a decimal point.',
    'string': 'string is a collection of alphabets, words or other characters.',
    'boolean': 'true or false expression.',
    'variable': "containers for storing data values.",
    'function': "a block of code which only runs when it is called.",
    'class': "object constructor, or a 'blueprint' for creating objects. ",
    'tutple': "collection which is ordered and unchangeable.",
}

# loop through the dictionary and print the key and value with items()
for key, value in glossary.items():
    print(key.title() + " - " + value.title() + "\n")