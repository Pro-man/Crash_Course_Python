# Nathan Reid
# Aug. 14th, 2022
# Think of three more guest to invite to dinner.
# Use insert() to add one guest to the beginning of your list
# Use insert() to add one guest to the middle of your list.
# Use insert() to add one guest to the end of your list.
# Print a new set of invitation message, one for each person in your list.

# current guest list
guests = ['Grandma B', 'George Washington Carver', 'Nipsey Hussle']
# inform current guest we found a bigger table. 
# We can invite more people.
bigger_table = ", I found a bigger table. I am going to invite more guests."
# display messages
print(guests[-1] + bigger_table)
print(guests[0] + bigger_table)
print(guests[1] + bigger_table)



# add new guest to different sections of the list.
# print new verson of list to make sure the gues t were added.
guests.insert(0, 'Malcolm X')
guests.insert(2, 'James Baldwin')
guests.insert(5, 'Bob Marley')
print(guests)

# new message for all guests
new_message = ' come to my party. We are going to have fun and eat good.'

# display new message to all guest
print(guests[0]+ new_message)
print(guests[1]+ new_message)
print(guests[2]+ new_message)
print(guests[3]+ new_message)
print(guests[4]+ new_message)
print(guests[-1]+ new_message)