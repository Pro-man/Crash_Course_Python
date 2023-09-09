# Nathan Reid
# Sept. 11th, 2022
# Write a while loop that asks people why they like programming.
# Each time someone enters a reason, add their reason to a file
# that stores all the responses. 

filename = 'reason.txt'

active = True

with open(filename, 'a') as file_object:
    while active:
        response = input("Why do you like to program? ")
        file_object.write(response + "\n")

        # option to end the while loop
        if response == 'done':
            active = False
    