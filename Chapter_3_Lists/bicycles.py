# Nathan Reid
# Aug. 13th, 2022
# list

# List - is a collection of items in a particular order.
# The items can include letters, digits, or names.
# Items in the list don't have to be in any particular order.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Each position in the list is called an index
print(bicycles[0])

# You can use methods with list
print(bicycles[2].title())

# index positions start at 0
print(bicycles[1])
print(bicycles[3])

# index -1 always return the last item in the list
print(bicycles[-1] + " - last item in list")

# index -2 return the second item from the end of the list
# index -3 returns the third item from the end.

# you can use individual values from a list just as an variable
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)