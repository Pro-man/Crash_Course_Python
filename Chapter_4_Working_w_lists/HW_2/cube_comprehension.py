# Nathan Reid
# Aug. 16th, 2022
# Use a list comprehension to generate a list on the first 10 cubes

# list comprehension
# list name = calculations then for loop
# no colon needed at the end
# use range() funtion
cubes = [num ** 3 for num in range(1,11)]
# display list
print(cubes)