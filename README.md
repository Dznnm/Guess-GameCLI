# Number Guessing Game CLI

A simple command-line Number Guessing Game built with Python as part of the roadmap.sh backend projects.

## Project URL

https://roadmap.sh/projects/number-guessing-game

## Description

This game generates a random number and challenges the player to guess it within a limited number of attempts.

Players can choose between three difficulty levels:

* Easy: 10 attempts
* Medium: 7 attempts
* Hard: 5 attempts

The game provides feedback after each guess:

* Too high
* Too low
* Correct guess

The game also validates user input to prevent crashes caused by invalid entries.

## Features

* Random number generation
* Multiple difficulty levels
* Input validation
* Remaining attempts counter
* Win and lose conditions
* Helpful feedback after each guess

## Technologies Used

* Python 3
* Random module

## How to Run

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate to the project folder:

```bash
cd number-guessing-game
```

3. Run the program:

```bash
python number_guessing_game.py
```

## Example Gameplay

```text
Welcome to Guess the Number Game!

Enter your Difficulty (Easy, Medium, Hard): medium

You have 7 attempts to guess a number between 1 and 20.

Guess the number!: 10
Too low! Try again.
You have 6 attempts left.

Guess the number!: 15
Too high! Try again.
You have 5 attempts left.

Guess the number!: 13
Congratulations! You've guessed the number!
```

## Learning Objectives

This project helped practice:

* Variables
* User input
* Conditional statements
* Loops
* Exception handling
* Game state management
* Random number generation

## Author

Dzannun Muhlashon
