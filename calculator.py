#Calculator Program

def add(x, y):
    return round(x + y, 3)
def subtract(x, y):
    return round(x - y, 3)
def multiply(x, y):
    return round(x * y, 3)  
def divide(x, y):
    if y != 0:
        return round(x / y, 3)
    else:
        return "Division by zero error"
def power(x, y):
    return round(x ** y, 3) 
def modulus(x, y):
    return round(x % y, 3)
def floor_division(x, y):
    return round(x // y, 3) 
def square_root(x):
    return round(x ** 0.5, 3)
def absolute_value(x):
    return round(abs(x), 3) 
def cube(x):
    return round(x ** 3, 3)
def square(x):
    return round(x ** 2, 3) 
def cube_root(x):
    return round(x ** (1/3), 3)
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Division")
    print("8. Square Root")
    print("9. Absolute Value")
    print("10. Cube")
    print("11. Square")
    print("12. Cube Root")
    print("13. Factorial")

    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12/13): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
        elif choice == "5":
            print(f"{num1} ** {num2} = {power(num1, num2)}")
        elif choice == "6":
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
        elif choice == "7":
            print(f"{num1} // {num2} = {floor_division(num1, num2)}")
        elif choice == "8":
            print(f"√{num1} = {square_root(num1)}")
        elif choice == "9":
            print(f"|{num1}| = {absolute_value(num1)}")
        elif choice == "10":
            print(f"{num1}^3 = {cube(num1)}")
        elif choice == "11":
            print(f"{num1}^2 = {square(num1)}")
        elif choice == "12":
            print(f"∛{num1} = {cube_root(num1)}")
        elif choice == "13":
            print(f"Factorial of {int(num1)} = {factorial(int(num1))}")
    else:
        print("Invalid Input")
        
calculator()