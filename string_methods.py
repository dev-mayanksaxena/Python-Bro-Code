#STRING METHODS
# String methods are functions that can be called on string objects to perform various operations.

# Example of string methods
my_string = "Hello, World!"
print(my_string.lower())
print(my_string.upper())
print(my_string.replace("World", "Python"))
print(my_string.split(", "))  # ['Hello', 'World!'] 
# Example usage:
# 1. lower() - Converts all characters in the string to lowercase. 
# 2. upper() - Converts all characters in the string to uppercase.
# 3. replace(old, new) - Replaces occurrences of 'old' with 'new' in the string.
# 4. split(separator) - Splits the string into a list where each word is a list item, using 'separator' as the delimiter.
# 5. join(iterable) - Joins elements of an iterable (like a list) into a single string, with the string as a separator.
print(my_string.join(["Python", "is", "fun"]))  # PythonHello, World!isfun
print(my_string.split(" "))  # ['Hello,', 'World!']