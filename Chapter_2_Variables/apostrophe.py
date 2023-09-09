# Nathan Reid
# Aug. 12, 2022
# Avoiding Syntax Errors with strings


# Syntax error occurs when Python doesn't recognize
#  a section of your program as valid Python code. 

message = "One of Python's strengths is its diverse community."
print(message)

# If you use signle quotes, Python can't identify where the string should end.

#  ----------
# message = 'One of Python's strengths is its diverse community.'
# print(message)

# File "apostrophe.py", line 14
#     message = 'One of Python's strengths is its diverse community.'
#                              ^
# SyntaxError: invalid syntax