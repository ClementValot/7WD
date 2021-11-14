from .Effectable import Effectable
from .utils.json_file_reader import read_json_file

class Board:
    def __init__(self):
        self.war_board = WarBoard()


class WarBoard:
    def __init__(self):
        warboard_params = read_json_file('../resource/WarBoard/WarBoard.json')
        self.war_token_position = warboard_params['initial_token_position']
        self.thresholds = warboard_params["threshold"].keys()

