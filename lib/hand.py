from baseclasses.generics import StatedObject
from cardgroups import DeckCardGroup, BoardCardGroup, BurnCardGroup
from pots import PotController
from random import choice

class PokerHand(StatedObject):
    """docstring for PokerHand"""
    def __init__(self):
        super(PokerHand, self).__init__()
        self.states = [
            "postgame",
            "showdown",
            "riverbetting",
            "dealriver",
            "turnbetting",
            "dealturn",
            "flopbetting",
            "dealflop",
            "preflopbetting",
            "dealpocket",
            "pregame"
        ]
        # Blind Information
        self.bigblind = 0
        self.smallblind = 0

        # Cards
        self.deck = DeckCardGroup()
        self.board = BoardCardGroup()
        self.burn = BurnCardGroup()

        # Pot Controller
        self.pot = PotController()

    def set_blinds(self, bigblind=20, smallblind=10):
        self.bigblind = bigblind
        self.smallblind = smallblind
        

    def betting_round(self):
        pass

    def state_change(self):
        super(PokerGame, self).state_change()
