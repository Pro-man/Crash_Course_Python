# Nathan Reid
# Aug. 12, 2022
# strings

name = 'ada lovelace'
print(name.title())

# method title appears after the variable in the print()

# A method is an action Python can perform on a piece of data.
# Every method is followed by a set of () ,
#  because methods often need additional information to do their work.

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# The lower() method is useful for storing data.
# Convert strings to lowercase before storing them. 

# -------- Combining or Concatenating Strings -------

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + " " + last_name

print(full_name)

# You can use concatenation to compose complete 
# messages using the information you've stored in a variable.

print("Hello, " + full_name.title() + "!")

# You can use concatenation to compose a message and 
# then store the entire message in a variable.

message = "Hello, " + full_name.title() + "!" 
print(message)

