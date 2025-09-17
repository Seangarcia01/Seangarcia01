#  Basketball Game Ticket Discount 

# (CONSTANT) Ticket price and discount
TICKET_PRICE = 120
DISCOUNT = 5

# Prompts the user for number of tickets to watch the basketball game
num_tickets = int(input("Enter the number of tickets: "))

# Calculate total cost using boolean math for discount
total_cost = num_tickets * (TICKET_PRICE - DISCOUNT * (num_tickets >= 10))
# 10 - 5 * (10 >= 10 = True = 1)
discounted_price = TICKET_PRICE - DISCOUNT * (num_tickets >= 10)

# Display the result
print("\n--- Ticket Summary ---")
print("Tickets Bought:", num_tickets)
print(f"Price per ticket: ₱{discounted_price:,}")
print(f"Total cost: ₱{total_cost:,}")



