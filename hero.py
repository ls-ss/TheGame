from Player import Player

class Hero(Player):

    def __init__(self, name):

        super().__init__(self)


    @property
    def attack_power(self) -> int:
        return self._attack

    @property
    def place(self):
        return self._place
