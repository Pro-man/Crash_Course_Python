# Nathan Reid
# Aug. 28th, 2022
# Functions

# Functions are names blocks of code that are designed to do one specific job
# Store functions in separate files called modules 
# modules help organize your main program files

# function
# pass information to a function in the () called PARAMETER *****
def greet_user(username):
# body
# docstring
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

# function call
# Information in the function call () is called ARGUMENT *****
greet_user('jesse')
# Python expects you to provide a value for username each time you call it.

# def (function definition) - keyword that informs Python that you're defining a function.
# Tell Python the name of the function.
# Also, tells Python what kind of information the function needs to do its job.
#   the () holds that information.

# Docstrings describes what the function does.

# A function call Python to execute the code in the function. 
# To call a function, you write the name of the function, followed by any necessary informationin ()

# greet_user()
# TypeError: greet_user() missing 1 required positional argument: 'username'


# Function with While loop
def get_formatted_name(first_name, last_name):
    # docstring
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    # calling line
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input('First Name: ')
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

