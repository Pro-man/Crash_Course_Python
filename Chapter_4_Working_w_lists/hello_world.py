# Nathan Reid
# Aug. 15, 2022

# You can avoid unexpected indentation errors 
# by indenting only when you have a specific reason to do so. 
# The only line you should indent are the actions you want to repeat 
# for each iotem in a for loop


artists = ['alice', 'david', 'carolina']
# loop through list
# NOTE - if you for get the colon you will get a syntax error: invalid syntax
for artist in artists:
    # everything inside a for loop get ran once for every item in the list
    print(artist.upper() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + artist.title() + ".\n")

    # indent unnecessarily after the loop
    print("Thank you, everyone. That was a great magic show!")
