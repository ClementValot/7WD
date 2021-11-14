class Effectable:
    def __init__(self, immediate_effects=None, permanent_effects=None, end_game_effects=None):
        self.immediate_effects = immediate_effects
        self.permanent_effects = permanent_effects
        self.end_game_effects = end_game_effects
