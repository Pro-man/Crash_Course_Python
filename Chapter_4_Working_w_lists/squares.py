# Nathan Reid
# Aug 16th, 2022
# Working with list

# You can create almost any set of numbers with the range function.

# two asterisks(**) represents exponents

# empty list
squares = []
# for loop to put the values in the list
for value in range(1,11):
    # put the value in a variable
    square = value**2
    # insert the value in the list
    squares.append(square)

print(squares)

# NOTE - Focus first on writing code that you understand clearly,
# which does what you want it to do.

# list
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))


# list comprehension - allows you to generate this same list in just one line of code.
# it combines the for loop and the creation of new element into one line, and appends each new element

# NOTE - no colon is used at the end opf the for statement

# list comprehension
squares = [value**2 for value in range(1,13)]
print(squares)

# descriptive variable name
# define the expression for the values you want to store in a new list
# for loop to generate the numbers you want to feed into the expression

