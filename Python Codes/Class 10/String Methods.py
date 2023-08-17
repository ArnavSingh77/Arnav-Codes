# Declaration of string
text = "arNav is a GOod boY"

# Converts all lowercase characters in a string into uppercase
print("UPPER:", text.upper())

# Converts the first character of the string to a capital (uppercase) letter
print("CAPITALIZE:", text.capitalize())

# Convert starting letter of each word to capital
print("TITLE:", text.title())

# Converts all uppercase characters in a string into lowercase
print("LOWER:", text.lower())

# Returns a concatenated String
print("JOIN:", '-'.join(text))

# Checks if all characters in the string are uppercase
print("IS UPPER:",text.isupper())

# Checks if all characters in the string are lowercase
print("IS LOWER:",text.islower())

# Returns “True” if the string is a title cased string
print("IS TITLE:",text.istitle())

# Returns “True” if all characters in the string are whitespace characters
print("IS SPACE:",text.isspace())

# It returns an integer which is the length of the string. 
print("COUNT/LEN:", len(text))

# Program to reverse a string
print("REVERSE:",text[::-1])

# Python Program to demonstrate String slicing
print("SLICING:",text[3:12])

# Splitting the string
print("SPLIT:", text.split())
