class Game:
    def __init__(self):
        # one board
        self.board = Board()

        # two new players
        self.player1 = Player()
        self.player2 = Player()

        self.active_player = self.player1

    def switch_active_player(self):
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1
