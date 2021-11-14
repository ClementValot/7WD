from .Effectable import Effectable


class Wonder:
    def __init__(self):
        self.levels = []


class WonderLevel(Effectable):
    def __init__(self, effects=[]):
        super().__init__(*effects)
        self.cost = 0
