from baseclasses.generics import Player
from cardgroups import PocketCardGroup
from chips import PlayerChips

class PokerPlayer(Player):
    """docstring for PokerPlayer"""
    def __init__(self):
        super(PokerPlayer, self).__init__()
        self.pocket = PocketCardGroup()
        self.stack = PlayerChips()
        
    def deal_pocket_card(self, card):
        self.pocket.add_card(card)

    def buyin(self, amount):
        pass