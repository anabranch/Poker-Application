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

    def reset_before_betting(self):
        self.minraise = self.bigblind
        self.raiseplayer = self.table.get_actor_as_player()
        self.raiseposition = self.table.get_actor_as_seat()

    def reset_after_betting(self):
        self.minraise = self.bigblind
        self.raiseplayer = None
        self.raiseposition = 0
        self.pot.commitrequirement = 0

    def get_bet_delta(self):
        temp = self.pot.commitrequirement - \
        self.pot.player_commit_amounts[self.table.get_actor_as_player()]
        if temp < 0:
            temp = 0
        # work
        return temp

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
        # need to enforce some amount thing here....
        self.bet(amount)
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
        if self.pot.commitrequirement == 0:
            actions.remove("call")
        elif self.pot.commitrequirement != 0:
            actions.remove("check")
        return actions


    def as_dict(self, betting_state=True):
        if betting_state:
            return {
                "big_blind_amount": self.bigblind,
                "small_blind_amount": self.smallblind,
                "min_raise": self.minraise,
                "raise_player": self.raiseplayer.as_dict(),
                "raise_position":self.raiseposition,
                "pot": self.pot.as_dict(),
                "bet_delta": self.get_bet_delta(),
                "actions":self.get_actions()
            }
        return {
            "big_blind_amount": self.bigblind,
            "small_blind_amount": self.smallblind,
            "min_raise": self.minraise,
            "raise_player": {},
            "raise_position": self.raiseposition,
            "pot": self.pot.as_dict(),
            "bet_delta": self.get_bet_delta(),
            "actions":[]
        }