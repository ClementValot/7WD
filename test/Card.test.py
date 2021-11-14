import unittest
from src.Card import Card


class CardTest(unittest.TestCase):
    def test_constructor(self):
        my_card = Card("myCardName")
        print(my_card)
        self.assertEqual(my_card.name, 'myCardName')


if __name__ == '__main__':
    unittest.main()
