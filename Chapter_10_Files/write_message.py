# Nathan Reid
# Sept. 11th, 2022
# Writing to a File

# NOTE - To write text to a file, you need to call open() with a second argument
# telling Python that you want to write to the file. 

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# NOTE - 'w' tells Python that we want to open the file in write mode. 
# read mode ('r')
# write mode ('w') - writes over exiting content
# append mode ('a') - add to content at the end of the file
# read and write a file ('r+')

# If you omit the mode argument Python opens the file in read-only by default.

# NOTE - Be careful opening a file in write mode ('w') because if the file does exist,
# Python will erase the file before returning the file object. 

# NOTE - Python can only write strings to a text file. If you want to store numerical data in a 
# text file, you'll have to convert the data to string format first using the str() function.

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
