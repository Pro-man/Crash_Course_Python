# Nathan Reid
# Sept. 2nd, 2022


# create function with parameter
def greet_users(names):
    # docstring
    """Print  a simple greeting to each user in the list."""
    # for loop to iterate through the list
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
