# Nathan Reid
# Sept. 1st, 2022
# write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician's name.
# Call show_magicians() to see that the list has actually been modified. 

# create function with list as a parameter.
def show_magicians(magicians_names):
    """
    Print the magician names in the list.
    """
    for magician in magicians_names:
        print(magician)


def make_great(magicians_names):
    """
    Print the magician names in the list.
    """
    new_names = []
    for magician in magicians_names:
        names = magician + " the Great"
        new_names.append(names)
    
    show_magicians(new_names)


# list
magicians_names = ['merlin', 'david', 'genie']
# call definition with list as the positional argument
show_magicians(magicians_names)
make_great(magicians_names)

# Had trouble with this



