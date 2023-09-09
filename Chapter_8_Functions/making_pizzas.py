# Nathan Reid
# Sept. 2nd, 2022
# Importing an Entire Module

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Importing specific functions
# NOTE - import a specific from a module
# --- from module_name import function_name

# NOTE - from module_name import function_0, function_1, function_2
# You can import as MANY functions as you want from a module by 
# separating each functions's name with a coma.

# NOTE - you don't need the dot notation when you call a function example  below

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# NOTE - Using as to Give a Function an Alias

# from module_name import function_name as fn

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# NOTE - Using as to Give a Module an Alias

import pizza as p 

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# import module_name as mn 


# NOTE - Importing All Functions in a Module
# You can tell Python to import every function in a module by using the asterisk(*) operator

from pizza import *

# You can call every function by name without using dot notation. Best not to use this with large modules. 

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')