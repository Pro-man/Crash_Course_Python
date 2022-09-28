# Nathan Reid
# Aug. 13, 2022
# str() function

#  ------------
# age = 23
# message = "Happy " + age + "rd Birthday!"
# print(message)

# Traceback (most recent call last):
#   File "birthday.py", line 7, in <module>
#     message = "Happy " + age + "rd Birthday!"
# TypeError: can only concatenate str (not "int") to str

# TypeError - Python can't recognize the kind of information you're using

# --------------

age = 23
# numbers variable
message = " Happy " + str(age) + "rd Birthday!"
# convert number into a string anf place in a variable
print(message)


# Integers
# Division of integers in Python results in an integer with 
# remainder truncated. The remainder is simply ommitted.

# Make sure that at least one of the numbers is a float.

print(3/2)
print(3.0 / 2)
print(3 / 2.0)
print(3.0 / 2.0)