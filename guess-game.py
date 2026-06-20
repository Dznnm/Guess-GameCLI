import random

print("Welcome to Guess the Number Game!")
difficulty = input("Enter your Difficulty (easy, medium, hard): ").lower()
if difficulty == "easy":
    number_to_guess = random.randint(1, 20)
    attempts = 10
elif difficulty == "medium":
    number_to_guess = random.randint(1, 50)
    attempts = 7
elif difficulty == "hard":
    number_to_guess = random.randint(1, 100)
    attempts = 5
else:
    print("Invalid difficulty. Please choose easy, medium, or hard.")
    exit()