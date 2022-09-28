# Nathan Reid
# Sept. 14, 2022
# Saving and Reading User Generated Data

# import json 

# # user input
# username = input("What is your name? ")

# filename = 'username.json'

# with open(filename, 'w') as f_obj:
#     # store user input in 'f_obj' variable
#     json.dump(username, f_obj)
#     print("We'll remember you when you come back, " + username + "!")

import json 

# Load the username, if it has been stored previously
# Otherwise, prompt for the username and store it.

filename = 'username.json'

try:
    # open file and if file exist, read back username in memory
    with open(filename) as f_obj:
        # print message welcome back the user
       username = json.load(f_obj)
# if it is first time for user this section will run prompting user
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj) 
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
    