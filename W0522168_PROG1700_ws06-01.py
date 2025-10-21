# Name: Malcolm Edwards
# Student Number: W0522168
# Course: PROG1700
# Week: 6 – Tuples CRUD Activity
# (removed Markdown code fence)
# --- Step 2 – Create (C) ---
customer = ("John Doe", "Premium", "Canada")
print("Customer Record:", customer)

# Print each item using indexing
print("Name:", customer[0])
print("Account Type:", customer[1])
print("Country:", customer[2])

# --- Step 3 – Read (R) ---
print("Customer Name:", customer[0])
print("Account Type:", customer[1])

# Challenge: Use a for loop to print each field
print("Customer Details:")
for field in customer:
    print(field)

# --- Step 4 – Update (U) ---
# Customer upgrades account type
customer = ("John Doe", "Platinum", "Canada")
print("Updated Customer Record:", customer)

# --- Step 5 – Delete (D) ---
del customer

# Challenge: Try printing customer after deletion
try:
    print(customer)
except NameError:
    print("Error: 'customer' is not defined (it was deleted).")

# --- Step 6 – Real-World Example ---
flight = ("AC123", "Halifax", "Toronto", "10:30 AM")
print(f"Flight {flight[0]} departs from {flight[1]} to {flight[2]} at {flight[3]}")

# Update flight time by creating a new tuple
flight = ("AC123", "Halifax", "Toronto", "11:15 AM")
print(f"Updated Flight {flight[0]} departs at {flight[3]}")

# Reflection:
# 1. Why can’t tuples be updated directly like lists?
#    Tuples are immutable, meaning their contents cannot be changed after creation.
#    This protects the data from accidental modification.

# 2. What are some advantages of immutability in programming?
#    - Data safety and integrity
#    - Easier debugging and reasoning about code
#    - Can be used as dictionary keys or set elements
#    - Better performance in some cases

# 3. Give one real-world example where tuples make more sense than lists.
#    Storing coordinates (x, y) or (latitude, longitude) — fixed values that should not change.
# (removed Markdown code fence)
