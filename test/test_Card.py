from unittest import TestCase
from src.Card import Card


class TestCar(TestCase):
    def test_constructor(self):
        my_card = Card("myCardName")
        print(my_card)
        self.assertEqual(my_card.name, 'myCardName')
