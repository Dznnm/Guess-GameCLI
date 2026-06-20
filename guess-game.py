print("Welcome to Guess the Number Game!")
difficulty = input("Enter your Difficulty (easy, medium, hard): ").lower()
if difficulty == "easy":
    number_to_guess = 5
    attempts = 10
elif difficulty == "medium":
    number_to_guess = 10
    attempts = 7
elif difficulty == "hard":
    number_to_guess = 15
    attempts = 5
else:
    print("Invalid difficulty. Please choose easy, medium, or hard.")
    exit()