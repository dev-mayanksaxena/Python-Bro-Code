#EXERCISE 2
# Shopping Cart Program

item = input("Enter the item name: ")  # Input item name
quantity = int(input("Enter the quantity: "))  # Input quantity
price = float(input("Enter the price: "))  # Input price
total = quantity * price  # Calculate total

print(f"You have bought {quantity} {item}(s) at ${price:.2f} each. Total cost: ${total:.2f}")  # Output the total cost
