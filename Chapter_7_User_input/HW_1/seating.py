# Nathan Reid
# Aug. 26th, 2022
# Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight,
# print a message saying they'll have to wait for a table.
# Otherwise, report that their table is ready. 

# prompt
number = input("How many people are in your dinner group? ")
# change string to a integer
number = int(number)

# conditional test
if number > 8:
    print("I'm sorry, you will have yo wait for a table.")
else:
    print("You table is ready")