# Nathan Reid
# Sept. 13th, 2022
# Use the count() method to find out how many times a word or phrase 
# appears in a string. Notice that converting the string to lowercase 
# using lower() catches all appearances of the word you're looking for,
# regardless of how it's formatted.
# Write a program that reads the files and determines how many times the word
# 'the' appears in each text. 


# function definition with a list as a parameter
def count_words(filenames):
    """Read the files and determine how many times the word 'the' appears in each text."""

    try:
        with open(filenames) as f_obj:
            books = f_obj.read()
    except FileNotFoundError:
        print("We did not find that book.")
    else:
        # change all the text to lower case and count the word 'the' 
        word = books.lower().count('the')
        print(" The book " + filename.title() + " has " + str(word) + " - 'the's" + " in it.")


filenames = ['little_women.txt', 'moby_dick.txt']
# loop through list of books
for filename in filenames:
    count_words(filename)
