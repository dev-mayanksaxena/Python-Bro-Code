#If statements = Do something if a condition is true, else do something else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You are not eligible to vote.")


response = input("Do you want some food? (yes/no): ").strip().lower()
if response == "yes":
    print("Here's some food for you!")
else:
    print("Okay, maybe next time.")
    
name = input("Enter your name: ")
if name:
    print(f"Hello, {name}!")
else:
    print("Type in your name!")