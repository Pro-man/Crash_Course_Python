# Nathan Reid
# Aug. 30th, 2022
# Write a while loop that allows users to enter an album's artist and title.
# Once you have that information, call make_album() with the user's input and print
    # the dictionary that's created.
# Include a 'quit' value in the while loop.


# function with parameters 
def make_album(artist_name,album_title):
    # docstring
    """Return a dictionary with the artist and ablum information."""
    # make a dictionary
    music = {'artist_name': artist_name.title(), 'album_title': album_title.title()}
    # return the dictionary information to the caller
    return music
    # NOTE - print statement returns NONE
    # print(music)

# while loop that can be continued and exited
while True:
    # Explain what the user is doing.
    print("\nPlease, enter in the album's information below.")
    print("Enter 'q' to exit.")

    name = input("Artist Name: ")
    if name == 'q':
        break

    a_title = input("Album Title: ")
    if a_title == 'q':  
        break

    # Make sure this section is within the while loop
    singing = make_album(name, a_title)
    print(singing)


# Traceback (most recent call last):
#   File "user_albums.py", line 29, in <module>
    # print("Music Information: " + singing)
# TypeError: can only concatenate str (not "dict") to str