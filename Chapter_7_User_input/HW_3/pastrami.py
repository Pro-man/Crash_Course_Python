# Nathan Reid
# Aug. 27, 2022
# Using the list sandwich_orders, make sure the sandwich 'pastrami' appears in 
# the list at least three times.
# Add code near the beginning of your program to print a message saying the deli
# has run out of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches. 

# list
sandwich_orders = ['pastrami','turkey', 'tuna','pastrami', 'roast chicken', 'brisket', 'pastrami','ham']

# empty list
finished_sandwiches = []

print("The deli has run out of pastrami.")
 
while 'pastrami' in sandwich_orders:
    # remove 'pastrami from list and make sure none get into the new list
    sandwich_orders.remove('pastrami')
    
    
for order in range(len(sandwich_orders)):  
    # put popped item in a variable
    move = sandwich_orders.pop()
        
    # insert newly popped item in empty list
    finished_sandwiches.append(move)
    
# new list
print(finished_sandwiches)  










