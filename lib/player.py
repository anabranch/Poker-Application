from baseclasses.generics import Player
from cardgroups import PocketCardGroup
from chips import PlayerChips

class PokerPlayer(Player):
    """docstring for PokerPlayer"""
    def __init__(self, pk, name):
        super(PokerPlayer, self).__init__(pk,name)
        self.pocket = PocketCardGroup()
        self.stack = PlayerChips()
        
    def deal_pocket_card(self, card):
        self.pocket.add_card(card)

    def as_dict(self):
        return {
            "name":self.name,
            "pk":self.pk,
            "stack":self.stack.as_dict()
        }