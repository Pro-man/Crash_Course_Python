# Nathan Reid
# Aug. 20th, 2022
# Write more tests
# one false / one true
# test for equality and inequality with strings
# tests using the lower() function
# numerical tests involving equality and inequality
    # greater than / less than / greater than or equal to / less than or equal to
# tests using the 'and' keyword and 'or' keyword
# test whether an item is in a list
# test whether an item is not in a list

# set the variable
truck = 'ford f-150 lighting'
print("Is truck == 'trailblazer'? I predict True.")
print(truck == 'ford f-15- lighting')

print("Is truck == 'trailblazer'? I predict False.")
print(truck == 'trailblazer')

# check for equality with lower() function
fitness = 'GYM'
print(fitness.lower() == 'gym')

# store
# comnvert == compare

# check for inequality 
health = 'eat healthy'
if health != 'run':
    print("You need to run too.")

# numerical tests
age = 27
print(age == 38)

if age != '50':
    print("I am still young.")

age = 18
print(age < 42)
print(age <= 19)
print(age > 14)
print(age >= 18)

print(age > 45 and age <= 18)
print(age < 14 or age >= 18)

# list
grandparents = ['ruth', 'cha', 'b','sherwood',]
# check for item in list
print('b' in grandparents)
# chek for item not in list
if 'aunt Eva' not in grandparents:
    print("This aunt was on my mother's side.")