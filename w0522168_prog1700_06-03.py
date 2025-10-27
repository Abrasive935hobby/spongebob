
import random
import time

def number_guesser():
    print("\n🎯 NUMBER GUESSER")
    secret = random.randint(1, 10)
    guess = None
    tries = 0
    max_tries = 5

    while guess != secret and tries < max_tries:
        user_input = input("Guess a number (1–10): ")

        if not user_input.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(user_input)
        tries += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("🎉 You got it!")

    if guess != secret:
        print("You're out of tries! The number was", secret)
    print("-" * 40)


def coin_flipper():
    print("\n🪙 COIN FLIPPER")
    flips = input("How many times should I flip the coin? ")

    if not flips.isdigit():
        print("Please enter a number!")
        return
    flips = int(flips)

    heads = 0
    tails = 0
    count = 0

    while count < flips:
        flip = random.choice(["Heads", "Tails"])
        print(flip)

        if flip == "Heads":
            heads += 1
        else:
            tails += 1

        count += 1

        if count > 0 and (heads / count >= 0.7 or tails / count >= 0.7):
            print("⚠️ 70% reached! Stopping early...")
            break

    percent_heads = (heads / count) * 100
    percent_tails = (tails / count) * 100

    print(f"Heads: {heads} ({percent_heads:.1f}%), Tails: {tails} ({percent_tails:.1f}%)")
    print("-" * 40)


def countdown_timer():
    print("\n⏱️ COUNTDOWN TIMER")
    start = input("Enter a starting countdown number: ")

    if not start.isdigit():
        print("Please enter a valid number!")
        return
    start = int(start)

    while start >= 0:
        print(f"{start} {'=' * start}")
        print("\a")  # Beep sound
        time.sleep(1)
        start -= 1

    print("🚀 Blast off!")
    print("-" * 40)


def pattern_generator():
    print("\n🎨 PATTERN GENERATOR")
    rows = input("How many rows? ")
    if not rows.isdigit():
        print("Please enter a number!")
        return
    rows = int(rows)
    symbol = input("Enter a symbol or emoji: ")

    print("\nIncreasing pattern:")
    r = 1
    while r <= rows:
        print(symbol * r)
        r += 1

    print("\nDecreasing pattern:")
    r = rows
    while r > 0:
        print(symbol * r)
        r -= 1
    print("-" * 40)


def main_menu():
    while True:
        print("""
==============================
🌀 LOOP CHALLENGES MENU
==============================
1️⃣  Number Guesser
2️⃣  Coin Flipper
3️⃣  Countdown Timer
4️⃣  Pattern Generator
5️⃣  Quit
==============================
""")
        choice = input("Choose an option (1–5): ")

        if choice == "1":
            number_guesser()
        elif choice == "2":
            coin_flipper()
        elif choice == "3":
            countdown_timer()
        elif choice == "4":
            pattern_generator()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please pick 1–5.")


if __name__ == "__main__":
    main_menu()

# ----------------------------------------------------------
# Reflection:
# 1. The most fun challenge was the Number Guesser because it felt like a game.
# 2. A common mistake that caused infinite loops was forgetting to update the loop variable.
# 3. While loops can be used for real-world apps like login attempts, timers, or data checks.
# 4. The Coin Flipper helped me best understand loop conditions, since I had to think about when to stop.
