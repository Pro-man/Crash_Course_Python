# Nathan Reid
# Aug. 17th, 2022
# slicing a list

# NOTE - To make a slice, specifiy the index of the first and last
# elements you want to work with.

# list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# slice the list - list name[ first index, second index]
print(players[0:3])
print(players[1:4])

# NOTE - If you omit the first index in a slice, 
# Python automatically starts your slice at the beginning of the list
print(players[:4])

# NOTE - You can omit the second index if you 
# want to include the end of the list
print(players[2:])

# NOTE - Slicing allows you to output all of the elments from any point
# in your list to the end regardless of the length of the list. 
# you can output any slice from the end of the list
print(players[-3:])

# ['michael', 'florence', 'eli']

# NOTE - You can use a slice in a for loop if you want to loop through a subset
# of the elements in a list.
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())




