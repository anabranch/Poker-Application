from baseclasses.generics import StatedObject
from cardgroups import DeckCardGroup, BoardCardGroup, BurnCardGroup

class PokerHand(StatedObject):
    """docstring for PokerHand"""
    def __init__(self, pokertable, bettingcontrol):
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
        self.bet = bettingcontrol

        # Table
        self.table = pokertable

    def hand_status(self):
        return {
            "board":self.board.as_json(),
            "pot": self.pot.as_json(),
            "table": self.table.as_json(),
            "actor": {
                "player":self.table.get_actor_as_player().to_json(),
                "actions":self.bettingcontrol.to_json()
            },
            "state": self.currentstate
        }



