from unittest import TestCase
from src.Board import Board, WarBoard


class TestWarBoard(TestCase):
    def test_constructor(self):
        my_warboard = WarBoard()
        self.assertEqual(my_warboard.war_token_position, 0)


class TestBoard(TestCase):
    def test_constructor(self):
        my_board = Board()
        self.assertEqual(my_board.war_board.war_token_position, 0)
