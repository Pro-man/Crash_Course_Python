# Nathan Reid
# Sept. 2nd, 2022
# Put the functions for the example printing_models.py in a separate file
# called printing_functions.py.
# Write an import statement at the top of printing_models.py and modify
# the file to use the imported functions.

# import functions
import printing_functions

# list
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# empty list
completed_models = []

# call the function with list as positional arguments > no quotation marks needed because they are lists
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)