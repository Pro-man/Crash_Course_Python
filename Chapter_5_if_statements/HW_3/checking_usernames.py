# Nathan Reid
# Aug. 21, 2022
# Do the following to create a program that simulates how websites ensure that
# everyone has a unique username.
# Make a list of five or more usernames called current_users.
# Make another list of five usernames called new_users. Make sure one or two
# of the new usernames are also in current_users list.
# Loop through the new_users list to see if each new username has already been used.
# If it has, print a message that the person will need to enter a new username.
# If a username has not been used, print a message saying thatthe username is available.

# create lists
# list # 1
current_users = ['prince','snowy_bear','nate','x', 'money_man', 'thomas']
# list # 2
new_users = ['Money_MaN', 'NaTe','X', 'TonynaTor', 'Dean_List']

# use list comprehension to convert current users list items casing
present = [current.lower() for current in current_users]

# loop through the new list of users
for user in new_users:
    # convert new list item and compare to current users list
    if user.lower() in present:
        # username already in use
        print(user + ", will need a new username. - -")
    else:
        # if the item is available
        print("Username " + user + " is available.")




