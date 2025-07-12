# TEMPERATURE CONVERTER
# This script converts temperatures between Celsius, Fahrenheit, and Kelvin.

unit = input("Enter the unit of temperature you want to convert from: (C/F/K): ").strip().upper()
if unit not in ['C', 'F', 'K']:
    print("Invalid unit. Please enter C, F, or K.")
elif unit == "C":
    temp = float(input("Enter temperature in Celsius: "))
    converted_temp_f = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted_temp_f:.2f}°F.")
    converted_temp_k = temp + 273.15
    print(f"{temp}°C is equal to {converted_temp_k:.2f} K.")
elif unit == "F":  
    temp = float(input("Enter temperature in Fahrenheit: "))
    converted_temp_c = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {converted_temp_c:.2f}°C.")
    converted_temp_k = (temp - 32) * 5/9 + 273.15
    print(f"{temp}°F is equal to {converted_temp_k:.2f} K.")
else:
    temp = float(input("Enter temperature in Kelvin: "))
    converted_temp_c = temp - 273.15
    print(f"{temp} K is equal to {converted_temp_c:.2f}°C.")
    converted_temp_f = (temp - 273.15) * 9/5 + 32
    print(f"{temp} K is equal to {converted_temp_f:.2f}°F.")
