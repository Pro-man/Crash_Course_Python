# Nathan Reid
# Aug. 16th, 2022
# Make a list of first 10 cubes, the cube of each integer from 1 to 10
# Use a for loop to print out the value of each cube

# empty list
cubes = []
# for loop and range() function to iterate through 1 to 10
for num in range(1,11):
    # put cube value in a variable
    cube = num ** 3
    # insert new value in list
    # list.append(variable)
    cubes.append(cube) 
# display list results
print(cubes)