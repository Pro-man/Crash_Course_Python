# Nathan Reid
# Sept. 15th, 2022
# use fav_number.py
# If the number is already stored, report the favorite number to the user.
# If not, prompt for the user's favorite number and store it in a file.
# Run the program twice to see that it works.


import json

# filename to write to
filename = 'digit.json'


try:
    with open(filename,'r', encoding='utf-8') as file_object:
        digit = json.load(file_object)
except FileNotFoundError:
    digit = input("What is your favorite number? ")
    with open(filename, 'w') as file_object:
        json.dump(digit, file_object)
        print("Your favorite number is stored.")
else:
    print("I know your favorite number! It's " + str(digit) + ".")


# NOTE - This happens when the file digit.json is empty.

# NOTE - The Python "json.decoder.JSONDecodeError: Expecting value: 
# line 1 column 1 (char 0)" occurs when we try to parse something that is not valid JSON as if it were. 
# To solve the error, make sure the response or the file is not empty 
# or conditionally check for the content type before parsing.
