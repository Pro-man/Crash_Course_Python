# Nathan Reid
# Aug. 17th, 2022
# Tuple 

# NOTE - Values that cannot change are immutable 
# NOTE - Immutable list is called a tuple
# NOTE - a tutple uses () instead of []
# NOTE a tuple have indexes

# Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250
# print(dimensions[0])

# Traceback (most recent call last):
#   File "dimensions.py", line 15, in <module>
#     dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment



# for loop
for dimension in dimensions:
    print(dimension)

# Writing over tuples
dimensions = (500, 900)
print("Original dimensions:")
# for loop
for dimension in dimensions:
    print(dimension)

# You can store a new tutple in the same variable name
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)