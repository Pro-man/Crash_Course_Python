# Nathan Reid
# Aug. 25th, 2022
# A dictionary in a dictionary

# NOTE - You should not nest lists and dictionaries too deeply

# dictionary 
# tww dictionaries in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }

}
# dictionary name {
    # nested dictionary name : {
    # nested dictionary key : value}
# }

# loop through dictionary
for username, user_info in users.items():
    # print nested dictionary name
    print("\nUsername: " + username)
    # print value of nested dictionaries and put in variables
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    # print variables
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


# print(users) - prints both dictionaries

# print(users[username]) - this prints information inside the dictionary

# TypeError: unhashable type: 'dict' - print(users[user_info])