# Nathan Reid
# Aug. 20th, 2022 
# if-elif-else 

# NOTE - To test more than two possible situations use the if-elif-else
# Python executes only one block in an if-elif-else chain.
# It runs each conditional test in order until one passes. When a tests
# passes, the code following that test is executed and python skips the rest of the tests.

# set the variable
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# more efficient way

age = 25
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# NOTE - You can use as many elif blocks in your code as you like.

age = 40
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")


# NOTE - Python does not require an else block at the end of an if-elif
# chain. Sometimes it is clearer to use an additional elif statement that
# catches the specific condition of interest.

age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# NOTE - The else block is a catchall statement.

# NOTE - If you have a specific final condition you are testing for,
# consider using a final elif block and omit the else block. 

# NOTE - if-lif-else is only appropriate to use when you just
# need one test to pass.