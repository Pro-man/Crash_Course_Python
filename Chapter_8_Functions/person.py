# Nathan Reid
# Aug. 29th, 2022
# Return a Dictionary

# function definition with parameters
def build_person(first_name, last_name):
    # docstring
    """Return a dictionary of information about a person."""
    # variable with a dictionary in it
    person = {'first': first_name, 'last': last_name}
    # print(person) - print statement
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# build_person('jimi', 'hendrix')


# function with default valut at the end in paramenter
def build_human(first_name, last_name, age=''):
    # docstring
    """Return a dictionary of information about a person."""
    # variable with a dictionary in it
    person = {'first': first_name, 'last': last_name}
    # conditional test
    if age:
        # add age key-value pair and put in the same name as the default value
        person['age'] = age
    # print(person) - print statement
    return person

musician = build_human('jimi', 'hendrix', age=27)
print(musician)