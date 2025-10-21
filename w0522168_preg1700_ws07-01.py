# ===========================
ticket = ("Halifax", "Toronto", "AC702", 349.99)
print("Flight:", ticket)
print(f"From {ticket[0]} to {ticket[1]} on flight {ticket[2]} costing ${ticket[3]}")

# 💡 Challenge: Unpack tuple + add emoji flair
origin, destination, flight_no, price = ticket
print(f"✈️  Your flight {flight_no} goes from {origin} to {destination} and costs ${price}! 🧳🌎")

# ===========================
flights = [
    ("Halifax", "Montreal", 189.99),
    ("Montreal", "Ottawa", 99.99),
    ("Ottawa", "Toronto", 159.99)
]

print("\nAll Flights:")
for origin, destination, price in flights:
    print(f"{origin} → {destination}: ${price}")

print("\nFlights cheaper than $150:")
for origin, destination, price in flights:
    if price < 150:
        print(f"{origin} → {destination}: ${price}")

i = 0
total = 0
while i < len(flights):
    total += flights[i][2]
    i += 1

average_price = total / len(flights)
print(f"\nTotal cost of all flights: ${total:.2f}")
print(f"Average ticket cost: ${average_price:.2f}")

# ===========================
flight = ("Halifax", "Toronto", 349.99)
print("\nBefore:", flight)

flight = (flight[0], "Vancouver", flight[2] + 150)
print("After:", flight)

def update_flight(f, new_dest, new_price):
    """Return a new tuple with updated destination and price."""
    return (f[0], new_dest, new_price)

updated = update_flight(("Ottawa", "Toronto", 159.99), "Calgary", 299.99)
print("Updated flight:", updated)

"""
flights_data = [
    ("Halifax", "Toronto", 349.99),
    ("Montreal", "Ottawa", 99.99)
]

for i in range(len(flights_data)):
    print(f"Current flight: {flights_data[i]}")
    new_dest = input("Enter new destination: ")
    new_price = float(input("Enter new price: "))
    flights_data[i] = update_flight(flights_data[i], new_dest, new_price)

print("Updated flights:", flights_data)
"""
# ===========================
orders = [
    ("Alex", "Large", ["Pepperoni", "Mushroom"]),
    ("Priya", "Medium", ["Cheese"]),
    ("Jordan", "Small", ["Veggie", "Onion"]),
    ("Taylor", "Large", ["Pepperoni", "Cheese"]),
]
print("\nPizza Orders Summary:")
for name, size, toppings in orders:
    topping_list = " & ".join(toppings)
    print(f"{name} ordered a {size} pizza with {topping_list}.")

large_count = sum(1 for _, size, _ in orders if size == "Large")
print(f"\nNumber of Large pizzas ordered: {large_count}")

unique_toppings = set()
for _, _, toppings in orders:
    unique_toppings.update(toppings)
print(f"Unique toppings ordered: {unique_toppings}")

# ===========================
# ===========================
# Step 1 – Tuple Basics: Airline Ticket
# ===========================

ticket = ("Halifax", "Toronto", "AC702", 349.99)
print("Flight:", ticket)
print(f"From {ticket[0]} to {ticket[1]} on flight {ticket[2]} costing ${ticket[3]}")

# 💡 Challenge: Unpack tuple + add emoji flair
origin, destination, flight_no, price = ticket
print(f"✈️  Your flight {flight_no} goes from {origin} to {destination} and costs ${price}! 🧳🌎")


# ===========================
# Step 2 – Tuple Collections: Travel Itinerary
# ===========================

flights = [
    ("Halifax", "Montreal", 189.99),
    ("Montreal", "Ottawa", 99.99),
    ("Ottawa", "Toronto", 159.99)
]

print("\nAll Flights:")
for origin, destination, price in flights:
    print(f"{origin} → {destination}: ${price}")

# 💡 Challenge 1: Print only flights cheaper than $150
print("\nFlights cheaper than $150:")
for origin, destination, price in flights:
    if price < 150:
        print(f"{origin} → {destination}: ${price}")

# 💡 Challenge 2: Use while loop to total up prices and find average
i = 0
total = 0
while i < len(flights):
    total += flights[i][2]
    i += 1

average_price = total / len(flights)
print(f"\nTotal cost of all flights: ${total:.2f}")
print(f"Average ticket cost: ${average_price:.2f}")


# ===========================
# Step 3 – Simulating Updates (Immutability in Action)
# ===========================

flight = ("Halifax", "Toronto", 349.99)
print("\nBefore:", flight)

# “Update” destination
flight = (flight[0], "Vancouver", flight[2] + 150)
print("After:", flight)

# 💡 Challenge: Write function to update flight
def update_flight(f, new_dest, new_price):
    """Return a new tuple with updated destination and price."""
    return (f[0], new_dest, new_price)

# Example usage
updated = update_flight(("Ottawa", "Toronto", 159.99), "Calgary", 299.99)
print("Updated flight:", updated)

# 💡 Bonus: interactive updates
# (You can uncomment this section if running interactively)
"""
flights_data = [
    ("Halifax", "Toronto", 349.99),
    ("Montreal", "Ottawa", 99.99)
]

for i in range(len(flights_data)):
    print(f"Current flight: {flights_data[i]}")
    new_dest = input("Enter new destination: ")
    new_price = float(input("Enter new price: "))
    flights_data[i] = update_flight(flights_data[i], new_dest, new_price)

print("Updated flights:", flights_data)
"""


# ===========================
# Step 4 – Real-World Mini Challenge: Pizza Orders
# ===========================

orders = [
    ("Alex", "Large", ["Pepperoni", "Mushroom"]),
    ("Priya", "Medium", ["Cheese"]),
    ("Jordan", "Small", ["Veggie", "Onion"]),
    ("Taylor", "Large", ["Pepperoni", "Cheese"]),
]

# 💡 Task 1: Print summaries
print("\nPizza Orders Summary:")
for name, size, toppings in orders:
    topping_list = " & ".join(toppings)
    print(f"{name} ordered a {size} pizza with {topping_list}.")

# 💡 Task 2: Count Large pizzas
large_count = sum(1 for _, size, _ in orders if size == "Large")
print(f"\nNumber of Large pizzas ordered: {large_count}")

# 💡 Task 3: Unique toppings
unique_toppings = set()
for _, _, toppings in orders:
    unique_toppings.update(toppings)
print(f"Unique toppings ordered: {unique_toppings}")


# ============================# ===========================
# Step 1 – Tuple Basics: Airline Ticket
# ===========================

ticket = ("Halifax", "Toronto", "AC702", 349.99)
print("Flight:", ticket)
print(f"From {ticket[0]} to {ticket[1]} on flight {ticket[2]} costing ${ticket[3]}")

# 💡 Challenge: Unpack tuple + add emoji flair
origin, destination, flight_no, price = ticket
print(f"✈️  Your flight {flight_no} goes from {origin} to {destination} and costs ${price}! 🧳🌎")


# ===========================
# Step 2 – Tuple Collections: Travel Itinerary
# ===========================

flights = [
    ("Halifax", "Montreal", 189.99),
    ("Montreal", "Ottawa", 99.99),
    ("Ottawa", "Toronto", 159.99)
]

print("\nAll Flights:")
for origin, destination, price in flights:
    print(f"{origin} → {destination}: ${price}")

# 💡 Challenge 1: Print only flights cheaper than $150
print("\nFlights cheaper than $150:")
for origin, destination, price in flights:
    if price < 150:
        print(f"{origin} → {destination}: ${price}")

# 💡 Challenge 2: Use while loop to total up prices and find average
i = 0
total = 0
while i < len(flights):
    total += flights[i][2]
    i += 1

average_price = total / len(flights)
print(f"\nTotal cost of all flights: ${total:.2f}")
print(f"Average ticket cost: ${average_price:.2f}")


# ===========================
# Step 3 – Simulating Updates (Immutability in Action)
# ===========================

flight = ("Halifax", "Toronto", 349.99)
print("\nBefore:", flight)

# “Update” destination
flight = (flight[0], "Vancouver", flight[2] + 150)
print("After:", flight)

# 💡 Challenge: Write function to update flight
def update_flight(f, new_dest, new_price):
    """Return a new tuple with updated destination and price."""
    return (f[0], new_dest, new_price)

# Example usage
updated = update_flight(("Ottawa", "Toronto", 159.99), "Calgary", 299.99)
print("Updated flight:", updated)

# 💡 Bonus: interactive updates
# (You can uncomment this section if running interactively)
"""
flights_data = [
    ("Halifax", "Toronto", 349.99),
    ("Montreal", "Ottawa", 99.99)
]

for i in range(len(flights_data)):
    print(f"Current flight: {flights_data[i]}")
    new_dest = input("Enter new destination: ")
    new_price = float(input("Enter new price: "))
    flights_data[i] = update_flight(flights_data[i], new_dest, new_price)

print("Updated flights:", flights_data)
"""


# ===========================
# Step 4 – Real-World Mini Challenge: Pizza Orders
# ===========================

orders = [
    ("Alex", "Large", ["Pepperoni", "Mushroom"]),
    ("Priya", "Medium", ["Cheese"]),
    ("Jordan", "Small", ["Veggie", "Onion"]),
    ("Taylor", "Large", ["Pepperoni", "Cheese"]),
]

# 💡 Task 1: Print summaries
print("\nPizza Orders Summary:")
for name, size, toppings in orders:
    topping_list = " & ".join(toppings)
    print(f"{name} ordered a {size} pizza with {topping_list}.")

# 💡 Task 2: Count Large pizzas
large_count = sum(1 for _, size, _ in orders if size == "Large")
print(f"\nNumber of Large pizzas ordered: {large_count}")

# 💡 Task 3: Unique toppings
unique_toppings = set()
for _, _, toppings in orders:
    unique_toppings.update(toppings)
print(f"Unique toppings ordered: {unique_toppings}")


# ===========================
# Reflection:
# 1. Tuples keep data safe from accidental changes, making them great for fixed records.
# 2. In Step 3, I learned to create a new tuple instead of editing one — that’s immutability in action.
# 3. I liked the pizza orders step; it was fun and practical.
# 4. Tuples fit well for GPS coordinates since those values don’t change.
