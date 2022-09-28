# Nathan Reid
# Aug. 26th, 2022
# Modulo Operator

# prompt
number = input("Enter a number, and I'll tell you if it's even or odd: ")
# change string to a number
number = int(number)

# conditional test to see if number is even
# divide by two
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# even numbers are always divisible by two