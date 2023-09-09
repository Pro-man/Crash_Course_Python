# Nathan Reid
# Aug. 26th, 2022
# Ask the user for a number, and then report whether the 
# number is a multiple of 10 or not. 

# Give directions and prompt
prompt = "Let's see if a number is a multiple of 10.\n"
prompt += " \nGive me a number. "

# put prompt in a variable
number = input(prompt)
# change the string variable to a number
number = int(number)
# conditional test - divide the number by 10 remainder 0
if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print("This number is NOT a multiple of 10.")