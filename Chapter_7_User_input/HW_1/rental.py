# Nathan Reid
# Aug. 26th, 2022
# Write a program that asks the user what kind of rental car they
# would like. Print a message about the car, 
# such as "Let me see if I can find you a Subaru."

# prompt
prompt = "What kind of rental car would you like? "

# put the prompt in a variable
rental = input(prompt)

# display prompt result
print("Let me see if I can find you a " + rental.title() + ".")

