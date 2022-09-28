# Nathan Reid
# Sept. 2nd, 2022
# Using a program you wrote that has one function in it,
# store that function in a separate file.
# Import the function into your main program file, and 
# call the function using each of these approaches.

# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from modle_name import *

# 1
import greet_u
# list
usernames = ['hannah', 'ty', 'margot']
# call function with argument
greet_u.greet_users(usernames)
print("----")

# 2
from greet_u import greet_users
# list
usernames = ['John', 'ty', 'margot']
# call function with argument
greet_users(usernames)
print("----")

# 3
from greet_u import greet_users as fn 
# list
usernames = ['hannah', 't', 'lewis']
# call function with argument
fn(usernames)
print("----")

# 4
import greet_u as mn
# list
usernames = ['grandma', 'eva', 'margot']
# call function with argument
mn.greet_users(usernames)
print("----")

# 5
from greet_u import *
# list
usernames = ['g', 'eve', 'mary']
# call function with argument
greet_users(usernames)
