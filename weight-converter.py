# Weight Converter
# This script converts weight from pounds to kilograms and vice versa.

weight = float(input("Enter weight: "))
unit = input("Enter unit (pounds/kg): ").strip().lower()
if unit == "pounds":
    converted_weight = weight * 0.453592
    print(f"{weight} pounds is equal to {converted_weight:.2f} kilograms.")
elif unit == "kg":
    converted_weight = weight / 0.453592
    print(f"{weight} kilograms is equal to {converted_weight:.2f} pounds.")
else:
    print("Invalid unit. Please enter 'pounds' or 'kg'.")