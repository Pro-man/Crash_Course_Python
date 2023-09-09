# Nathan Reid
# Aug. 28th, 2022
# Write a function called favorite_book() that accepts are 
# parameter, title. The function should print a message, such as One
# of my favorite books is Alice in Wonderland. Call the function, making sure
# to include a book title as an argument in the function call. 

# function with paramenter
def favorite_book(title):
    """Inform what is my favorite
    book."""
    print("One of my favorite books is " + title.title() + ".")
    # use parameter within function print statement

# call the function and put the argument in the ()
favorite_book("charlotte's web")