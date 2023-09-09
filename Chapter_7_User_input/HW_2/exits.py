# Nathan Reid
# Aug. 26, 2022
# write a different version of movie.py
# Use a conditional test in the while statement to stop the loop
# Use an active variable to control how long the loop runs
# Use a break statement to exit the loop when the user enter a 'quit' value

# ask for the users age
prompt = "What is your age? "

# create flag
active = True
# while loop
while active:
    # set the variable of the input
    age = input(prompt)
    # condition to see if age equals the 'quit' string
    if age != 'quit':
        # change the string input to an integer
        age = int(age)
        if age < 3:
            print("The cost of your ticket is free.")
        elif age >= 3 and age <= 12:
            print("The cost of your ticket is $10.")
        elif age > 12:
            print("The cost of your ticket is $15.")
    
    # condition to see if age equals the 'quit' string
    if age == 'quit':
        break

# NOTE - Had trouble on this but I got it. Needed to think about the logic. 