from baseclasses.statedobject import StatedObject
from cardgroups import DeckCardGroup, BoardCardGroup, BurnCardGroup

class PokerGame(StatedObject):
    """docstring for PokerGame"""
    def __init__(self):
        super(PokerGame, self).__init__()
        # pregame, dealing pocket, dealing, etc
        self.state = "pregame"
        self.players = []
        # all these card groups should have the same state so we can advance them together
        self.deck = DeckCardGroup()
        self.board = BoardCardGroup()
        self.burn = BurnCardGroup)()

        # should have no concept of the current table, it should just get it's own table
        # so people can sit and get up without affecting the game
        
    def pre_game(self):
        pass