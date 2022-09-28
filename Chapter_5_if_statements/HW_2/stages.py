# Nathan Reid
# Aug. 20th, 2022
# if-elif-else that determines a person's stage of life.
# Set a value for the variable age and then:
# If the person is less than 2 yrs old, print a message that the person is a baby.
# If the person is at least 2 yrs old but less than 4, print a message that the person is a toddler.
# If the person is at least 4 yrs old but less than 13, print a message that the person is a kid.
# If the person is at least 13 yrs old but less than 20, print a message that the person is a teenager.
# If the person is at least 20 yrs old but less than 65, print a message that the person is a adult.
# If the person is 65 yrs old or older, print a message that the person is a elder.


# set a value to a variable
age = 1
# age = 3
# age = 6
# age = 15
# age = 20
# age = 65
# age = 70
# conditional test to check person's age
if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are a adult.")
elif age >= 65:
    print("You are a elder.")