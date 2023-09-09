# Nathan Reid
# Aug. 26, 2022
# A movie theater charges different ticket prices depending on a person's age.
# If a person is under the age of 3, the ticket is free;
# if they are between 3 and 12, the ticket is $10;
# if they are over age 12, the ticket is $15.
# Write a loop in which you can ask users their age, and then tell them the cost
# of their movie ticket. 

# ask for the users age
prompt = "What is your age? "

# while loop
while True:
    # set the variable of the input
    age = input(prompt)
    # change the string input to an integer
    age = int(age)
    # exit while loop with integer
    if age < 3:
        print("The cost of your ticket is free.")
    elif age >= 3 and age <= 12:
        print("The cost of your ticket is $10.")
    elif age > 12:
        print("The cost of your ticket is $15.")
    

# summary NOTE- the program is saying while true ask the user what is their age,
# turn the user input to am integer and test that integer to a condition before
# displaying the print statement
       
# NOTE - Had trouble on this !!!!!! But I got it. 
    
       