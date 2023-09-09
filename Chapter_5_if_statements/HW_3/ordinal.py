# Nathan Reid
# Aug. 21, 2022
# Most ordinal numbers end in th, except 1,2, and 3
# Store the number 1 - 9 in a list
# Loop through the list
# Use an if elif else inside the loop to print the proper ordinal ending
#  for each number. Each resuklt should be on a separate line

# create number list
numbers = [1,2,3,4,5,6,7,8,9]

# loop through the entire list
for num in numbers:
    # use str() function to concatenate with string ending
    # the first three integers have a different ending
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    # the remaining integers have the same ending that's why I used the else to catch all
    else:
        print(str(num) + "th")