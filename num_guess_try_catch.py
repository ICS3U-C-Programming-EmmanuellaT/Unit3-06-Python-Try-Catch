#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 20th Oct, 2026
# This program asks the for a number between 0 and 9 and
# checks if the input is valid or not. If the input is valid,
# it will display the number back to the user or if the input
# is invalid, it will display an error message.
import random


def main():
    # a number between 0 and 9
    random_number = random.randint(0, 9)
    try:
        # Get the number from the user and convert it to an integer.
        number = int(input("Enter a number between 0 and 9: "))
    except ValueError:
        print("Invalid input, the input is not an integer")
    else:
        # Check if the number is correct and display the result.
        if number == random_number:
            print("You guessed the right number: {0}".format(number))
        else:
            print("You guessed the wrong number. Try again.")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
