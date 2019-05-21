from string import ascii_lowercase
from wordsearch.app import GameBoard


def test_gameboard_create_row():
    row = GameBoard._create_row(size=10)
    assert len(row) == 10
    for e in row:
        assert e in ascii_lowercase


def test_create_square_game_board():
    g = GameBoard(size=9)
    assert g.size == 9
    assert g.board.shape[0] == g.size and g.board.shape[1] == g.size
    assert g.shape == g.board.shape
