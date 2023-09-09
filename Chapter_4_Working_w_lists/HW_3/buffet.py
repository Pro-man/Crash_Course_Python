# Nathan Reid
# Aug.17th, 2022
# Think of five simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers.
# Try to modify one of the items, and make sure Python rejects the change.
# Replace two items with different foods. Add a block of code that rewrites
#  the tuple, and then use a for loop to print each of the items on the revised menu.

# create tuple of foods
menu_items = ('shrimp', 'chicken', 'steak', 'pork', 'tofu')
# for loop
for item in menu_items:
    print(item)

# try to change an item in tuple
# menu_items[0] = 'tuna'
# result
# Traceback (most recent call last):
#   File "buffet.py", line 16, in <module>
#     menu_items[0] = 'tuna'
# TypeError: 'tuple' object does not support item assignment

menu_items = ('vegetable', 'chicken', 'steak', 'pork', 'fish')
# for loop
for item in menu_items:
    print(item)
