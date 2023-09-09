# Nathan Reid
# Sept. 11th, 2022
# Write a program that prompts the user for their name.
# When they respond, write their name to a file called guest.txt.

name = input("What is your name? ")

book = 'guest.txt'

with open(book,'w') as file_object:
    file_object.write(name)