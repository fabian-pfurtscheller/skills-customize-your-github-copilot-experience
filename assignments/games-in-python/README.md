# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a console-based Hangman game in Python. You will practice loops, conditionals, string handling, and game logic by implementing guessing, progress tracking, and win/loss conditions.

## 📝 Tasks

### 🛠️	Implement Core Game Setup

#### Description
Create the initial game setup for Hangman. Define a word list, choose one word at random, and prepare variables to track guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Store at least 5 possible words in a predefined list.
- Randomly select one word from the list when the game starts.
- Initialize a variable for remaining incorrect guesses (for example, 6).
- Initialize an empty collection to store guessed letters.


### 🛠️	Build Gameplay Loop and End Conditions

#### Description
Implement the main game loop where the player enters letter guesses. Show current word progress after each guess, update attempts for incorrect guesses, and end the game with a clear result message.

#### Requirements
Completed program should:

- Prompt the player to enter one letter per turn.
- Display the word progress using underscores for unknown letters (for example, `_ a _ _ m a n`).
- Decrease remaining attempts only when the guessed letter is not in the word.
- End with a win message when all letters are guessed.
- End with a lose message when no attempts remain and reveal the hidden word.
