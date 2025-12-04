# Input Number Checker

# Start
while True:
    # Get Steps (1–26) or 0 to Exit
    user_input = input("Enter a number (1–26) or 0 to exit: ")

    # Try converting to integer
    try:
        steps = int(user_input)
    except ValueError:
        print("Invalid Selection")
        continue

    # Check for exit
    if steps == 0:
        print("Exiting program...")
        break

    # Check for valid steps
    if 1 <= steps <= 26:
        print("Well Done")
        break   # End after valid entry
    else:
        print("Invalid Selection")
