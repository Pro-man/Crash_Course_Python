# Nathan Reid
# Aug. 17th, 2022

# Print the message, The first three items in the list are: 
# Then use a slice to print the first three items from the list.

# Print the message, Three items from the middle of the list are: 
# Then use a slice to print the middle three items from the list.

# Print the message, The last three items in the list are: 
# Then use a slice to print the last three items from the list.

# list
players = ['charles', 'martina', 'michael', 'florence', 'eli','lewis']

print("The first three items in the list are: ")
print(players[0:3])

print("Three items from the middle of the list are: ")
print(players[1:4])

print("The last three items in the list are: ")
print(players[-3:])
# or
print(players[3:])
# or
print(players[3:6])