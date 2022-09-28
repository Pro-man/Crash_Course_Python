# Nathan Reid
# Sept. 15th, 2022
# The final listing for remember_you.py assumes either that the 
# user has already entered their username or that the program is running for the first time.
# We should modify it in case the current user is not the person who last used the program.
# Before printing a welcome back message in greet_user(), ask the user if
# this is the correct username. If it's not, call get_new_username() to get the correct username.

# Got help from only and the book.

# NOTE - need to take my time and think it through


import json

def get_stored():
    """Store username if available."""
    filename = 'digit.txt'
    try:
        with open(filename) as f_obj:
            user_n = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return user_n

def get_new_username():
    """Prompt for a new user."""
    user_n = input("What is your username? ")
    filename = 'digit.txt'
    with open(filename, 'w') as f_obj:
        json.dump(user_n, f_obj)
    return user_n


def greet_user():
    """Greet user by name."""
    user_n = get_stored()
    if user_n:
        # verifiy user
        correct = input("Are you " + str(user_n) + "? (y/n) ")
        if correct == 'y':
            print("Welcome back, " + str(user_n) + "!")
        else:
            user_n = get_new_username()
            print("We'll remember you when you come back, " + user_n + "!")
    else:
        user_n = get_new_username()
        print("We'll remember you when you come back, " + user_n + "!")

greet_user()

