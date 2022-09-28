# Nathan Reid
# Aug 15th, 2022
# Data visualizations, almost always work with sets of numbers
# Lists are ideal for storing set of numbers

# Python's range() function makes it easy to generate a series of numbers

# Range() function has off by one behavior

# for loop 
for value in range(1,5):
    # display value
    print(value)

# Python start counting at the first value you give it,
#  and it stops when it reaches the second value you provide.
# Because it stops at that second value, the output never contains 
# the end value. 

# for loop and use range() function
for value in range(1,6):
    print(value)

# Convert the results of the range() into a list() function.
# Wrap list() around range() function, the output will be a list of numbers.

# put range() wraped by list() function into a variable
numbers = list(range(1,6))
print(numbers)