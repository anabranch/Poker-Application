from baseclasses.generics import StatedObject
from cardgroups import DeckCardGroup, BoardCardGroup, BurnCardGroup
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
        self.buttonposition = 0
        self.bigposition = 0
        self.smallposition = 0

        # Players/Seats
        self.positions = dict([(x,None) for x in range(1,13)])
        self.players = {}

        # Cards
        self.deck = DeckCardGroup()
        self.board = BoardCardGroup()
        self.burn = BurnCardGroup()

    def get_small_blind_player(self):
        return self.get_player_from_position(self.smallposition)

    def get_big_blind_player(self):
        return self.get_player_from_position(self.bigposition)

    def get_button_player(self):
        return self.get_player_from_position(self.buttonposition)

    def get_position_from_player(self, player):
        return self.players[player]

    def get_player_from_position(self, position):
        return self.positions[position]

    def set_players(self, playerposdict):
        if len([player for pos, player in playerposdict.items() if player != None]) < 2:
            raise ValueError("Cannot have a PokerHand with < 2 Players")
        for pos, player in playerposdict.items():
            if player:
                self.players[player] = pos
                self.positions[pos] = player

    def set_blinds(self, bigblind=20, smallblind=10):
        self.bigblind = bigblind
        self.smallblind = smallblind
        
    def _blind_assignment(self, buttonposition=0):
        # this could be a lot easier if we kept track of occupied positions
        if not buttonposition:
            buttonposition = choice(self.players.values())
        self.buttonposition = buttonposition
        temp = buttonposition
        # this can be optimized a ton, interate through keys of active players
        if len(self.players) == 2:
            while True:
                if temp >= 12:
                    temp = 0
                temp = temp + 1
                if self.positions[temp]:
                    self.smallposition = temp
                    self.bigposition = buttonposition
                    break
        else:
            temp = buttonposition
            while temp < 12:
                if temp >= 12:
                    temp = 0
                temp = temp + 1
                if self.positions[temp]:
                    self.smallposition = temp
                    break
            temp = self.smallposition
            while temp < 12:
                if temp >= 12:
                    temp = 0
                temp = temp + 1
                if self.positions[temp]:
                    self.bigposition = temp
                    break

    def betting_round(self):
        pass

    def state_change(self):
        super(PokerGame, self).state_change()
