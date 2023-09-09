# Nathan Reid
# Aug. 27, 2022

# Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order,
# "I made your tuna sandwich"
# after all the sandwiches have been made, print a message listing each sandwich that was made

# list
sandwich_orders = ['turkey', 'tuna', 'roast chicken', 'brisket']
# empty list
finished_sandwiches = []

# loop through the list of sandwiches the length of the list
for order in list(sandwich_orders):
    # put popped item in a variable
    done = sandwich_orders.pop()
    # insert newly popped item in empty list
    finished_sandwiches.append(done)
    print(" I made your " + order.title() + " sandwich!")

# now empty list is full
print(finished_sandwiches)
# full list is empty now
print(sandwich_orders)

# Traceback (most recent call last):
#   File "deli.py", line 28, in <module>
#     order.title()
# AttributeError: 'int' object has no attribute 'title'