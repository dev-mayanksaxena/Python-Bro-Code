# VALIDATE USER INPUT
# Username < 12 characters
# Username must not contain spaces
# Username must not contain digits


username = input("Enter your username: ")
valid = True

if username == "":
    print("Username cannot be empty.")
    valid = False
elif len(username) >= 12:
    print("Username must be less than 12 characters.")
    valid = False
elif " " in username:
    print("Username must not contain spaces.")
    valid = False
elif any(char.isdigit() for char in username):
    print("Username must not contain digits.")
    valid = False

if valid:
    print("Username is valid.")