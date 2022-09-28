# Nathan Reid
# Aug. 31, 2022
# Passing a list

# create function with parameter
def greet_users(names):
    # docstring
    """Print  a simple greeting to each user in the list."""
    # for loop to iterate through the list
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

# list
usernames = ['hannah', 'ty', 'margot']
# call function with argument
greet_users(usernames)

# NOTE - When you pass a list to a function, the function gets direct access
#  to the contents of the list.