import random
import re
import numpy as np
from string import ascii_lowercase

WORD_RE = re.compile("^[a-zA-Z]+$")


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


class WordIndex:
    """A contains a list of words used to search a game board grid."""

    def __init__(self, words=[]):
        self.index = {}
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        """Adds a word to the index."""
        if not isinstance(word, str) or not WORD_RE.match(word):
            raise ValueError(
                f"WordIndex entries must be type str or matching the {WORD_RE} regex pattern: {word}"
            )
        word = word.lower()
        if word[0] in self.index.keys():
            self.index[word[0]].append(word)
        else:
            self.index[word[0]] = [word]

    def sort_index(self):
        for k, v in self.index.items():
            v.sort()

    @classmethod
    def from_file(cls, path=None):
        index = cls.__call__()
        with open(path, mode="r") as f:
            for line in f:
                index.add_word(line.strip())
        return index
