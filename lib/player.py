from baseclasses.generics import Player
from cardgroups import PocketCardGroup
from chips import PlayerChips


# think this will need to be split into hand and game player


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
            "stack":self.stack.as_dict(),
            "pocket": self.pocket.as_dict()
        }