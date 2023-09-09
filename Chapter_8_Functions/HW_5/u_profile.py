# Nathan Reid
# Sept. 2nd, 2022
# Build a profile of yourself by calling build_profile().
# Using your first and last names and three other key-value pairs that describe you..

#create function definition with arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing a few things about yourself."""
    # create empty dictionary
    profile = {}
    # create keys:values
    profile['first_name'] = first
    profile['last_name'] = last
    # iterate through dictionary
    for key, value in user_info.items():
        profile[key] = value
    return profile

me_profile = build_profile('nathan', 'reid', weight='163', hair_color ='brown', location='virginia')

print(me_profile)