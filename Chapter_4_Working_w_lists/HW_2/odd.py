# Nathan Reid
# Aug. 16th, 2022
# Use the thrid argument of the range() function
# to make a list of the odd numbers from 1 to 20
# Use a for loop to print each number.

# empty list
numbers = []
# for loop using range() function third argument
for num in range(1,21,3):
    # put number in a variable
    number = num
    # insert number in list
    # list.append(variable)
    numbers.append(number)
    
# display list
print(numbers)