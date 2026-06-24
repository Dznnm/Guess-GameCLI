# Number Guessing Game CLI

A simple command-line Number Guessing Game built with Python as part of the roadmap.sh backend projects.

## Project URL

https://roadmap.sh/projects/number-guessing-game

## Description

The computer generates a random number, and the player must guess it before running out of attempts.

Players can choose between three difficulty levels:

| Difficulty | Attempts | Number Range |
| ---------- | -------- | ------------ |
| Easy       | 10       | 1–20         |
| Medium     | 7        | 1–20         |
| Hard       | 5        | 1–20         |

After each guess, the game provides feedback indicating whether the guess is too high or too low.

The player wins by guessing the correct number before running out of attempts.

---

## Features

* Random number generation
* Three difficulty levels
* Limited attempts based on difficulty
* Higher / Lower hints
* Input validation for non-numeric values
* Range validation (1–20)
* Exit command (`exit`)
* Win and lose conditions
* Remaining attempts counter

---

## Technologies Used

* Python 3
* Random module

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

Navigate to the project directory:

```bash
cd <repository-name>
```

Run the program:

```bash
python number_guessing_game.py
```

---

## Example Gameplay

```text
Welcome to Guess the Number Game!

Enter your Difficulty (Easy, Medium, Hard): medium

You have 7 attempts to guess a number between 1 and 20.

Guess the number! or type 'exit' to quit: 10
Too low! Try again.
You have 6 attempts left.

Guess the number! or type 'exit' to quit: 15
Too high! Try again.
You have 5 attempts left.

Guess the number! or type 'exit' to quit: 13
Congratulations! You've guessed the number!
```

---

## Exit Example

```text
Guess the number! or type 'exit' to quit: exit

Exiting the game. Goodbye!
```

---

## Learning Objectives

This project was built to practice:

* Variables
* User input
* Conditional statements
* Loops
* Exception handling
* State management
* Input validation
* Random number generation

---

## Future Improvements

Potential enhancements:

* Play Again feature
* Score tracking
* Difficulty settings using dictionary mapping
* Custom number ranges
* Best score leaderboard
* Function-based refactoring

---

## Author

Dzannun Muhlashon
