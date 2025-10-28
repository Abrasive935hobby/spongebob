# ================================================

temperatures = [14, 16, 18, 17, 20, 19, 15]

total = 0
for temp in temperatures:
    total += temp
avg = total / len(temperatures)
print("Average temperature:", avg)

while True:
    new_temp = input("Enter a new temperature (or 'done' to stop): ")
    if new_temp.lower() == "done":
        break
    if new_temp.isdigit() or (new_temp.startswith('-') and new_temp[1:].isdigit()):
        temperatures.append(int(new_temp))
    else:
        print("Invalid input, please enter a number.")

highest = max(temperatures)
lowest = min(temperatures)
above_18 = sum(1 for t in temperatures if t > 18)

unique_temps = set(temperatures)

print(f"\nHighest temperature: {highest}°C")
print(f"Lowest temperature: {lowest}°C")
print(f"Days above 18°C: {above_18}")
print(f"Unique temperature readings: {unique_temps}\n")

# ================================================

books = {
    "Python Basics": 3,
    "Web Design 101": 2,
    "Networking Made Easy": 1
}

while True:
    for title, qty in books.items():
        print(f"{title:25} copies: {qty}")

    action = input("\nEnter 'checkout', 'return', or 'done': ").lower()
    if action == "done":
        break
    book_name = input("Enter book title: ")

    if book_name not in books:
        print("Book not found.")
        continue

    if action == "checkout":
        if books[book_name] > 0:
            books[book_name] -= 1
        else:
            print("⚠️ No more copies available!")
    elif action == "return":
        books[book_name] += 1
    else:
        print("Invalid action.")

fewest = min(books, key=books.get)
total_books = sum(books.values())

print(f"\nBook with fewest copies: {fewest}")
print(f"Total books in circulation: {total_books}\n")

# ================================================

items = ["Latte", "Espresso", "Tea", "Muffin"]
sales = [12, 8, 10, 6]

print("Item".ljust(15), "Sales")
print("-" * 25)
for i in range(len(items)):
    print(f"{items[i]:15} {sales[i]}")

total_sales = sum(sales)
average_sales = total_sales / len(sales)
print(f"\nTotal sales: {total_sales}")
print(f"Average per item: {average_sales:.2f}")

while True:
    new_item = input("\nAdd a new item (or 'done'): ")
    if new_item.lower() == "done":
        break
    try:
        sold = int(input(f"How many {new_item}s sold? "))
        items.append(new_item)
        sales.append(sold)
    except ValueError:
        print("Please enter a valid number.")

unique_items = set(items)
best_seller = items[sales.index(max(sales))]

print(f"\nUnique menu items: {unique_items}")
print(f"Best-selling item: {best_seller}\n")

# ================================================

adoptions = {
    "Cats": 4,
    "Dogs": 6,
    "Rabbits": 2
}

species_seen = set(adoptions.keys())

while True:
    new_pet = input("Enter pet species (or 'done'): ").title()
    if new_pet.lower() == "done":
        break
    try:
        count = int(input(f"How many {new_pet} adopted? "))
        if count < 0:
            print("⚠️ Invalid number.")
            continue
        adoptions[new_pet] = adoptions.get(new_pet, 0) + count
        species_seen.add(new_pet)
    except ValueError:
        print("Please enter a number.")

total_adoptions = sum(adoptions.values())
most_popular = max(adoptions, key=adoptions.get)

print("\nAdoption Summary:")
for species, count in adoptions.items():
    print(f"{species:10} adopted: {count}")

print(f"\nTotal adoptions: {total_adoptions}")
print(f"Most popular pet: {most_popular}")
print(f"Unique species: {species_seen}\n")

# ================================================

# 1. Which dataset (weather, library, café, or pets) was easiest to work with, and why?
#    → The café sales were easiest since it used simple lists and basic arithmetic.
#
# 2. How do loops make repetitive tasks faster in programming?
#    → Loops repeat actions automatically, saving time and reducing errors from manual repetition.
#
# 3. Which collection type (list, set, or dict) felt most useful today?
#    → Dictionaries, because they link data labels to values clearly (like book titles to copies).
#
# 4. Describe one improvement you would make if this lab continued next week.
#    → Add file saving/loading to keep data between runs.
