import unittest
from src.Card import Card
from src.Pyramid import Pyramid
from src.utils.json_file_reader import read_json_file


class PyramidTest(unittest.TestCase):

    def test_constructor(self):
        card_list = generate_card_list()
        my_pyramid = Pyramid(read_json_file("../resource/PyramidStructures/age_1.json"), card_list)
        self.assertEqual(my_pyramid.rows, 5)
        self.assertEqual(my_pyramid.max_row_length, 11)

    def test_get_remove_card(self):
        my_pyramid = Pyramid(
            read_json_file("../resource/PyramidStructures/age_1.json"),
            generate_card_list()
        )
        self.assertEqual(my_pyramid.get_card(4, 0).name, "myCard 6")
        self.assertEqual(my_pyramid.get_card(3, 1).name, "myCard 11")
        removed_card = my_pyramid.remove_card(4, 0)
        self.assertEqual(removed_card.name, "myCard 6")
        self.assertEqual(my_pyramid.get_card(4, 0), None)

    def test_display(self):
        my_pyramid = Pyramid(
            read_json_file("../resource/PyramidStructures/age_1.json"),
            generate_card_list()
        )
        self.assertEqual()
        return


def generate_card_list() -> [Card]:
    card_list = []
    for i in range(20):
        card_list.append(Card("myCard " + str(i+1)))
    return card_list


if __name__ == '__main__':
    unittest.main()
