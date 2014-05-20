from baseclasses.statedobject import StatedObject
from cardgroups import DeckCardGroup, BoardCardGroup, BurnCardGroup
from chips import PotChips

class PokerGame(StatedObject):
    """docstring for PokerGame"""
    def __init__(self):
        super(PokerGame, self).__init__()
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

        self._players = {} # id, player_instance
        # all these card groups should have the same state so we can advance them together
        self._deck = DeckCardGroup()
        self._board = BoardCardGroup()
        self._burn = BurnCardGroup()
        self._pot = PotChips()

        # should have no concept of the current table, it should just get it's own table
        # so people can sit and get up without affecting the game
        
    def pregame(self):
        pass

    def state_change(self):
        super(PokerGame, self).state_change()


# if __name__ == '__main__':
#     p = PokerGame()
#     p.state_change()