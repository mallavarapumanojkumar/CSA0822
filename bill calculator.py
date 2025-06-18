# List of items with name, price, and quantity
items = [
    {"name": "Milk", "price": 25.0, "quantity": 2},
    {"name": "Bread", "price": 30.0, "quantity": 1},
    {"name": "Eggs", "price": 6.0, "quantity": 12},
    {"name": "Rice", "price": 50.0, "quantity": 1}
]

# Calculate total cost
total_cost = 0.0
print("Item-wise Billing:")
for item in items:
    cost = item["price"] * item["quantity"]
    total_cost += cost
    print(f"{item['name']}: {item['quantity']} x {item['price']} = {cost:.2f}")

print("\nTotal Bill Amount: ₹{:.2f}".format(total_cost))
