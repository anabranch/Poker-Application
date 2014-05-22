from baseclasses.generics import Chips

class PlayerChips(Chips):
    """docstring for PlayerChips"""
    def __init__(self):
        super(PlayerChips, self).__init__()
    # need to implement some checks here
    def commit(self, amount):
        self._stack = self._stack - amount

    def win(self, amount):
        self._stack = self._stack + amount


class PotChips(Chips):
    """docstring for PotChips"""
    def __init__(self):
        super(PotChips, self).__init__()

    def commit(self, amount):
        self.total += amount
