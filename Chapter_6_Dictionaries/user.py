# Nathan Reid
# Aug. 23, 2022
# Dictionaries can contain large amounts of data. 
# Dictionaries can be used to store information in a variety of ways.

# dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}


#  for loop to iterate through dictionary
# create two variable names to store the pairs
# items() returns a list of key-value pairs.
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)