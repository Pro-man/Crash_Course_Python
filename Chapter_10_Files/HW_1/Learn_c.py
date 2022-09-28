# Nathan Reid
# Sept. 11th, 2022
# Use replace() method to replace any word in a string with a different word.
# Read in each line from the file you just created, learning_python.txt
# and replace the word Python with the name of another language.
# Print each modified line to the screen.

page = 'learning_python.txt'

with open(page) as file_object:
    for line in file_object:
        change = line.replace('Python', 'JavaScript')
        print(change)
