
import random
import time

valid_moves = ["rock", "paper", "scissors", "lizard", "spock"]
valid_set = set(valid_moves)

score = {"player": 0, "cpu": 0, "ties": 0}
history = []

wins_over = {
    ("rock", "scissors"), ("rock", "lizard"),
    ("paper", "rock"), ("paper", "spock"),
    ("scissors", "paper"), ("scissors", "lizard"),
    ("lizard", "spock"), ("lizard", "paper"),
    ("spock", "rock"), ("spock", "scissors")
}

def get_player_move(valid_set):
    """Prompt user for move, accept abbreviations, validate input."""
    while True:
        move = input("Enter your move (rock/paper/scissors/lizard/spock): ").strip().lower()
        # Accept first letters (accessibility enhancement)
        abbreviations = {"r": "rock", "p": "paper", "s": "scissors", "l": "lizard", "sp": "spock"}
        if move in abbreviations:
            move = abbreviations[move]
        if move in valid_set:
            return move
        print("❌ Invalid move. Try again.\n")

def get_cpu_move(valid_moves):
    """Randomly choose a CPU move."""
    return random.choice(valid_moves)

def decide_winner(player, cpu):
    """Return 'player', 'cpu', or 'tie' based on move rules."""
    if player == cpu:
        return "tie"
    elif (player, cpu) in wins_over:
        return "player"
    else:
        return "cpu"

def print_scoreboard(score):
    """Display the current scoreboard."""
    print("\n===== SCOREBOARD =====")
    print(f"Player Wins: {score['player']}")
    print(f"CPU Wins:    {score['cpu']}")
    print(f"Ties:        {score['ties']}")
    print("======================\n")

def print_history(history):
    """Display full match history."""
    print("\n===== MATCH HISTORY =====")
    for record in history:
        print(f"Round {record['round']}: Player({record['player']}) vs CPU({record['cpu']}) → {record['result'].upper()}")
    print("==========================\n")

def get_best_of():
    """Ask player for an odd 'best-of' number."""
    while True:
        try:
            n = int(input("Play best of how many rounds? (3, 5, 7): "))
            if n in [3, 5, 7]:
                return n
            print("❌ Please enter an odd number: 3, 5, or 7.\n")
        except ValueError:
            print("❌ Invalid input. Enter a number.\n")

def analyze_history(history):
    """Compute most used moves by player and CPU."""
    if not history:
        print("No history yet.")
        return

    from collections import Counter
    player_moves = Counter([r["player"] for r in history])
    cpu_moves = Counter([r["cpu"] for r in history])

    print("===== MOVE ANALYTICS =====")
    print(f"Most used by PLAYER: {player_moves.most_common(1)[0][0].title()} ({player_moves.most_common(1)[0][1]} times)")
    print(f"Most used by CPU:    {cpu_moves.most_common(1)[0][0].title()} ({cpu_moves.most_common(1)[0][1]} times)")
    print("==========================\n")

def play_game():
    print("\n🎮 Welcome to RPS+ (Rock, Paper, Scissors, Lizard, Spock)!")
    print("First to win majority of chosen rounds wins the match.\n")

    global history, score
    history.clear()
    score = {"player": 0, "cpu": 0, "ties": 0}

    best_of = get_best_of()
    win_target = best_of // 2 + 1

    round_num = 0

    while score["player"] < win_target and score["cpu"] < win_target:
        round_num += 1
        print(f"--- ROUND {round_num} ---")

        player_move = get_player_move(valid_set)
        cpu_move = get_cpu_move(valid_moves)

        print(f"You chose {player_move.title()}...")
        time.sleep(0.5)
        print(f"CPU chose {cpu_move.title()}...")
        time.sleep(0.5)

        result = decide_winner(player_move, cpu_move)
        if result == "player":
            print("✅ You win this round!")
            score["player"] += 1
        elif result == "cpu":
            print("💻 CPU wins this round!")
            score["cpu"] += 1
        else:
            print("🤝 It's a tie!")
            score["ties"] += 1

        history.append({
            "round": round_num,
            "player": player_move,
            "cpu": cpu_move,
            "result": result
        })

        print_scoreboard(score)
        time.sleep(0.5)

    print("🎉 MATCH COMPLETE!")
    if score["player"] > score["cpu"]:
        print("🏆 You won the match!")
    else:
        print("💻 CPU won the match!")

    print_history(history)
    analyze_history(history)

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing RPS+! Goodbye 👋\n")
            break

if __name__ == "__main__":
    main()

# REFLECTION QUESTIONS
# 1) Which function was most useful to keep your code organized? Why?
# The 'decide_winner()' function, since it centralizes the win logic and makes it easy to modify for extra moves like Lizard and Spock.
#
# 2) What bug or edge case did you fix (describe inputs + expected vs actual)?
# Input validation for 'spock' abbreviation — initially 's' conflicted with 'scissors', so we added 'sp' for clarity.
#
# 3) Which data structure (list/set/dict) felt best for each part (why)?
# List for valid_moves, set for fast validation, dict for score/history records for easy key access.
#
# 4) If you had one more hour, what improvement would you ship next? 
# Add a streak tracker and save results to a text file for session history.