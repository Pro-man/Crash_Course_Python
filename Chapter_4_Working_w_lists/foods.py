# Nathan Reid
# Aug. 17th, 2022
# copying a list

# NOTE - To copy a list, make a slice that includes the entire original list
# omitting the first index and the second index ([:]).

# list
my_foods = ['pizza', 'falafel', 'carrot cake']
# copy entire list
friend_foods = my_foods[:]
# add new food to each lists to prove there are two separate list
my_foods.append('cannoli')
friend_foods.append('ice cream')
# original list
print("My favorite foods are:")
print(my_foods)
# new list
print("\nMy friend's favorite foods are:")
print(friend_foods)

# This does not work.
# Both variables point to the same list
# There are no separate list with this code.

# friend_foods = my_foods