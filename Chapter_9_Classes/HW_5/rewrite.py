# Nathan Reid
# Sept. 9th, 2022
# Use exerise 6-4
# Rewrite the program using  OrderedDict class and make sure the order of the 
# output matches the order in which key-value pairs were added to the dictionary

# import from library
from collections import OrderedDict

# NOTE - When using OrderedDict you have to create the instance after you import the library!!!!
# create instance
glossary = OrderedDict()

glossary['list'] = 'a collection of items in a particular order.'
glossary['integer'] = 'a whole number without decimals.'
glossary['float'] = 'any number with a decimal point.'
glossary['string'] = 'string is a collection of alphabets, words or other characters.'
glossary['boolean'] = 'true or false expression.'
glossary['variable'] = "containers for storing data values."
glossary['function'] = "a block of code which only runs when it is called."
glossary['class'] = "object constructor, or a 'blueprint' for creating objects. "
glossary['tuple'] = "collection which is ordered and unchangeable."

# for loop
for name, definition in glossary.items():
    print(name.title() + " - " + definition.title())


 