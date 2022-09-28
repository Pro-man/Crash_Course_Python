# Nathan Reid
# Aug. 17th, 2022
# Choose a version of foods.py, and 
# write two for loops to print each list of foods.

# lists
my_foods = ['pizza', 'falafel', 'carrot cake']

# copy list
your_foods = my_foods[:]

# add new food items to lists
my_foods.append("donut")
your_foods.append("chocolate cake")

print("My favorite foods are below:")
for food in my_foods:
    print(food.title())

print("\nYour favorite foods are below:")
for food in your_foods:
    print(food.title())