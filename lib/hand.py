from baseclasses.generics import StatedObject
from cardgroups import DeckCardGroup, BoardCardGroup, BurnCardGroup
from betting import BettingController
from copy import copy

class PokerHand(StatedObject):
    """docstring for PokerHand"""
    def __init__(self, handid, pokertable):
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

        self.pk = handid

        # Cards
        self.deck = DeckCardGroup()
        self.board = BoardCardGroup()
        self.burn = BurnCardGroup()

        # Table
        self.table = pokertable

        self.bet = BettingController(pokertable)

    def state_change(self):
        super(PokerHand, self).state_change()

    def assign_button_blinds(self, dealerposition):
        self.table.set_button(dealerposition)
        self.table.assign_blinds()

    def pregame(self, dealerposition=0, bigblind=20, smallblind=10):
        self.state_change() # entered pregame
        self.bet.set_blinds(bigblind, smallblind) # set blind amounts
        self.assign_button_blinds(dealerposition) # assignments
        self.deck.shuffle()
        # CURRENT ACTOR SHOULD BE SMALL BLIND
        self.bet.commit_blinds()
        self.table.set_actor(self.table.smallposition) # reset back to smallblind
        self.state_change()

    def deal_pocket(self):
        small = self.table.smallposition
        for x in range(0, len(self.table.active)*2):
            self.table.get_actor_as_player().deal_pocket_card(self.deck.pop_pocket())
            self.table.next_active_player()
        self.table.set_actor(self.table.bigposition)
        self.table.next_active_player()
        self.state_change()

    # def action(self, details):
    #     actiontype = details['type']
    #     seat = details['seat']
    #     amount = details['amount']
    #     success = False
    #     #first check that it's the current actors turn
    #     if seat != self.table.get_actor_as_seat():
    #         return False
        
    #     if actiontype == 'fold':
    #         self.table.remove_by_seat(seat)
    #         success = True
    #     elif actiontype == 'call':
    #         pass
    #     elif actiontype == 'bet':
    #         self.bet(amount)
    #         success = True #need to make sure we're not pulling too much
    #     elif actiontype == "check":
    #         pass

    #     if success:
    #         self.table.next_active_player()
    #         return True
    #     return False


    def hand_status(self):
        return {
            "board":self.board.as_dict(),
            "table": self.table.as_dict(),
            "actor": self.table.get_actor_as_player().as_dict(),
            "bet_controller":self.bet.as_dict(),
            "state": self.currentstate
        }