import os
import sys


def load_passwords(filename="passwords.txt"):
    """Load valid passwords from a file and return as a list.

    Behavior:
    - If `filename` is an absolute path, open it directly.
    - Otherwise try to open relative to this script's directory (when `__file__` is present).
    - If that fails, fall back to the current working directory.
    Returns an empty list on failure.
    """
    # If an absolute path was provided, prefer it.
    try:
        if os.path.isabs(filename):
            filepath = filename
        else:
            # Prefer the script's directory when available; otherwise use cwd
            base_dir = os.path.dirname(__file__) if '__file__' in globals() else os.getcwd()
            filepath = os.path.join(base_dir, filename)

        with open(filepath, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        # Try fallback: open filename directly from current working directory
        try:
            filepath = os.path.join(os.getcwd(), filename)
            with open(filepath, "r") as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"ERROR: {filename} not found at {filepath}!")
            return []


def get_numeric_input():
    """Request a 5-digit numeric code per flowchart rules."""
    user_input = input("Enter your 5-digit password: ")

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

    password_attempts = 5  

    while True:

        user_input = get_numeric_input()  

        if user_input is None:
            continue

        passwords_list = valid_passwords

        if user_input in passwords_list:

            if alarm_status == "off":
                alarm_status = "on"
            else:
                alarm_status = "off"

            print("\nPassword Match!")
            print("alarm_status:", alarm_status)
            return alarm_status

        else:
            password_attempts -= 1
            print("Invalid Password!")
            print("Attempts Remaining:", password_attempts)

            if password_attempts == 0:
                print("No attempts left → Alarm TRIPPED!")
                return alarm_status 


def main():
    alarm_status = "off"

    valid_passwords = load_passwords()

    print("SYSTEM READY")

    print("\n--- ACTIVATE ALARM ---")
    alarm_status = password_loop(valid_passwords, alarm_status)

    if alarm_status != "on":
        print("\nAlarm Did Not Activate. System Locked.")
        return

    print("\nAlarm Activated Successfully.")

    print("\n--- DEACTIVATE ALARM ---")
    alarm_status = password_loop(valid_passwords, alarm_status)


if __name__ == "__main__":
    main()