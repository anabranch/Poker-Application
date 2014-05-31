from chips import PotChips
from copy import copy

class BettingController(object):
    """docstring for BettingController"""
    def __init__(self, pokertable):
        super(BettingController, self).__init__()
        # action Controls
        self.defaultactions = ["check", "fold", "bet", "call"]

        # Static Pot Controls
        self.bigblind = 0
        self.smallblind = 0

        # Dynamic Pot Controls
        self.minraise = 0 # changes with each bet
        self.raiseplayer = None
        self.raiseposition = 0

        #pots
        self.pot = PotChips()
        self.pot.commit_players(pokertable.active_players_list())
        self.table = pokertable

    def set_blinds(self, bigblind, smallblind):
        self.bigblind = bigblind
        self.smallblind = smallblind

    def bet(self, amount):
        p = self.table.get_actor_as_player()
        pos = self.table.get_actor_as_seat()
        # this needs to be a contract that is all or nothing
        # we'll also need to do our split pot logic here
        if amount > self.pot.commitrequirement:
            self.raiseplayer = p
            self.raiseposition = pos
            self.minraise = amount

        p.stack.remove(amount)
        self.pot.add(p, amount)
        self.table.next_active_player()
        return True

    def fold(self):
        self.table.remove_by_player(self.table.get_actor_as_player())
        self.table.next_active_player()
        return True

    def call(self, amount):        
        self.bet(amount)
        self.table.next_active_player()
        return True

    def check(self):
        self.table.next_active_player()
        return True

    def commit_blinds(self):
        self.bet(self.smallblind)
        self.bet(self.bigblind)
        self.table.set_actor(self.table.smallposition)

    def get_actions(self):
        actions = copy(self.defaultactions)
        if self.raiseplayer == None:
            actions.remove("call")
            return actions
        actions.remove("check")
        return actions


    def as_dict(self):
        return {
            "big_blind_amount": self.bigblind,
            "small_blind_amount": self.smallblind,
            "min_raise": self.minraise,
            "raise_player": self.raiseplayer.as_dict(),
            "raise_position":self.raiseposition,
            "pot": self.pot.as_dict(),
            "actions":self.get_actions()
        }