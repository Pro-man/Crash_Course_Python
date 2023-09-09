# Nathan Reid
# Sept. 2nd, 2022
# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function
# call provides, and it should print a summary of the sandwich that is being ordered.
# Call the function three times, using different arguments each time.

# function definition with arbitrary number of arguments
def make_sandwich(*toppings):
    """Print a list of toppings on a person's sanwich."""
    print("Hello, here is a summary of your sandiwch items: ")
    print(toppings)
    

# call funtion with positional arguments
make_sandwich('wheat bread', 'pastrami','mustard','provolone','red onions')
make_sandwich('rye bread', 'chicken','avocado','green peppers', 'chipotle mayo')
make_sandwich('ciabatta bread', 'briskets', 'black pepper', 'salt', 'grilled onions','gouda cheese')