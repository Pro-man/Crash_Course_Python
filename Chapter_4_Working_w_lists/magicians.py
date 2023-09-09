# Nathan Reid
# Aug. 15th, 2022
# Loops



# list
magicians = ['alice', 'david', 'carolina']
# for loop - pull a name from the list and store in the variable magician
for magician in magicians:
    # display only one name at a time
    print(magician.title())


# NOTE - Do no use the list name. sort() in the print function it will return none
# change the order of the list - permanently
magicians.sort()
print(magicians)

# NOTE - Do no use the list name. sort(reverse=True) in the print function it will return none
# change the order of the list back - permanently
magicians.sort(reverse=True)
print(magicians)

# change list back permanently
magicians.reverse()
print(magicians)

# create list
artists = ['alice', 'david', 'carolina']
# loop through list
for artist in artists:
    # everything inside a for loop get ran once for every item in the list
    print(artist.upper() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + artist.title() + ".\n")
    
# any line out side the for loop gets ran once
print("Thank you, everyone. That was a great magic show!")
