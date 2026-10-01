# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}") #converts all char in string to Uppercase equivalent
print(f"Modified String 2: {user_string.upper()}") #converts all char in string to Uppercase equivalent
print(f"Modified String 3: {user_string.strip()}") #removes all spaces from the beginning and end of the string.
print(f"Modified String 4: {user_string.replace('a', '@')}")# replaces all instances of the first given string with the second given string.
print(f"Modified String 5: {user_string.capitalize()}") # capitalizes the first char in the string
print(f"Modified String 6: {user_string[::-1]}") #reverses the string 
print(f"Modified String 7: {user_string.title()}") # capitalizes the first char of each word in the string
print(f"Modified String 8: {len(user_string)}") # returns the length of the string
print(f"Modified String 9: {user_string.find('a')}") # returns the first position of the char given as an argument in the string, -1 if it does not.
print(f"Modified String 10: {user_string.count('a')}") # returns the number of times the char given as an argument appears in the string
print(f"Modified String 11: {user_string.startswith('Hello')}") # returns whether or not the string begins with the string passed as an argument
print(f"Modified String 12: {user_string.endswith('!')}") # returns whether or not the string ends with the string passed as an argument
print(f"Modified String 13: {user_string.isalnum()}") # returns whether or not the string only contains numvers or letters
print(f"Modified String 14: {user_string.isalpha()}") # returns whether or not the string only contains letters
print(f"Modified String 15: {user_string.isdigit()}") # returns whether or not the string is a whole positive number



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!