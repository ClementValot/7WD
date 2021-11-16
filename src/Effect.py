from .Player import Player
from .Board import Board


class Effect:
    def __init__(self, effect_as_str: str):
        self.effectAsString: str = effect_as_str

    def apply_effect(self, active_player: Player, board: Board):
        return

