import csv
from datetime import datetime


# ======================================================

def daily_log_writer():
    """Allows user to write daily notes into daily_log.txt with timestamps."""
    print("\n=== 📝 DAILY LOG WRITER ===")
    count = 0
    with open("daily_log.txt", "a") as file:
        while True:
            entry = input("Enter a daily note (or type 'done' to finish): ").strip()
            if entry.lower() == "done":
                break
            elif entry == "":
                print("Empty entry skipped.")
                continue
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {entry}\n")
            count += 1

    print("\n--- Your Daily Log ---")
    with open("daily_log.txt", "r") as file:
        content = file.read()
        print(content)
    print(f"Total entries recorded: {count}\n")

# ======================================================

def inventory_reader():
    """Reads inventory.txt, calculates total and average prices."""
    print("\n=== 🛒 INVENTORY READER ===")

    if not open("inventory.txt", "a+").read().strip():
        with open("inventory.txt", "w") as f:
            f.write("Apples,3.50\nBananas,2.75\nBread,2.99\n")

    total = 0
    count = 0

    with open("inventory.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue 
            try:
                name, price = line.split(",")
                price = float(price)
                total += price
                count += 1
                print(f"Item: {name:<10} | Price: ${price:.2f}")
            except ValueError:
                print(f"⚠ Skipping invalid line: {line}")

    if count > 0:
        avg = total / count
        print(f"\nTotal inventory value: ${total:.2f}")
        print(f"Average item price:   ${avg:.2f}")
    else:
        print("No valid items found in inventory.\n")

# ======================================================

def cafe_sales_export():
    """Writes café sales data to a CSV file, optionally adding more items."""
    print("\n=== ☕ CAFE SALES EXPORT ===")

    sales = [
        ["Latte", 12, 3.25],
        ["Tea", 10, 2.50],
        ["Muffin", 5, 2.00]
    ]

    while True:
        add = input("Add a new sale? (y/n): ").lower()
        if add == 'n':
            break
        elif add == 'y':
            item = input("Item name: ")
            try:
                qty = int(input("Quantity sold: "))
                price = float(input("Price each: "))
                sales.append([item, qty, price])
            except ValueError:
                print("Invalid input. Skipping entry.")
        else:
            print("Please enter 'y' or 'n'.")

    total_revenue = 0
    with open("cafe_sales.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Quantity", "Price"])
        for row in sales:
            writer.writerow(row)
            total_revenue += row[1] * row[2]
        writer.writerow(["Total Revenue", "", round(total_revenue, 2)])

    print(f"\nSales data saved to cafe_sales.csv")
    print(f"Total revenue: ${total_revenue:.2f}\n")


# ======================================================

def student_grades_report():
    """Reads grades.csv, calculates stats, and writes summary to text file."""
    print("\n=== 🎓 STUDENT GRADES REPORT ===")
    
    if not open("grades.csv", "a+").read().strip():
        with open("grades.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Grade"])
            writer.writerow(["Ava", 88])
            writer.writerow(["Noah", 92])
            writer.writerow(["Liam", 79])

    names, grades = [], []

    with open("grades.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None) 
        for row in reader:
            try:
                name, grade = row[0], float(row[1])
                names.append(name)
                grades.append(grade)
                print(f"{name}: {grade}")
            except (ValueError, IndexError):
                print(f"⚠ Skipping invalid row: {row}")

    if grades:
        avg = sum(grades) / len(grades)
        highest = max(grades)
        lowest = min(grades)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("grades_summary.txt", "w") as summary:
            summary.write("=== Grades Summary ===\n")
            summary.write(f"Average Grade: {avg:.2f}\n")
            summary.write(f"Highest Grade: {highest}\n")
            summary.write(f"Lowest Grade: {lowest}\n")
            summary.write(f"Timestamp: {timestamp}\n\n")

            summary.write("Pass/Fail Results:\n")
            for name, grade in zip(names, grades):
                result = "Pass" if grade >= 50 else "Fail"
                summary.write(f"{name}: {grade} ({result})\n")

        print(f"\nAverage: {avg:.2f}")
        print(f"Highest: {highest}")
        print(f"Lowest:  {lowest}")
        print("Grades summary written to grades_summary.txt\n")
    else:
        print("No valid grade data found.\n")

# ======================================================

def main():
    while True:
        print("========== MAIN MENU ==========")
        print("A) Daily Log Writer")
        print("B) Inventory Reader")
        print("C) Café Sales Export")
        print("D) Student Grades Report")
        print("E) Exit Program")
        print("===============================")
        choice = input("Choose an option (A–E): ").lower()

        if choice == 'a':
            daily_log_writer()
        elif choice == 'b':
            inventory_reader()
        elif choice == 'c':
            cafe_sales_export()
        elif choice == 'd':
            student_grades_report()
        elif choice == 'e':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# ======================================================

if __name__ == "__main__":
    main()


# ======================================================

# 1. File persistence allows programs to *remember* data between runs.
#    Instead of losing everything when the script stops, data is saved
#    permanently — essential for logs, records, reports, and analytics.
#
# 2. CSV files were easier for structured data since each field has a
#    clear place, and Python’s csv module simplifies reading/writing.
#    Text files were simpler for free-form notes like logs.
#
# 3. Many programs use both: for example, a café system might save daily
#    notes (text) and sales data (CSV) together for a full business report.
#
# 4. One issue I faced was skipping invalid or empty lines in text/CSV
#    files. I solved it by adding .strip() checks and try/except blocks
#    around conversions to safely ignore bad data.
