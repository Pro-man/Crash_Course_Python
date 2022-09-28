# Nathan Reid
# Aug. 25th, 2022 
# Modify your program so each person can have more than one favorite number.
# Then print each person's name along with their favorite numbers. 

# dictionary
numbers = {
    'Shantae': [39, 27],
    'E.J.': [31, 25],
    'T': [48, 4],
    'Shannon': [54, 7],
    'Skip': [70, 63],
}

# for loop into the dictionary to have access to the keys and values
for key, value in numbers.items():
    # display the key
    print("\n" + key + " favorite numbers are: ")
    # since the values are list loop in them and print the integers
    for val in value:
        print(val)
    