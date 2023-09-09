# Nathan Reid
# Sept. 12, 2022
# Exceptions

# Exceptions - manage errors that arise during a programs's execution.
# Exceptions are handled with try-except blocks.

# NOTE - When you think an error may occur, you can write a try-except block to handle
# the exception that might be raised.

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# NOTE - If the code in the try block causes an error, Python looks for an except block
# whose error matches the one that was raised and runs the code in that block.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    # NOTE - the try block has the code that might cause an error
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

    # NOTE - The only code that should go in a try statement is code that might cause 
    # an exception to be raised. 

    # The except block tells Python what to do in case a certain exception arises
    #  when it tries to run the code in the try statement. 