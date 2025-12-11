import os


def load_passwords(filename="passwords.txt"):
    """Load valid passwords from a file (relative to this script) and return as a list."""
    try:
        base_dir = os.path.dirname(__file__)
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"ERROR: {filename} not found at {filepath}!")
        return []


def get_numeric_input():
    """Request a 5-digit numeric code per flowchart rules."""
    user_input = input("Enter your 5-digit password: ")

    # Flowchart block: Convert ASCII → Validate number
    if not user_input.isdigit():
        print("Invalid Input! Numbers only.")
        return None

    if len(user_input) != 5:
        print("Invalid Input! Must be exactly 5 digits.")
        return None

    return user_input


def password_loop(valid_passwords, alarm_status):
    """
    Runs the password checking loop EXACTLY as in the flowchart.
    Returns updated alarm_status.
    """

    password_attempts = 5   # Flowchart: Set password_attempts to 5

    while True:

        user_input = get_numeric_input()  # Display → Enter your 5-digit password

        # If invalid format, go back to the loop without losing an attempt
        if user_input is None:
            continue

        # Flowchart: Create password list (even if already loaded)
        passwords_list = valid_passwords

        # Flowchart: Check Password decision
        if user_input in passwords_list:

            # Flowchart: Password Match branch
            if alarm_status == "off":
                alarm_status = "on"
            else:
                alarm_status = "off"

            print("\nPassword Match!")
            print("alarm_status:", alarm_status)
            return alarm_status

        else:
            # Flowchart: Incorrect Password branch
            password_attempts -= 1
            print("Invalid Password!")
            print("Attempts Remaining:", password_attempts)

            # Flowchart: Password attempts decision
            if password_attempts == 0:
                print("No attempts left → Alarm TRIPPED!")
                return alarm_status  # Final exit


def main():
    alarm_status = "off"

    valid_passwords = load_passwords()

    print("SYSTEM READY")

    # Phase 1 → Turn alarm ON
    print("\n--- ACTIVATE ALARM ---")
    alarm_status = password_loop(valid_passwords, alarm_status)

    if alarm_status != "on":
        # Flowchart: If failed activation (or tripped) → End
        print("\nAlarm Did Not Activate. System Locked.")
        return

    print("\nAlarm Activated Successfully.")

    # Phase 2 → Turn alarm OFF
    print("\n--- DEACTIVATE ALARM ---")
    alarm_status = password_loop(valid_passwords, alarm_status)


if __name__ == "__main__":
    main()