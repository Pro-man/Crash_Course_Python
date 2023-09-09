# Nathan Reid
# Sept. 14, 2022
# Writing a program that greets a user whose name has already been stored. 

import json 

filename = 'username.json'

# open file
with open(filename) as f_obj:
    # read the file back, remember the user input and store in variable
    username = json.load(f_obj)
    # print the variable
    print("Welcome back, " + username + "!")
