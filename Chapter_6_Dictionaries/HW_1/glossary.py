# Nathan Reid
# Aug. 22nd, 2022
# Think of five programming words you've learned about in the previous chapters
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You might print
# the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the 
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output. 

glossary = {
    'list': 'a collection of items in a particular order.',
    'integer': 'a whole number without decimals.',
    'float': 'any number with a decimal point.',
    'string': 'string is a collection of alphabets, words or other characters.',
    'boolean': 'true or false expression.',
}

print('List - ' + glossary['list'].title() + '\n')
print('Integer - ' + glossary['integer'].title() + '\n')
print('Float - ' + glossary['float'].title() + '\n')
print('String - ' + glossary['string'].title() + '\n')
print('Boolean - ' + glossary['boolean'].title() + '\n')