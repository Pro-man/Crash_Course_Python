# Nathan Reid
# Aug. 27, 2022
# Write a program that polls users about their dream vacation.
# Write a prompt similar to 'If you could visit one place in the world, where would you go?'
# Include a block of code that prints the results of the poll.

# create an empty list
vacations = {}

# set the flag
dream = True

while dream:
    # key
    dreamer = input("What is your name? ")
    # value
    response = input("If you could visit one place in the world, where would you go? ")
    
    # Store the response(both inputs) in the dictionary
    # NOTE - Make it into a key-value pair here
    # vacations[name] = response
    # NOTE - connect the key and value together ^^^^^^^^^^^^^^^
    vacations[dreamer] = response

    # Key of dictionary - to see what the key is
    n = vacations.keys()
    print(n)
   
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        dream = False
        
# Polling is complete. Show the results.
print("\n---Poll Results---")
for dreamer,response in vacations.items():
    print(dreamer.title() + "'s dream vacation would be going to " + response.title() + "!")

print(vacations)