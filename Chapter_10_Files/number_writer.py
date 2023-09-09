# Nathan Reid
# Sept. 14th, 2022
# JSON

# NOTE - JSON module allows you to dump simple Python data structures into a file
# and load the data from that file the next time the programs runs.
# Use JSON to share data between different Python programs

# JSON - JavaScript Object Notation

# NOTE - json.dump() function takes two arguments: piece of data, a file object it can use to store the data

import json 

# list
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
# open file and write to it
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)