string = "Hello World!"


# Removes the Last Character
print(string[:-1])

# Removes the First Character
print(string[1:])

#
print(string[6:9])

#
print(string[:1], string[:3])

"""STEPPING"""

# Default Step is 1
print(string[::3])

# Prints the string in reverse
print(string[::-1])

string1 = string[::-1]

print(string1)


string.title()