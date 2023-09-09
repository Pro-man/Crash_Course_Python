# Nathan Reid
# Aug. 12, 2022
# Adding Whitespaces to strings with tabs or newline
# Stripping whitespace

print("Python")

# tab - to add a tab to your text use \t
print("\tPython")

# newline - add a newline in a string, use the character combination \n
print("Languages:\nPython\nC\nJavaScript")

# combine tabs and newlines in a single string
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Python detects the extra space in 'python ' and considers it
#   significant unless you tell it otherwise.
# Compare two strings to determine whether they are same.
# One important instance might involve checking people's 
#  usernames when they log into a website. 

# To ensure that no whitespace exists at the right end of a string, 
# use the rstrip() method.

favorite_language = 'python '
print(favorite_language)

favorite_language.rstrip()
print(favorite_language)

# To remove the whitespace from the string permanently, 
# you have to store the stripped value back into the variable

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

# To remove the whitespaces from the string,
#  you strip the whitespace from the right side of the string
#  and then store that value back in the original variable

favorite_language = ' python  '
# right side strip of space
favorite_language = favorite_language.rstrip()
print(favorite_language)

# left side strip of space
favorite_language = favorite_language.lstrip()
print(favorite_language)

# strip whitespaces on both sides
favorite_language = favorite_language.strip()
print(favorite_language)
