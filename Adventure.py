""" File: Adventure.py

    This module starts the adventure game.

    To play the game, run this file or type the following command:
    >>> python -m program

    There are two options for playing this game:

    "Small"     A 12-room Adventure for getting a taste of the game.
    "Crowther"  The full 77-room Adventure game.
"""

"""This file runs the Adventure game."""

from AdvGame import AdvGame

# Constants

DATA_FILE_PREFIX = "Crowther"

# Main program

def adventure():
    game = AdvGame(DATA_FILE_PREFIX)
    game.run()

# Startup code

if __name__ == "__main__":
    adventure()