from baseclasses.generics import StatedObject
from cardgroups import DeckCardGroup, BoardCardGroup, BurnCardGroup
from pots import PotController
from tables import PokerHandTable


class PokerHand(StatedObject):
    """docstring for PokerHand"""
    def __init__(self, pokertable):
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

        # Cards
        self.deck = DeckCardGroup()
        self.board = BoardCardGroup()
        self.burn = BurnCardGroup()

        # Pot Controller
        self.pot = PotController()

        # Table
        self.table = pokertable

    def hand_status(self):
        return {
            "board":self.board.as_json(),
            "pot": self.pot.as_json(),
            "table": self.table.as_json(),
            "state": self.currentstate
        }

    # def preflop(self):



