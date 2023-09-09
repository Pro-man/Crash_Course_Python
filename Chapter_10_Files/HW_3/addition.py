# Nathan Reid
# Sept. 12, 2022
# Write a program that prompts for two numbers.
# Add them together and print the result.
# Catch the ValueError if either input value is not a number,
# and print a friendly error message.
# Test your program by entering two numbers and then by entering some text instead
# of a number.

print("Give us two numbers.")
print("Enter 'q' to quit.\n")

active = True

while active:
    f_num = input("What is your first number: ")
    if f_num == 'q':
        # active = False - this allows the program to continue and end once the second iinput is done
        break
    s_num = input("What is your second number: ")
    try:
        add = int(f_num) + int(s_num)
    except ValueError:
        print("Input value is not a number. Please, enter a number.")
    else:
        print(add)

    
        