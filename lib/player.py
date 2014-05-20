from card import Card
from cardgroups import PocketCardGroup

class Player(object):
    """docstring for Player"""
    def __init__(self):
        super(Player, self).__init__()
        # States are Initiated, dealing cards, in_game
        # and more
        self.state = "Initiated"
        self._id = 1
        self.pocket = PocketCardGroup()
        