name = input("Enter your name: ").title()
item_name = input("Enter your item name: ").upper()
item_price = float(input("Enter price of the item: "))
quantity = int(input("Enter quantity: "))

print("--- RECEIPT ---")
print("Customer:", name)
print("Item:", item_price)
print("Price per item: ₱" + item_price)
print("Quantity: ", quantity)
final_bill = item_price * quantity
print("Final Bill: ₱" + final_bill)