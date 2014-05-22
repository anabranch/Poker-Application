from baseclasses.statedobject import StatedObject
from cardgroups import DeckCardGroup, BoardCardGroup, BurnCardGroup
from chips import PotChips

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
        self.button = 0
        self.positions = dict([(x,None) for x in range(1,13)])
        self._deck = DeckCardGroup()
        self._board = BoardCardGroup()
        self._burn = BurnCardGroup()
        self._pot = PotChips()

    def _set_players(self, playerposdict):
        if len(playerposdict) < 2:
            TypeError("Cannot have a PokerHand with < 2 Players")

    def _set_blinds(self, buttonposition):
        # this could be a lot easier if we kept track of occupied positions
        self.button = buttonposition
        temp = buttonposition
        if len(self.players) == 2:
            while True:
                temp = temp + 1
                if self.positions[temp]:
                    self.smallblind = temp
                    self.bigblind = buttonposition
                    break
        else:
            temp = buttonposition
            while temp < 12:
                temp = temp + 1
                if self.positions[temp]:
                    self.smallblind = temp
                    break
            temp = self.smallblind
            while temp < 12:
                temp = temp + 1
                if self.positions[temp]:
                    self.bigblind = temp
                    break

        
    def pregame_check(self):
        pass

    def postgame_check(self):
        pass

    def state_change(self):
        super(PokerGame, self).state_change()


# if __name__ == '__main__':
#     p = PokerGame()
#     p.state_change()