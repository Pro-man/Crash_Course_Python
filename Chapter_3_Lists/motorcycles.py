# Nathan Reid
# Aug. 13, 2022
# list

# To change an element, use the name of the list followed by the index
# of the element you want to change, and then provide the new value you 
# want that item to have

# list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# change index value
motorcycles[0] = 'ducati'
print(motorcycles)

# Add a new element to a list is to append the item to the list
motorcycles.append('ducati')
print(motorcycles)

# empty list
bikes = []

# append elements
bikes.append('honda')
bikes.append('yamaha')
bikes.append('harley')

print(bikes)

# insert elements
# add a new element at any position in your list
# specifying the index of the new element and the value of the new item
# This action shifts every other value in the list

# list
planes = ['piper cherokee 140', 'piper comanche 250', 'piper Aztec F']

# insert new element
planes.insert(0, 'cessna 150M')

# display new list
print(planes)