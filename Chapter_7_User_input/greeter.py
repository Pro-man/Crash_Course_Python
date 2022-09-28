# Nathan Reid
# Aug. 26, 2022
# Writing clear prompts

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# NOTE - You can store your prompt in a variable and pass that variable
# to the input() function. This allows you to build your prompt over several lines.

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

# put prompt in variable
name = input(prompt)
# print the prompt entry
print("\nHello, " + name + "!")
