# Nathan Reid
# Aug. 29th, 2022
# Passing Arguments

# Positional arguments - need to be in the same order the parameters were written

# Keyword arguments - each argument consists of a variable name and a value;
    # and lists and dictionaries of values.

# NOTE - Python must match each argument in the function call with a parameter in 
#   in the function definition. 

# function with parameters
def describe_pet(animal_type, pet_name):
    # docstring
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# function call with arguments
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# NOTE - You can call a function as many times as needed.
# NOTE - You can use as many positional arguments as you need in your function.

# NOTE - keyword argument is a name-value pair that you pass to a function.
describe_pet(animal_type='cat', pet_name='louis')
describe_pet(pet_name='prince', animal_type='bird')

# NOTE - Keyword arguments free you from having to worry about 
#   correctly ordering your arguments in the function call, and 
#   they clarify the role of each value in the function call.

# NOTE - When using keyword arguments, be sure to use the exact names of the paramenters
#   in the function's definition. 

# DEFAULT VALUE
# NOTE - the order of the parameters in the function definition had to be changed. ^^^^^^^ ^^^^^^ ^^^^^^
# Its unnecessary to specify a type of animal as an argument. 
def describe_schnauzer(pet_name, animal_type='dog'):
    # docstring
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# function call with keyword argument
describe_schnauzer(pet_name='prince')
describe_schnauzer(pet_name='william',animal_type='hamster')

# NOTE - When you use default values, any parameter with a default value needs to be listed
# after all the parameters that don't have default values. This allows Python to continue
# interpreting positional arguments correctly. 