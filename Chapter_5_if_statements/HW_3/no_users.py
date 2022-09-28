# Nathan Reid
# Aug. 21, 2022
# add an if test to admin.py to make sure the list of users is not empty
# if list is empty, print the message - We need to find some users!
# Remove all of the usernames from your list and make sure the correct message is printed

# create a list
users = ['curtis', 'tron', 'mel', 'bob', 'admin']

# for loop to loop through the list
# use range() function to iterate through complete list
for user in range(6):
    # check to see if any users are still in the list
    if users:
        print(len(users))
        # users.pop()
    # once there are no users the else block will execute
    else:
        print("We need to find some users!")


# Try to use this code just in case the list grows or decrease in indexes
# This code print the else block 5 times
# for user in range(len(users)):  

# This code prints nothing
# for user in users:


members = ['curtis', 'tron', 'mel', 'bob', 'admin']

# # for loop to loop through the list
# # use range() and len() functions to iterate through complete list by indexes
for member in range(len(members)):
#     # check to see if any users are still in the list
    if member: 
#         # get rid of the users in the list until there are none left
        members.pop()
#     # once there are no users the else block will execute
    else:
        print("We need to find some users!")