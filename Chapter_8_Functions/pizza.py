# Nathan Reid
# Sept. 1st, 2022
# Pass an Arbitrary Number of Arguments

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# NOTE - the asterisk in the parameter name *toppings tell Python to make 
# an empty tuple called toppings and pack whatever values it receives into this tuple.

# Python packs the arguments into a tuple, even if the function receives only one value

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:    
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# NOTE - The parameter that accepts an arbitrary number of arguments must be placed
#       last in the function definition. Python matches positional and keyword arguments
#       first and then collect any remaining arguments in the final parameter. 

def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings:")
    for topping in toppings:    
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# NOTE - You can store your functions in a separate file called a module and then
# importing that module into your mail program.

# NOTE - An import statement tell Python to make the code in a module available in the 
# currently running program file. 

# NOTE - Storing your functions in a separate file allows you to hide the details of
# your program's code and focus on its higher level logic. It allows you to reuse functions
# in many different programs. 

# NOTE - A module is a file ending in .py

# *****  NOTE ******* Each function in the module is available through the following syntax:
# module_name.function_name()
