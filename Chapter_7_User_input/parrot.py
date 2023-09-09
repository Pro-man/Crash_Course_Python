# Nathan Reid
# Aug. 26, 2022
# input function

# NOTE - Input() function pauses your program and waits for the user to enter
# some text. Once Python receives the user's input, it stores it in a variable
# to make it convenient for you to work with.

# NOTE - input() function takes one argument: the prompt, or instructions, that
# we want to display to the user so they know what to do.

# message = input("Tell me something, and I will repeat it back to you: ") ---
# print(message)----

# include a clear, easy-to-follow prompt that tells the user exactly what kind
#  of information you're looking for.

# set variable value
prompt = "\nTell me something, and I will repeat it back to you: "
# add to variable
prompt += "\nEnter 'quit' to end the program."

# empty variable - give initial value
# message = " "  ---
# while loop does not equal 'quit' run program 
# NOTE - 'quit' is case sentive. It has to be lowercase
# while message != 'quit': ----
    # reset the prompt value in the input function and new variable
    # message = input(prompt) ---
    # print(message)---

    # conditional test
    # if message != 'quit': ---
        # print(message) ----

# NOTE - If python has nothing to compare, it won't be able to continue running the program
# NOTE - Python reevaluates the condition in the while statement as long as the user has not
# entered the word 'quit'

# flag
active = True 
# while loop
while active:
    # set the variable and value with the input function
    message = input(prompt)
    # conditional test if-else  / 'quit' is case sensitive
    if message.lower() == 'quit':
        # change flag status - end program with false flag
        active = False
    else:
        print(message)

    # Tell programs to run while the flag is set to True and stop
    # running when any of several events sets the value of the flag to False.