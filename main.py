
import random
import time

# -----------------------------
# Difficulty settings
# -----------------------------
def choose_difficulty():
    print("\n Choose Difficulty")
    print("1. Easy   (1-10, 6 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard   (1-100, 10 attempts)")

    choice = input("Select (1/2/3): ")

    if choice == "2":
        return 1, 50, 7
    elif choice == "3":
        return 1, 100, 10
    else:
        return 1, 10, 6  # default easy


# -----------------------------
# Main game
# -----------------------------
def play_game():
    low, high, attempts = choose_difficulty()
    secret = random.randint(low, high)

    print(f"\n Guess the number between {low} and {high}")
    print(f"You have {attempts} attempts\n")

    start_time = time.time()

    for i in range(1, attempts + 1):

        # Safe input handling
        user_input = input(f"Attempt {i}: ")

        if not user_input.isdigit():
            print(" Enter a valid number!")
            continue

        guess = int(user_input)

        if guess == secret:
            end_time = time.time()
            time_taken = round(end_time - start_time, 2)

            print("\n You won!")
            print(f" Attempts used: {i}")
            print(f" Time: {time_taken} seconds")

            # Simple score system
            score = (attempts - i + 1) * 10
            print(f" Score: {score}")

            return

        elif guess < secret:
            print(" Too low")
        else:
            print(" Too high")

        # Hint system
        if abs(guess - secret) <= 2:
            print(" VERY CLOSE!")

    print(f"\n Out of attempts! The number was {secret}")


# -----------------------------
# Game loop
# -----------------------------
def main():
    print("🎮 Advanced Guessing Game")

    while True:
        play_game()

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("👋 Goodbye!")
            break


# Run program
if __name__ == "__main__":
    main()
