# Nathan Reid
# Aug. 16th, 2022
 # Make a list of the numbers from one to one million.
# Use min(), and max() make sure the list starts at one and end at one million
# Use sum() to see how quickly the program can add up to one million

# create an empty list
numbers = []
# create a for loop that counts to one million
# use range() function to skip numbers - reason for third number
for num in range(1, 1000001, 1001):
    # put number in variable to use
    number = num
    # insert integer in list
    # list.append(variable)
    numbers.append(number)
    # display nums in list
    print(numbers)

# use min(), max(), sum() to check the values in list
print(min(numbers))
print(max(numbers))
print(sum(numbers))
