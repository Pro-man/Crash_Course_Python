# Nathan Reid
# Aug. 31st, 2022
# Make a list of magician's names. 
# Pass the list to a function called show_magicians(), 
# which prints the name of each magician in the list.

# create function with list as a parameter.
def show_magicians(magicians_names):
    """
    Print the magician names in the list.
    """
    for magician in magicians_names:
        # magic = "Let me see a magic trick Magician " + magician.title() + "!"
        print(magician)

# list
magicians_names = ['merlin', 'david', 'genie']
# call definition with list as the positional argument
show_magicians(magicians_names)
