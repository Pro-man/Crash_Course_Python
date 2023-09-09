# Nathan Reid
# Sept. 9th, 2022
# Python Standard Library


# NOTE - Keep track of the order in which key-value pairs are added,
# use the OrderedDict class from collections module.

# NOTE - Instances of the OrderedDict class behave almost exactly like dictionaries
# except they keep track of the order in which key-value pairs are added.

# import from library
from collections import OrderedDict

# create instance
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + " 's favorite language is " + language.title() + ".")