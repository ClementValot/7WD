from .Effectable import Effectable


class Card(Effectable):
    def __init__(self, name, cost=None, effects=[], picture=None):
        super().__init__(*effects)
        self.name = name
        self.picture = picture
        self.cost = cost
