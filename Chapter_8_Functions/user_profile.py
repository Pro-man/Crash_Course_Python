# Nathan Reid
# Sept. 2nd, 2022
# Using Arbitrary Keyword Arguments

# function definition
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    # create empty dictionary
    profile = { }
    # create key-value pair
    profile['first_name'] = first
    profile['last_name'] = last
    # loop through dictionary
    for key, value in user_info.items():
        profile[key] = value
    # return the dictionary to the function call line
    return profile

# call function / location and field and keys in user_info dictionary (Keyword arguments)
user_profile = build_profile('albert', 'einstein', location='princeton',field='physics')

print(user_profile)

# NOTE - double asterisks before the parameter **user_info cause Python to create an empty
# dictionary called user_info and pack whatever name-value pairs it receives into this dictionary. 
