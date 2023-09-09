# Nathan Reid
# Aug. 27, 2022
# Filling a dictionary with user input

# NOTE - You can prompt for as much input as you need in each pass through a 
# while loop.

# empty dictionary
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

# while loop
while polling_active:
    # Prompt for the person's name and response
    # key 
    name = input("\nWhat is your name? ")
    
    # value
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the response(both inputs) in the dictionary
    # NOTE - Make it into a key-value pair here
    responses[name] = response

    # Key of dictionary - to see what the key is
    n = responses.keys()
    print(n)
   
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
# Polling is complete. Show the results.
print("\n---Poll Results---")
for name,response in responses.items():
    print(name + " would like to climb " + response + ".")

