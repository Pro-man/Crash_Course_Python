# Nathan Reid
# Aug. 30th, 2022
# Return value 

# Function with parameters
def get_formatted_name(first_name, last_name):
    # docstring
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    # calling line
    return full_name.title()

# function call with positional arguments put in a variable
musician = get_formatted_name('jimi', 'hendrix')
# variable
print(musician)

# NOTE - When you call a function that returns a value, you need to provide
# a variable where the return value can be stored. 


# Argument Optional -- - -- - - - use an empty string and make it last parameter
# Function with parameters
def get_formatted_full_name(first_name, last_name, middle_name=''):
    # docstring
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    # calling line
    return full_name.title()


# function call with positional arguments put in a variable
musician = get_formatted_full_name('jimmy', 'hendrix')
print(musician)

musician = get_formatted_full_name('john', 'hooker', 'lee')
print(musician)

# NOTE - You can use default values to make an argument optional.
# We can give the middle_name argument an empty default value and 
#  ignore the argument unless the user provides a value.
# We set the default value of middle_name to an empty string and move it
#   to the end of the list of parameters.

# Python interprets non-empty strings as True
# Returned to the function call line where it's stored in the variable musician and printed.
# Formatted name is returned to the calling line where it's stored in musician and printed.
# We have to make sure the middle name is the last argument passed so Python will match 
#   up the potential arguments correctly
