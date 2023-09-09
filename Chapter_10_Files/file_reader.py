# Nathan Reid
# Sept. 11th, 2022
# Reading from a file

# NOTE - Exceptions - are special objects
# NOTE - JSON - module, which allows you to save user data 
# so it isn't lost when your program stop running.

# use open function with one argument: 
# the name of the file you want to open.
# NOTE - Python store this object in file_object
# NOTE - The keyword (with) closes the file once access to it is no longer needed.
with open('pi_digits.txt') as file_object:
    # read() - reads the entire contents of the file and store it as a string in contents
    contents = file_object.read()
    print(contents.rstrip())

# rstrip() - removes the extra blank line at the bottom.

# open('file name') store as file_object / use keyword with
    # variable name = file_object.read()

# file path - tells Python to look in a specific location on your system.
# with open('text_files/filename.txt') as file_object:

# absolute path 
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:
# NOTE - in the open(variable) function and using the absolute path it is a variable 


# reading line by line
filename = 'hello.txt'

with open(filename) as file_object:
    # examine each line from a file one at a time with a for loop.
    for line in file_object:
        print(line.rstrip())

# Making a list of lines from a file
# NOTE - To retain access to a file's contents outside the with block,
#  you can store the file's lines in a list inside the block and then work 
# with that list.
filename = 'hello.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())