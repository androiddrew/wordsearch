import numpy as np
from string import ascii_lowercase
import random


class GameBoard:
    """A square board of random letters."""

    def __init__(self, size: int = 15):
        self.size = size
        self.board = self._generate_square_board(size=size)

    @classmethod
    def _generate_square_board(cls, size: int):
        """Creates a 2 dimensional array of random ascii characters."""
        return np.array([cls._create_row(size) for j in range(0, size)])

    @classmethod
    def _create_row(cls, size: int):
        """Creates a single array of random ascii characters."""
        return [random.choice(ascii_lowercase) for i in range(0, size)]

    @property
    def shape(self):
        return self.board.shape

    def __str__(self):
        """Pretty prints the game board."""
        s = ""
        for row in self.board:
            s += "| " + "  ".join(row) + " |\n"
        return s
