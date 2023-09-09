# Nathan Reid
# Aug. 14th, 2022
# Store at least five places in a list
# Print the orginal order
# Use sorted() to print your list in alphabetical order
# Show the your list is still in the original order - print it
# Use reverse() to change the order of your list - print it
# Use reverse to change the order of your list again - print it
# Use sort() to change your list so it's stored alphabetical order - print it
# Use sort() to change your list so it's stored in reverse alphabetical order - print it

# create list
places = ['virginia', 'new york', 'oakland', 'canada', 'thailand']
print(places)

# sorted
print("Sorted list")
print(sorted(places))

# original list order
print("Original list")
print(places)

# reverse list
print("Reverse list")
places.reverse()
print(places)

# reverse list again
print("Reverse list again")
places.reverse()
print(places)

# sort list
print("Sort list")
places.sort()
print(places)

# sort list again
print("Sort list again")
places.sort(reverse=True)
print(places)