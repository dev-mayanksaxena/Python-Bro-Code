import math

# ARITHMETIC OPERATIONS + MATH FUNCTIONS + Exercises
friends = 10

#Addition
#friends = friends + 1
#friends += 1 #Augmented assignment operator

#Subtraction
#friends -= 1 

#Multiplication
#friends *= 2

#Division
#friends /= 2  

#Exponentiation
#friends **= 2

#Floor Division
#friends //= 2

#Modulus
#friends %= 2

print(friends)


x = 10
y = -3
z = 2.4

#result = round(x) #round to nearest integer
#result = abs(y) #absolute value
#result = pow(x, z) #x raised to the power of z
#result = max(x, y, z) #maximum value
#result = min(x, y, z) #minimum value
#result = divmod(x, 3) #returns quotient and remainder as a tuple

print(math.pi)
print(math.e)
#result = math.sqrt(16) #square root
result = math.ceil(2.4) #round up to nearest integer
result = math.floor(2.4) #round down to nearest integer


#Exercises
#Calculate circumference of a circle
radius = float(input("Enter the radius of the circle: "))
circumference = 2*math.pi*radius
print(f"Circumference of the circle: {round(circumference, 2)}cm")

#Calculate area of a circle
area = math.pi*pow(radius, 2)
print(f"Area of the circle: {round(area, 2)}cm²")