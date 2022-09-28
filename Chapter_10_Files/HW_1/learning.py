# Nathan Reid
# Sept. 11th, 2022
# Create a new txt file and summarizing what you learned in Python
# Start each line with the phase In Python you can ...Save the file as learning_python.txt
# in the same directory as your exercises from this chapter.
# Write a program that reads the file and prints what you wrote three times.
# Print the contents once by reading in the entire file, once by looping over file object,
# and once by storing the lines in a list and then working with them outside the with block.

#  entire file
with open('learning_python.txt') as file_object:
    code = file_object.read()
    print(code)

print("-------")

# once by looping over file object
page = 'learning_python.txt'

with open(page) as file_object:
    for line in file_object:
        print(line)

print("********")

# once by storing the lines in a list
with open(page) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())