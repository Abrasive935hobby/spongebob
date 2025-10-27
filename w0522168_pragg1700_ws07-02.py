# ============================================================
groceries = {
    "Apples": 3.50,
    "Bananas": 2.75,
    "Bread": 2.99,
    "Milk": 4.29,
    "Eggs": 3.49
}
# Allow user to add new items
while True:
    item = input("Enter an item name (or 'done' to finish): ").title()
    if item.lower() == "done":
        break
    try:
        price = float(input(f"Enter price for {item}: $"))
        groceries[item] = price
    except ValueError:
        print("Invalid price, try again.")

# Apply 10% discount to items > $4.00 and calculate totals
total = 0
most_expensive_item = ""
highest_price = 0

print("\n--- Grocery List ---")
for item, price in groceries.items():
    if price > 4.00:
        price *= 0.9  # 10% discount
        print(f"{item:10} ${price:5.2f}  (10% off!)")
    else:
        print(f"{item:10} ${price:5.2f}")
    total += price
    if price > highest_price:
        highest_price = price
        most_expensive_item = item

print(f"\nTotal cost: ${total:.2f}")
print(f"Most expensive item: {most_expensive_item} (${highest_price:.2f})")
print(f"Total number of items: {len(groceries)}")

# ============================================================

students = ["Ava", "Noah", "Liam"]
grades = [88, 92, 79]

# Add students interactively
while True:
    name = input("\nEnter student name (or 'done' to finish): ").title()
    if name.lower() == "done":
        break
    try:
        grade = int(input(f"Enter grade for {name}: "))
        students.append(name)
        grades.append(grade)
    except ValueError:
        print("Invalid grade, try again.")

print("\n--- Student Grades ---")
for i in range(len(students)):
    print(f"{students[i]:10} → {grades[i]}")

average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)
honour_roll = {students[i] for i in range(len(students)) if grades[i] >= 90}

print(f"\nAverage grade: {average:.2f}")
print(f"Highest grade: {highest}")
print(f"Lowest grade: {lowest}")
print(f"Honour Roll Students: {', '.join(honour_roll) if honour_roll else 'None'}")

# ============================================================

scores = {"Alex": 12, "Priya": 18, "Jordan": 9}

# Allow score updates
while True:
    player = input("\nEnter player name (or 'done' to finish): ").title()
    if player.lower() == "done":
        break
    try:
        points = int(input(f"Enter {player}'s new score: "))
        scores[player] = points
    except ValueError:
        print("Invalid number, try again.")

print("\n--- Game Scores ---")
for name, points in scores.items():
    print(f"{name:10} {points} pts")
    if points > 20:
        print("   🎉 Level Up!")

# Find top player
top_player = max(scores, key=scores.get)
print(f"\nTop Player: {top_player} ({scores[top_player]} pts)")

# ============================================================

songs = ["Song A", "Song B", "Song C"]
plays = [5, 10, 7]

# Add new songs interactively
while True:
    song = input("\nEnter song title (or 'done' to finish): ").title()
    if song.lower() == "done":
        break
    try:
        count = int(input(f"Enter play count for {song}: "))
        songs.append(song)
        plays.append(count)
    except ValueError:
        print("Invalid number, try again.")

print("\n--- Playlist ---")
for i in range(len(songs)):
    print(f"{songs[i]:20} {plays[i]} plays")

most_played = songs[plays.index(max(plays))]
least_played = songs[plays.index(min(plays))]
unique_songs = set(songs)
total_plays = sum(plays)
average_plays = total_plays / len(plays)

print(f"\nMost Played: {most_played}")
print(f"Least Played: {least_played}")
print(f"Unique Songs: {len(unique_songs)}")
print(f"Total Plays: {total_plays}")
print(f"Average Plays per Song: {average_plays:.2f}")

# ===========================================================
# 1. Which mini-project felt most realistic, and why?
#    → The Grocery Analyzer felt most realistic because it simulates how stores track and adjust prices interactively.
#
# 2. How do loops make data handling easier?
#    → Loops automate repetitive tasks like printing lists, updating records, or computing totals without rewriting code.
#
# 3. What did you find challenging about combining loops with collections?
#    → Managing synchronization between related lists (like students and grades) can be tricky, especially when adding data dynamically.
#
# 4. One idea for how you could expand any of these mini-projects.
#    → The Student Tracker could be expanded into a full grading system with letter grades, data saving, and performance charts.
