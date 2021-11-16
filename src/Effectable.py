from .Effect import Effect


class Effectable:
    def __init__(self,
                 immediate_effects: [Effect] = None,
                 permanent_effects: [Effect] = None,
                 end_game_effects: [Effect] = None
                 ):
        self.immediate_effects = immediate_effects
        self.permanent_effects = permanent_effects
        self.end_game_effects = end_game_effects
