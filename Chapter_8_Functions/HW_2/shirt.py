# Nathan Reid
# Aug. 29th, 2022
# Write a function called make_shirt() that accepts a size and text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments. 


# create function
def make_shirt(size, message):
    """Display information about the size of shirt
    and message printed on it."""
    print("The size of this shirt is " + size + ".")
    print("The shirt design says: " + message.title() + "!")

# positional argument
make_shirt('small', 'i love to program python')
# keyword argument
make_shirt(size='medium',message='drink plenty of water')