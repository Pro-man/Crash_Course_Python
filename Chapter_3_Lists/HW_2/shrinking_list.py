# Nathan Reid
# Aug. 14th, 2022
# You have space for only two guests.
# Add a new line that prints a message saying that you can invite only two people to dinner.
# Use pop() to remove guests. Each time you pop print a message letting the person know you're sorry
# Print a message to the two remaining guests letting them know they are still invited
# Use del statement to remove the last two names from your list, print empty list



# current list
guests = ['Malcolm X', 'Grandma B', 'James Baldwin', 'George Washington Carver', 'Nipsey Hussle', 'Bob Marley']
# two guest list
uninvite = ", unfortunately I can only invite two guest now."
# inform all guests of the news
print(guests[0] + uninvite)
print(guests[1] + uninvite)
print(guests[2] + uninvite)
print(guests[3] + uninvite)
print(guests[4] + uninvite)
print(guests[5] + uninvite)

# pop() the guest from the list
# reminder - the list gets shorter as you pop and the indexes positions shrink
less_1 = guests.pop(0)
less_2 = guests.pop(1)
less_3 = guests.pop(2)
less_4 = guests.pop(-1)

# message
message = ", I am sorry you are uninvited from the party."

# inform guest they are uninvited
print(less_1 + message)
print(less_2 + message)
print(less_3 + message)
print(less_4 + message)

# print new version of list
print(guests)

# still invited
message_1 = " you are still invited to my party!"

# inform remaining guest they are still invited
print(guests[0] + message_1)
print(guests[1] + message_1)

# remove last items in list
del guests[0]
# the list is shrinking as well as the indexes. there is no longer an index 1
del guests[0]

print(guests)

