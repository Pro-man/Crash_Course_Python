# Nathan Reid
# Aug. 27, 2022
# While loop with lists and dictionaries

# To keep track of many users abd pieces of information, we'll 
# need to use lists and dictionaries with a while loop

# Using a while loop with lists and dictionaries allows you to collect,
# store, and organize lots of input to examine and report on later. 

# Start with users that need to be verified,
#   and an empty list to hold confirmed users
unconfirmed_users = ['alice','brian','candace']

confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#   Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# When the list of unconfirmed users is empty, the loop stops and the list of confirmed users 
# is printed