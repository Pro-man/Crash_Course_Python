# Nathan Reid
# Sept. 13th, 2022
# Modify your except block to fail silently if either file is missing.


# files
filenames = ['cats.txt', 'dogs.txt']


def read(filenames):
    """Read files and print contents of the files."""
    try:
        with open(filenames) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

# loop through the files
for filename in filenames:
    read(filename)