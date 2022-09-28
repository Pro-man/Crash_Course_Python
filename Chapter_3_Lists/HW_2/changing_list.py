# Nathan Reid
# Aug. 14th, 2022
# Modify your list, replacing the name of the guest who can't make it
# with the name of the new person you are inviting. Add a print statement
# at the end of the program stating the name of the guest who can't make it.
# Print a second set of invitation messages, one for each person who is still in your list.

# list
invites = ['Grandma B', 'Grandfather Cha', 'George Washington Carver']
# delete person from my list
# use the pop method to be able to use the delete item
guest = invites.pop(1)
# message informing this guest can't make it
no_guest = " can't make it to the party. I will be inviting a new guest."
print(guest + no_guest)

# add new guest at the end of the current list
invites.append('Nipsey Hussle')
# new list
print(invites)
# new message
new_party = ", we will have a private chef at the party on Saturday. They will be cooking all of your favorite dishes."
# display new invite messages
print(invites[-1] + new_party)
print(invites[0] + new_party)
print(invites[1] + new_party)

