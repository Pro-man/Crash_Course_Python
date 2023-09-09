# Nathan Reid
# Sept. 1st, 2022
# Call the function make_great() with a copy of the list of magicians' names.
# The orginal list will be unchanged.
# Return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original
# names and one list with the Great added to each magician's name.

# function defition
def make_great(magicians):
    """Return and store a new list of magician names."""
    # create empty list
    for new in magicians[:]:
        trick = 'the Great ' + new
        new_magic.append(trick)
    return new_magic 




def show_magicians(magicians):
    """Display the names of the magicians of each list."""
    # for loop
    print("Original List")
    for magician in magicians:
        print(magician)

    print("\nCopy list")
    for magic in new_magic:
        print(magic)


new_magic = [ ]
magicians = ['teller', 'blaine', 'houdini']
make_great(magicians)
show_magicians(magicians)


# Had trouble with this