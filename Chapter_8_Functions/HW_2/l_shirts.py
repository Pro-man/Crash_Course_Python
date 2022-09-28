# Nathan Reid
# Aug. 29th, 2022
# Modify the make_shirt() function so that shirts are large
# by default with a message that reads 'I love Python.' 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size 
# with a different message. 

# create function
def make_shirt(size='large', message='i love python'):
    """Display information about the size of shirt
    and message printed on it."""
    print("The size of this shirt is " + size + ".")
    print("The shirt design says: " + message.title() + "!")

# default values
make_shirt()

# keyword argument
make_shirt(size='medium')
make_shirt(size='x-large', message='time to master your skills. love learning')