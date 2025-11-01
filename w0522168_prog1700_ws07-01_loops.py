# ---------------------------
ticket = ("Halifax", "Toronto", "AC702", 349.99)
print("Flight:", ticket)
print(f"From {ticket[0]} to {ticket[1]} on flight {ticket[2]} costing ${ticket[3]}")

origin, destination, flight_num, price = ticket
print(f"✈️  Your flight {flight_num} takes you from {origin} to {destination} for ${price}! 🧳🌎")
# ---------------------------
flights = [
    ("Halifax", "Montreal", 189.99),
    ("Montreal", "Ottawa", 99.99),
    ("Ottawa", "Toronto", 159.99)
]

print("\nAll Flights:")
for origin, destination, price in flights:
    print(f"{origin} → {destination}: ${price}")

print("\nFlights under $150:")
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
# ---------------------------
flight = ("Halifax", "Toronto", 349.99)
print("\nBefore:", flight)

flight = (flight[0], "Vancouver", flight[2] + 150)
print("After:", flight)

def update_flight(f, new_dest, new_price):
    """Return a new tuple with updated destination and price."""
    return (f[0], new_dest, new_price)

print("\nUpdated Flight Records:")
flights_updated = []
for f in flights:
    new_dest = f[1] + " Intl"
    new_price = f[2] + 25
    flights_updated.append(update_flight(f, new_dest, new_price))

for f in flights_updated:
    print(f)
# ---------------------------
orders = [
    ("Alex", "Large", ["Pepperoni", "Mushroom"]),
    ("Priya", "Medium", ["Cheese"]),
    ("Jordan", "Small", ["Veggie", "Onion"]),
    ("Taylor", "Large", ["Cheese", "Bacon"]),
    ("Sam", "Large", ["Pepperoni"])
]

print("\nPizza Orders:")
for name, size, toppings in orders:
    topping_list = " & ".join(toppings)
    print(f"{name} ordered a {size} pizza with {topping_list}.")

large_count = sum(1 for name, size, toppings in orders if size == "Large")
print(f"\nNumber of Large pizzas ordered: {large_count}")

unique_toppings = set()
for _, _, toppings in orders:
    unique_toppings.update(toppings)
print(f"Unique toppings ordered: {', '.join(sorted(unique_toppings))}")