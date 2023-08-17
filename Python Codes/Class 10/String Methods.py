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

'''

This code manipulates a given string named "text" using various string methods and operations. It performs the following actions:

Converts the entire string to uppercase using upper() and prints the result.
Capitalizes the first character of the string using capitalize() and prints the result.
Converts the starting character of each word to capital using title() and prints the result.
Converts the entire string to lowercase using lower() and prints the result.
Joins each character of the string with a hyphen using join() and prints the result.
Checks if all characters in the string are uppercase using isupper() and prints the result.
Checks if all characters in the string are lowercase using islower() and prints the result.
Checks if the string is title-cased using istitle() and prints the result.
Checks if all characters in the string are whitespace characters using isspace() and prints the result.
Calculates and prints the length of the string using len().
Reverses the string using slicing ([::-1]) and prints the result.
It uses string slicing to extract a substring from index 3 to 11 (exclusive) and prints the result.
Splits the string into a list of substrings using whitespace as the separator using split() and prints the result.

'''
