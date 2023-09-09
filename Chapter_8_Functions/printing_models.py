# Nathan Reid
# Aug. 31, 2022
# Modifying a list in a function

# NOTE - When you pass a list to a function, the function can modify the list.
# any changes made to the list inside the function's body are permanent.

# Start with some designs that need to be printed.
# list
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# empty list
completed_models = []

# ssimulate printing each design, until none are left.
# Move each design to completed_models after printing.
# while loop
while unprinted_designs:
    # pop items from the full list
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    # move items from one list to another
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

print("-----")

# function with lists as parameters
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        # move items from one list to another
        completed_models.append(current_design)

# function with list as a parameter - pass the list to this function ***
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model) 

# list
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# empty list
completed_models = []

# call the function with list as positional arguments > no quotation marks needed because they are lists
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# NOTE - Every function should have one specific job. 
# NOTE - You can always call a function from another function, 
# which can be helpful when splitting a complex task into a series of steps.

# Preventing a function from modifying a list
# function_name(list_name[:]) -> You can address the issue by passing the function a copy of the list, not the original.
# print_models(unprinted_designs[:], completed_models)