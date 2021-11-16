from math import floor

from .Player import Player
from .Pyramid import Pyramid
from .Board import Board
from .utils.json_file_reader import read_json_file


class Game:
    def __init__(self, player1_name, player2_name):
        # one board
        self.board = Board()

        # one empty pyramid
        self.pyramid = None

        # two new players
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.active_player = self.player1

    def play(self):
        for i in [1, 2, 3]:
            self.start_age(i)
            self.play_until_pyramid_is_empty()

    def play_until_pyramid_is_empty(self):
        while self.pyramid.current_number_of_cards > 0:
            action_result = self.active_player.wait_for_action(self.board, self.pyramid)  # FIXME
            if action_result.win:
                self.trigger_win(self.active_player)
            if not action_result.replay:
                self.switch_active_player()

    def trigger_win(self, player):
        print("player {} wins!".format(player.name))  # FIXME interrupt

    def calculate_scores(self):
        p1_score = 0
        p2_score = 0
        p1_score += floor(self.player1.coins/3)
        p2_score += floor(self.player2.coins/3)

    def switch_active_player(self):
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1

    def start_age(self, age_number):
        assert(age_number in [1, 2, 3])
        cards = []  # FIXME
        pyramid_filepath = "../resource/PyramidStructures/age_{}.json".format(age_number)
        pyramid_structure = read_json_file(pyramid_filepath)
        self.pyramid = Pyramid(pyramid_structure, cards)
