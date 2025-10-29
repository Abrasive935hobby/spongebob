def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

def is_float(value):
    """Check if input can be converted to float"""
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_positive(num):
    return num > 0

def is_integer(value):
    return value.isdigit()

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def lbs_to_kg(lbs):
    return lbs * 0.453592

def kg_to_lbs(kg):
    return kg / 0.453592

def calculator():
    print("\n=== Simple Calculator ===")
    while True:
        num1 = input("Enter first number (or type 'exit' to quit): ")
        if num1.lower() == "exit":
            break
        num2 = input("Enter second number: ")
        if not (is_float(num1) and is_float(num2)):
            print("Invalid input. Please enter numeric values.")
            continue

        num1, num2 = float(num1), float(num2)
        op = input("Enter operation (+, -, *, /): ")

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator.")
            continue

        if result is not None:
            print(f"Result: {round(result, 2)}")

def unit_converter():
    print("\n=== Unit Converter ===")
    while True:
        print("\nChoose a conversion:")
        print("1. Kilometres ↔ Miles")
        print("2. Celsius ↔ Fahrenheit")
        print("3. Pounds ↔ Kilograms")
        print("4. Exit converter")

        choice = input("Enter choice: ")
        if choice == '4':
            break

        value = input("Enter the value to convert: ")
        if not is_float(value):
            print("Invalid input. Please enter a number.")
            continue
        value = float(value)

        if choice == '1':
            direction = input("Convert (k)m to miles or (m)iles to km? ").lower()
            if direction == 'k':
                print(f"{value} km = {km_to_miles(value):.1f} miles")
            elif direction == 'm':
                print(f"{value} miles = {miles_to_km(value):.1f} km")
            else:
                print("Invalid direction.")
        elif choice == '2':
            direction = input("Convert (c)elsius to fahrenheit or (f)ahrenheit to celsius? ").lower()
            if direction == 'c':
                print(f"{value}°C = {c_to_f(value):.1f}°F")
            elif direction == 'f':
                print(f"{value}°F = {f_to_c(value):.1f}°C")
            else:
                print("Invalid direction.")
        elif choice == '3':
            direction = input("Convert (p)ounds to kg or (k)g to pounds? ").lower()
            if direction == 'p':
                print(f"{value} lbs = {lbs_to_kg(value):.1f} kg")
            elif direction == 'k':
                print(f"{value} kg = {kg_to_lbs(value):.1f} lbs")
            else:
                print("Invalid direction.")
        else:
            print("Invalid option.")

def validated_input():
    print("\n=== Input Validation Example ===")
    attempts = 0
    while True:
        val = input("Enter a positive integer: ")
        attempts += 1

        if not is_integer(val):
            print("Invalid input. Please enter a whole number.")
        elif int(val) <= 0:
            print("Number must be positive.")
        else:
            print(f"Valid input! You entered {val}.")
            break

        if attempts >= 3:
            print("Too many invalid attempts.")
            break

def main():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. Input Validation Demo")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            calculator()
        elif choice == '2':
            unit_converter()
        elif choice == '3':
            validated_input()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Reflection:
# 1. Using functions made the code much more organized and reusable.
#    Each feature (calculator, converter, validation) is separate, making debugging easier.
#
# 2. The calculator felt most useful because it demonstrates function calls, loops, and validation together.
#
# 3. Modular code helps large projects by allowing different developers to work on separate parts
#    without breaking other sections. It also makes maintenance and testing simpler.
#
# 4. In the real world, functions are used in everything from web applications to data analysis
#    — for example, using modular functions to handle data input, cleaning, and reporting separately.
