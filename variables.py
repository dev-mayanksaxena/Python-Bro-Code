#STRING VARIABLES# This is a string variable
# A string is a sequence of characters enclosed in quotes

name = "Mayank Saxena"
print(name)
print(name + "is 21 years old.") #concatenation
print(type(name)) #method to check type

#This is a comment
f_name = "Mayank"
l_name = "Saxena"
print(f_name + " " + l_name)
print(f"{f_name} {l_name} is 21 years old.") #formatted string
email = "dev.mayanksaxena@gmail.com"
print(email)

#INTEGER VARIABLES# This is an integer variable
age = 21
print(age)
print(f"{name} is {age} years old.") #formatted string with integer

quantity = 5
print(f"{name} has {quantity} apples.") #formatted string with integer

number_of_students = 30
print(f"There are {number_of_students} students in the class.") #formatted string with integer  

#FLOAT VARIABLES# This is a float variable
height = 1.74
print(height)
print(f"{name} is {height} meters tall.") #formatted string with float

price = 19.99
print(f"The price of the book is ${price}.") #formatted string with float

distance = 10.5
print(f"The distance to the destination is {distance} kilometers.") #formatted string with float

#BOOLEAN VARIABLES# This is a boolean variable
is_student = True
print(is_student)
print(f"{name} is a student: {is_student}.") #formatted string with boolean
#Boolean values can be True or False, Mostly used for conditions internally.

for_sale = False
if for_sale:
    print(f"Is the item for sale? {for_sale}.") #formatted string with boolean

else:
    print(f"The item is not for sale: {for_sale}.") #formatted string with boolean
    
is_online = True
if is_online:
    print(f"{name} is online") #formatted string with boolean
else:
    print(f"{name} is offline") #formatted string with boolean
    
# The four basic variable types in Python are strings, integers, floats, and booleans.
