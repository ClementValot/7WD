from typing import Literal


class Player:
    def __init__(self, name: str, number: Literal[1, 2]):
        self.name: str = name
        self.number: Literal[1, 2] = number
        self.coins: int = 0

    def give_coins(self, number_of_coins: int) -> int:
        self.coins += number_of_coins
        return self.coins

    def remove_coins(self, number_of_coins: int) -> int:
        self.coins = max(self.coins - number_of_coins, 0)
        return self.coins
