#input() function is used to take input from the user
# The input is always taken as a string, so type casting may be required for other datatypes.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
is_student = bool(input("Are you a student? (True/False): "))

print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")