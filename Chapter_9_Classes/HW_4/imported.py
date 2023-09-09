# Nathan Reid
# Sept. 8th, 2022
# Using Restaurant class, store it in a module.
# Make a separate file that imports Restaurant. 
# Make a Restaurant instance, and call one of Restaurant's methods to show 
# that the import statement is working properly.

from taste import Restaurant

food = Restaurant('windy city pizza', 'italian')
food.open_restaurant()
food.describe_restaurant()

