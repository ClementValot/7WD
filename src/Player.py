class Player:
    def __init__(self, name:str):
        self.name: str = name
        self.coins: int = 0

    def coins(self):
        return self.coins

    def give_coins(self, number_of_coins: int) -> int:
        self.coins += number_of_coins
        return self.coins

    def remove_coins(self, number_of_coins: int) -> int:
        self.coins = max(self.coins - number_of_coins, 0)
        return self.coins
