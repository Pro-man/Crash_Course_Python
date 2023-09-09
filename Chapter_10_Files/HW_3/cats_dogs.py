# Nathan Reid
# Sept. 13th, 2022
# Make two files, cats.txt and dogs.txt.
# Store at least three names of cats in the first file
# and three names of dogs in the second file.
# Write a program that tries to read these files and print
# the contents of the file to the screen

# files
filenames = ['cats.txt', 'dogs.txt']


def read(filenames):
    """Read files and print contents of the files."""
    try:
        with open(filenames) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        message = "Sorry, the file " + filename + " is missing."
        print(message)
    else:
        print(contents)

# 
for filename in filenames:
    read(filename)

