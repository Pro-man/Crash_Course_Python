# Nathan Reid
# Aug. 20th, 2022 
# if statements

# if conditional test:
    # do something

# store
# check
# execute

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# NOTE - You can put any conditional test in the first line and 
# just about action in the indented block following the test.
# If the conditional test evaluates to True, Python executes the code
# following the if statement. 

# NOTE - All indented lines after an if statement will be executed if 
# the test passes, and the entire block of indented lines will be 
# ignored if the test does not pass.

# NOTE - (if-else) Take one action when a conditional test passes and a different
# action in all other cases. The else statement allows you to define an action
# or set of actions that are executed when the conditional test fails.

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# NOTE - The if-else structure works well in situations in which you want
# Python to always execute one of two possible actions.


