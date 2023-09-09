# Nathan Reid
# Aug. 26, 2022
# Write a loop that prompts the user to enter a series of pizza toppings until
# they enter a 'quit' value. As they enter each topping, print a message saying
# you'll add that topping to their pizza.


# Give directions to the user
prompt = "\nEnter in your favorite toppings on your pizza:  "

# Put the instructions into the input function and set the variable
toppings = input(prompt)
# create while loop
while toppings != 'quit':
    # Conditional test to see what value was entered by the user and should the program continue
    if toppings.lower() == 'quit':
        break
    else:
        print("You added " + toppings + " to you pizza.")
        
