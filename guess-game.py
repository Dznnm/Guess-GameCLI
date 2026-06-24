import random

print("Welcome to Guess the Number Game!")
difficulty = input("Enter your Difficulty (Easy, Medium, Hard): ").lower()
if difficulty == "easy":
    number_to_guess = random.randint(1, 20)
    attempts = 10
    print("You have 10 attempts to guess a number between 1 and 20.")
elif difficulty == "medium":
    number_to_guess = random.randint(1, 20)
    attempts = 7
    print("You have 7 attempts to guess a number between 1 and 20.")
elif difficulty == "hard":
    number_to_guess = random.randint(1, 20)
    attempts = 5
    print("You have 5 attempts to guess a number between 1 and 20.")
else:
    print("Invalid difficulty. Please choose Easy, Medium, or Hard.")
    exit()

while attempts > 0:
    user_input = input("Guess the number! or type 'exit' to quit: ").lower()
    if user_input == "exit":
        print("Exiting the game. Goodbye!")
        break
    try:
        guess = int(user_input)
    except ValueError:
        print("Please enter a number between 1 and 20.")
        continue
    if not (1 <= guess <= 20):
        print("Please enter a number between 1 and 20.")
        continue
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break
    attempts -= 1
    print(f"You have {attempts} attempts left.")
    if attempts == 0:
        print(f"Game Over! The number was {number_to_guess}.")