# Nathan Reid
# Aug. 30th, 2022
# Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and it should return a dictionary
    # containing these two pieces of information. 
# Use the function to make three dictionaries representing diffent albums.
# Print each return value to show that the dictionaries are storing the album information correctly.
# Add an optional parameter to make_album() that allows you to store the number of tracks on an album.

# function with parameters add optional default value
def make_album(artist_name,album_title, make_album=''):
    # docstring
    """Return a dictionary with the artist and ablum information."""
    music = {'artist_name': artist_name.title(), 'album_title': album_title.title()}
    # add conditional test for optional default value
    if make_album:
        # create key and value
        music['make_album'] = make_album
    return music

# call funtion with in a variable
R_n_b = make_album('michael jackson', 'thriller')
print(R_n_b)
R_n_b = make_album('jodeci', 'forever my lady')
print(R_n_b)
R_n_b = make_album('whitney houston', 'sing town')
print(R_n_b)
# default value - optional argument
R_n_b = make_album('dre hill', 'enter the dragon', 10)
print(R_n_b)

