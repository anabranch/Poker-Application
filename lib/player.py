from baseclasses.generics import Card
from cardgroups import PocketCardGroup
from chips import PlayerChips

class Player(object):
    """docstring for Player"""
    def __init__(self, uniqueid=0, name=None):
        super(Player, self).__init__()
        # States are Initiated, dealing cards, in_game
        self.name = name
        self.uniqueid = uniqueid
        self.pocket = PocketCardGroup()
        self.stack = PlayerChips()

    def __str__(self):
        return "%i -- %s" % (self.uniqueid, self.name)

    def __repr__(self):
        return str(self)

    def deal_pocket_card(self, card):
        self.pocket.add_card(card)

    def buyin(self, amount):
        pass
        