# Nathan Reid
# Aug. 14th, 2022
# Organizing a list

# list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# list name . sort()
cars.sort()
# sort() changes the list permanently
print(cars)

# reverse the sort permanently
cars.sort(reverse=True)
print(cars)
print("-")

# reverse() changes the order of a permanently list, 
# you can revert to the original order anytime by using
# reverse() to the same list a second time
cars.reverse()
print(cars)

# length of list
print(len(cars))

# list
vehicles = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(vehicles)

# sorted changes the list but not permanently
print("\nHere is the sorted list:")
print(sorted(vehicles))

print("\nHere is the original list again:")
print(vehicles)

print(len(vehicles))
