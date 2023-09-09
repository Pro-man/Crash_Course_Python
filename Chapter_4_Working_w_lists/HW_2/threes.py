# Nathan Reid
# Aug. 16th, 2022
# Make a list of the multiples of 3 from 3 to 30.
# Use a for loop to print the numbers in your list. 

# create empty list
threes = []
# for loop with range() function
for num in range(3,31):
    # put number in variable after multiple by three
    number = num * 3
    # insert variable in  list
    # list.append(variable)
    threes.append(number)

# display list results
print(threes)