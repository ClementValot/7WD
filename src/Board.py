from .Effectable import Effectable
from .utils.json_file_reader import read_json_file


class Board:
    def __init__(self):
        self.war_board = WarBoard()


class WarBoard:
    def __init__(self):
        warboard_params = read_json_file('../resource/WarBoard/WarBoard.json')
        self.war_token_position: int = warboard_params['initial_token_position']
        self.objectives_numbers: [int] = map(int, warboard_params["objectives"].keys())
        self.effectables = {}
        for objective_number in self.objectives_numbers:
            self.effectables[objective_number] = Effectable(warboard_params["objectives"][str(objective_number)])
            # FIXME

    def move_token(self, player, number, board):
        initial_position: int = self.war_token_position
        if player.number == 1:
            player_sign: int = +1
        else:
            player_sign: int = -1
        self.war_token_position += player_sign * number
        for objective_number in self.objectives_numbers:
            if (player_sign * objective_number > 0) and abs(initial_position) <= abs(objective_number) <= abs(
                    self.war_token_position):
                self.__do_objective(objective_number, player, board)

    def __do_objective(self, objective_number, player, board):
        player.apply_effect(self.effectables[objective_number], board)
        del (self.effectables[objective_number])
