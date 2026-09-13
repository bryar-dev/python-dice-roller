Python Dice Roller

A simple Python program that allows the user to roll two six-sided dice repeatedly.

Features

* Roll two dice at the same time
* Generate random numbers between 1 and 6
* Continue rolling until the user chooses to quit
* Accepts both uppercase and lowercase input
* Basic input validation

What I Learned

This project helped me practise:

* `while` loops
* `if`, `elif`, and `else` statements
* User input with `input()`
* Generating random numbers with Python's `random` module
* Using `.upper()` to handle different user inputs
* Basic input validation

How It Works

The program asks the user whether they would like to roll the dice.

* Enter `y` to roll two dice.
* Enter `n` to stop playing.
* Any other input produces an error message.

Each die generates a random number from **1 to 6** using Python's `random.randint()` function.

How to Run

1. Make sure Python is installed.
2. Download or clone this repository.
3. Open `dice_roller.py`.
4. Run the program in a Python IDE or terminal.
5. Follow the instructions displayed in the terminal.

Example

```text
Would you like to roll dice? (y/n) y
You rolled a 3 and a 6

Would you like to roll dice? (y/n) y
You rolled a 1 and a 4

Would you like to roll dice? (y/n) n
Thank you for playing!
```

## Technologies Used

* **Python**
* **Python `random` module**

