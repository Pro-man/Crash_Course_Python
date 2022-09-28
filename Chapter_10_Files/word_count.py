# Nathan Reid
# Sept. 12, 2022
# working with multiple files

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
    else:
        # count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


# filename = 'alice.txt'
# function call with a positional argument
# count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


# NOTE - Sometimes you'll want the program to fail silently
# when an exception occurs and continue on as if nothing happened.
# Tell Python to do nothing in the ecept block.

# NOTE - Use the pass statement also acts as a placeholder. 
