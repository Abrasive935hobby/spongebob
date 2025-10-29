
# ======================================================

import os
import csv
from datetime import datetime

# ======================================================

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def log_calculation(a, b, op, result):
    """Append a calculation record to calc_log.txt with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("calc_log.txt", "a") as f:
        f.write(f"[{timestamp}] {a} {op} {b} = {result}\n")

def calculator():
    """Run calculator interface."""
    print("\n=== 🧮 CALCULATOR ===")
    calc_count = 0
    while True:
        print("\nType 'calc' to perform a calculation, 'view' to view log, or 'exit' to return.")
        choice = input("Option: ").lower()

        if choice == 'exit':
            break
        elif choice == 'view':
            if os.path.exists("calc_log.txt"):
                with open("calc_log.txt", "r") as f:
                    print("\n--- Calculation Log ---")
                    print(f.read())
            else:
                print("No log file found yet.")
        elif choice == 'calc':
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            op = input("Enter operation (+, -, *, /): ")

            try:
                a, b = float(a), float(b)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if op == '+': result = add(a, b)
            elif op == '-': result = subtract(a, b)
            elif op == '*': result = multiply(a, b)
            elif op == '/': result = divide(a, b)
            else:
                print("Invalid operator.")
                continue

            if result is not None:
                result = round(result, 2)
                print(f"Result: {result}")
                log_calculation(a, b, op, result)
                calc_count += 1
        else:
            print("Invalid option. Try again.")
    return calc_count

# ======================================================

def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def km_to_miles(km): return km * 0.621371
def miles_to_km(miles): return miles / 0.621371

def save_conversion(conv_type, input_val, output_val):
    """Append conversion details to conversions.csv with a header if needed."""
    file_exists = os.path.exists("conversions.csv")
    with open("conversions.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Type", "Input", "Output", "Timestamp"])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([conv_type, input_val, output_val, timestamp])

def unit_converter():
    """Run unit converter interface."""
    print("\n=== 🔁 UNIT CONVERTER ===")
    conv_count = 0
    while True:
        print("\nSelect conversion:")
        print("1. Celsius ↔ Fahrenheit")
        print("2. Kilometres ↔ Miles")
        print("3. View conversion history")
        print("4. Exit converter")

        choice = input("Enter choice: ").strip()
        if choice == '4':
            break
        elif choice == '3':
            if os.path.exists("conversions.csv"):
                with open("conversions.csv", "r") as f:
                    print("\n--- Conversion History ---")
                    print(f.read())
            else:
                print("No conversion history found.")
        elif choice in ['1', '2']:
            value = input("Enter value to convert: ")
            try:
                value = float(value)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                direction = input("Convert (c)elsius → Fahrenheit or (f)ahrenheit → Celsius? ").lower()
                if direction == 'c':
                    result = round(c_to_f(value), 2)
                    print(f"{value}°C = {result}°F")
                    save_conversion("C to F", value, result)
                elif direction == 'f':
                    result = round(f_to_c(value), 2)
                    print(f"{value}°F = {result}°C")
                    save_conversion("F to C", value, result)
                else:
                    print("Invalid direction.")
                    continue
            elif choice == '2':
                direction = input("Convert (k)m → miles or (m)iles → km? ").lower()
                if direction == 'k':
                    result = round(km_to_miles(value), 2)
                    print(f"{value} km = {result} miles")
                    save_conversion("Km to Miles", value, result)
                elif direction == 'm':
                    result = round(miles_to_km(value), 2)
                    print(f"{value} miles = {result} km")
                    save_conversion("Miles to Km", value, result)
                else:
                    print("Invalid direction.")
                    continue
            conv_count += 1
        else:
            print("Invalid option.")
    return conv_count

# ======================================================

def create_session_summary(calc_total, conv_total):
    """Write session summary to text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("session_summary.txt", "w") as f:
        f.write("=== SESSION SUMMARY ===\n")
        f.write(f"Total Calculations: {calc_total}\n")
        f.write(f"Total Conversions: {conv_total}\n")
        f.write(f"Session End: {timestamp}\n")
    print("\n📄 Session summary saved to 'session_summary.txt'.")
    
# ======================================================

def main():
    total_calcs = 0
    total_convs = 0

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Calculator Module")
        print("2. Converter Module")
        print("3. Exit and Generate Report")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            total_calcs += calculator()
        elif choice == '2':
            total_convs += unit_converter()
        elif choice == '3':
            create_session_summary(total_calcs, total_convs)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1–3.")

if __name__ == "__main__":
    main()

# ======================================================
# Reflection:
# 1. File persistence is vital in real-world applications because it allows
#    data to be retained across sessions — for logs, reports, and analytics.
#
# 2. CSV was more suitable for structured data like conversions since
#    it supports tabular formats readable by both humans and software.
#    Text logs were perfect for plain event-style records like calculations.
#
# 3. Combining functions with file I/O made the code modular and organized:
#    each module handles its logic and persistence independently.
#
# 4. In an expanded version, I’d store user preferences, recent activities,
#    or analytics (like most used conversions) for deeper functionality.
