# Nathan Reid
# Aug. 12, 2022
# Store a person's name, and include some whitespace characters at the beginning and end of name. 
# Make sure you use each character combination, "\t" and "\n"
# Print the name once, so the whitespace around the name is dispalyed.
# Use the three stripping functions, lstrip(), rstrip(), and strip().

name = " james baldwin "
print(name.title())
print("\t" + name + "\t\n" + name.upper())
print(name.lstrip() + " - left strip")
print(name.rstrip() + " - right strip")
print(name.strip() + " - strip")