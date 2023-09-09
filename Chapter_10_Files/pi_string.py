# Nathan Reid
# Sept. 9th, 2022
# Working with a file's contents

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# variable create to hold the digits of pi
pi_string = ''
# for loop will add each line of digits to pi_string
# and removes newline character from each line. 
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# NOTE - When Python reads from a text file, 
# it interprets all text as a string.

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    # make a list of the information
    lines = file_object.readlines()

pi_string = ' '
# for loop through the list called lines
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
