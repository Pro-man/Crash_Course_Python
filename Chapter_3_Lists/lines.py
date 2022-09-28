# Nathan Reid
# Aug. 13, 2022
# list

# You can remove an item from it's position in the list or value

# list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# del statement
del motorcycles[0]
print(motorcycles)

# You can remove an item from any 
# position in a list using the del statement

# When you want to delete an item from a list
# and not use it in any way use the del statement

del motorcycles[1]
print(motorcycles)

# pop method removes the last item in a list, but it lets you work
# with that item after removing it
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# new list
# pop value from list
popped_motorcycle = motorcycles.pop()
# show the value was removed
print(motorcycles)
print(popped_motorcycle)


motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# You can use pop() to remove an item in a list at any position by including
# the index of the item you want to remove in parentheses

bikes = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + ".")

# If you only know the value of the item you want to remove,
# you can use the remove method.


motorcycles = ['honda', 'yamaha', 'suzuki','ducati', 'harley']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# remove() method can work with a value that's being removed from a list.

m_cycles = ['honda', 'yamaha', 'suzuki','ducati', 'harley']
print(m_cycles)
too_expensive = 'ducati'
m_cycles.remove(too_expensive)
print(m_cycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


# remove() method deletes only the first occurrence of the value you specify.
# If there's  a possibility the value appears more than once in the list, 
# you'll need to use a loop to determine if all occurrences of the value have 
# been removed. 