# Nathan Reid
# Aug. 27, 2022
# break statement

# NOTE - To exit a while loop without running any remaining code in the loop
# regardless of the results of any conditional test, use the break statement.

# instructions to the user
prompt = "\nPlease, enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

# while loop
while True:
    # set the value to the input function
    city = input(prompt)
    # set the conditional test to exit the program
    if city.lower() == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
