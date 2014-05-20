class PlayerChips(object):
    """docstring for PlayerChips"""
    def __init__(self):
        super(PlayerChips, self).__init__()
        self._stack = 0
    # need to implement some checks here
    def commit(self, amount):
        self._stack = self._stack - amount

    def win(self, amount):
        self._stack = self._stack + amount


class PotChips(object):
    """docstring for PotChips"""
    def __init__(self):
        super(PotChips, self).__init__()
        self._total = 0

    def commit(self, amount):
        self.total += amount
