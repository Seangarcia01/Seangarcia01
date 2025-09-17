# Prompt user for the 'name' and format it in title format
name = input("Enter your name: ").title()

# Prompt user for the 'item_name' and format it in UPPERCASE / Upper
item_name = input("Enter your item name: ").upper()

# Prompt user for the 'item_price' (float)
item_price = float(input("Enter price of the item: "))

# Prompt user for the 'quantity' (int)
quantity = int(input("Enter quantity: "))


# Calculate the Final Bill
final_bill = item_price * quantity


# Print the receipt in a clean and formatted way
print("\n--- RECEIPT ---")
print(f"Customer: {name}") 
print(f"Item: {item_name}") 
print(f"Price per item: ₱{item_price:,.2f}") # Display price with proper currency formatting
print(f"Quantity: {quantity}") 
print(f"Final Bill: ₱{final_bill:,.2f}") # Display final bill with currency formatting