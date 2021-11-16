from unittest import TestCase
from src.Player import Player


class TestPlayer(TestCase):

    def setUp(self) -> None:
        self.my_player = Player("Jean", 1)

    def test_constructor(self):
        self.assertEqual(self.my_player.name, "Jean")
        self.assertEqual(self.my_player.number, 1)
        self.assertEqual(self.my_player.coins, 0)

    def test_give_coins(self):
        self.assertEqual(self.my_player.coins, 0)
        self.my_player.give_coins(2)
        self.assertEqual(self.my_player.coins, 2)
        self.assertEqual(self.my_player.give_coins(5), 7)

    def test_remove_coins(self):
        self.my_player.give_coins(5)
        self.my_player.remove_coins(3)
        self.assertEqual(self.my_player.coins, 2)
        self.assertEqual(self.my_player.remove_coins(12), 0)
