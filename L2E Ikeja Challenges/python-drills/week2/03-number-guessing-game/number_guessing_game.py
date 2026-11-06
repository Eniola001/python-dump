import random


def play_game(target=None, max_attempts=None):
    # Choose a random number if target is not provided
    if target is None:
        target = random.randint(1, 100)

    guesses = 0

    while True:
        # Check whether the maximum attempts have been used
        if max_attempts is not None and guesses >= max_attempts:
            print(f"game over! the number was {target}")
            return

        try:
            guess = input("guess a number between 1 and 100: ")
            guess = int(guess)

            # Validate the guess
            if guess < 1 or guess > 100:
                print("invalid input. enter a whole number between 1 and 100.")
                continue

        except ValueError:
            print("invalid input. enter a whole number between 1 and 100.")
            continue

        # Count only valid guesses
        guesses += 1

        # Compare the guess with the target
        if guess > target:
            print("too high")
        elif guess < target:
            print("too low")
        else:
            print(f"correct! you got it in {guesses} guesses")
            return


def main():
    while True:
        play_game(max_attempts=7)

        while True:
            again = input("would you like to play again? (yes/no): ").strip().lower()

            if again in ("yes", "y"):
                break
            elif again in ("no", "n"):
                print("thanks for playing!")
                return
            else:
                print("invalid input. enter yes or no.")


# Do not modify below this line
if __name__ == "__main__":
    play_game()
