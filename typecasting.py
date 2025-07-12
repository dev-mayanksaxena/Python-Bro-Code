#TYPE CASTING = Process of converting one data type to another
# In Python, type casting can be done using built-in functions like int(), float(), str(), and bool().

name = "Mayank Saxena"
age = 21
height = 1.74
is_student = True

print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
print(type(height))  # Output: <class 'float'>
print(type(is_student))  # Output: <class 'bool'>  

age = str(age)  # Convert integer to string
print(type(age))  # Output: <class 'str'>

height = int(height)  # Convert float to integer #Truncates the decimal part  #Truncate means to remove the decimal part without rounding
print(type(height))  # Output: <class 'int'>

#name = int(name)  # This will raise an error because name is a string and cannot be converted to an integer
# Uncommenting the line above will result in a ValueError: invalid literal for int() with base 10: 'Mayank Saxena'

is_student = int(is_student)  # This is valid; True becomes 1 and False becomes 0
print(type(is_student))  # Output: <class 'int'>, since True becomes 1 and False becomes 0, which may not be obvious in all contexts

