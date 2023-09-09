# Nathan Reid
# Sept. 14th, 2022

import json

# def greet_user():
#     """Greet the user by name."""
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#             print("Well remember you when come back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")

# greet_user()

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

# NOTE - a function should either return the value your're expecting or it should return None

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    # put function into variable
    username = get_stored_username()
    # conditional test
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("Well remember you when come back, " + username + "!")


greet_user()

