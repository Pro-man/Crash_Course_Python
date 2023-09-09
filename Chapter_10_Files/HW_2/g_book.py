# Nathan Reid
# Sept. 11th, 2022
# Write a while loop that prompts users for their name.
# When they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.


# file inside of a variable
book = 'guest.txt'

# flag
active = True

with open(book,'a') as file_object:
    while active:
        # prompt the user
        name = input("What is your name? ")
        file_object.write(name + "\n")

        if name == 'end':
            active = False
        else:
            print("Hello, I hope you are having a good day!")
   

        

        
