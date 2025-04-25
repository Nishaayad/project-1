import random

def number_guess_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("🎉 Welcome to the Number Guessing Game!")
    print("🔢 I have selected a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("👉 Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("⬇️ Too low! Try again.")
            elif guess > number_to_guess:
                print("⬆️ Too high! Try again.")
            else:
                print(f"🎊 Congrats! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

number_guess_game()
