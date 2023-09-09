# Nathan Reid
# Aug. 26, 2022
# Using int() to accept numerical input

# Int() function, which tells Python to treat the input as a numerical value.

# prompt
height = input("How tall are you, in inches? ")
# change string to number
height = int(height)

# conditional test
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")