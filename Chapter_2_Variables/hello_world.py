# Nathan Reid
# Aug. 12, 2022
# Variables and Simple Data Types

print("Hello Python world")

# Put print message into a variable
# The message in orange is syntax highlighting
message = "Hello Python world!"
# Print is the name of the function
# Every variable holds a value, which is the information associated
#  with that variable
print(message)

message_2 = "Hello Python Crash Course world!"
print(message_2)
# You can change the value of a variable in your program at any time,
#  Python will always keep track of its current value.

# Variables names can contain only letters, numbers, and underscores.
# Variables can not start with a number.
# Spaces are not allowed in variables names, but underscores can be used to separate
# Avoid using Python keywords and function names as variables names
# Variable names should be short but descriptive.
# Becareful using lowercase letter l and uppercase letter O,
#   they could be confused with the numbers 1 and 0.

# ----> message_2 = "Hello Python Crash Course reader!"
# ----> print(mesage)

#Traceback is a record of where the interpreter ran into trouble
#  when trying to execute your code

# Traceback (most recent call last):
#   File "hello_world.py", line 29, in <module> (output)
    # print(mesage)                             (error)
# NameError: name 'mesage' is not defined       (error type)

# Python does not spellcheck your code but it ensures that 
#  variable names are spelled consistenly.