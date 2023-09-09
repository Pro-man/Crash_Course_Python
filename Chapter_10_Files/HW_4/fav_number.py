# Nathan Reid
# Sept. 15th, 2022
# Write a program that prompts for the user's favorite number.
# Use json.dump() to store this number in a file.
# Write a separate protgram that reads in this value and prints the messafe, 
# "I know your favorite number! It's  ."

# import JavaScript
import json

# filename to write to
filename = 'digit.json'

# prompt the user for their information
f_num = input("What is your favorite number? ")
# convert the information to an integar
number = int(f_num)

# open the file and write the input in the file and store it
with open(filename,'w') as file_object:
    # store the set number
    json.dump(f_num, file_object)
    print("I know your favorite number! It's " + str(number) + ".")
    