# Nathan Reid
# Aug. 21, 2022
# Make a list of five or more usernames, including admin
# Write code that will print a greeting to each user.
# If the username is admin, print a special greeting 
# - Hello admin, would you like to see a status report?
# Print a generic greeting - Hello Eric, thank you for logging in again.


# create a list
users = ['curtis', 'tron', 'mel', 'bob', 'admin']
# loop through the list
for user in users:
    # print a special message to admin
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again.")