# Nathan Reid
# Sept. 14, 2022

# NOTE - json.load() to read the list back into memory


import json 


filename = 'numbers.json'
# open file
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

# NOTE - json.load() function to load the information stored in numbers.json
#  and we store it in the variable numbers.

