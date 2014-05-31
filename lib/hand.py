from baseclasses.generics import StatedObject
from cardgroups import DeckCardGroup, BoardCardGroup, BurnCardGroup
from chips import PotChips
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

        # action Controls
        self.defaultactions = ["check", "fold", "bet", "call"]
        self.currentactions = []

        # Static Pot Controls
        self.bigblind = 0
        self.smallblind = 0

        # Dynamic Pot Controls
        self.minbet = 0 # changes with each bet
        self.callamount = 0

        #Pots
        # there needs to be a pot manager to see if we need to split a pot or something, just not there yet
        self.mainpot = PotChips()
        self.sides = []

        # Table
        self.table = pokertable

    def state_change(self):
        super(PokerHand, self).state_change()

    def set_blinds(self,bigblind, smallblind):
        self.bigblind = bigblind
        self.smallblind = smallblind
        self.minbet = bigblind
        self.callamount = bigblind

    def assign_buttons_and_blind(self, dealerposition):
        self.table.set_button(dealerposition)
        self.table.assign_blinds()

    def bet(self, amount):
        # try:
            self.table.get_actor_as_player().stack.remove(amount)
            self.minbet = amount*2
            self.callamount = self.callamount = amount
            self.table.next_active_player()
        # except ValueError:
        #     print self.currentstate
                

    def pregame(self, dealerposition=0, bigblind=20, smallblind=10):
        self.state_change() # entered pregame
        self.set_blinds(bigblind, smallblind) # set blind amounts
        self.assign_buttons_and_blind(dealerposition) # assignments
        self.deck.shuffle()
        # CURRENT ACTOR SHOULD BE SMALL BLIND
        self.bet(smallblind)
        self.bet(bigblind)
        self.minbet = bigblind # override bet amount
        self.table.set_actor(self.table.smallposition) # reset back to smallblind
        self.state_change()

    def add_to_pot(self, amount):
        pass

    def deal_pocket(self):
        small = self.table.smallposition
        for x in range(0, len(self.table.active)*2):
            self.table.get_actor_as_player().deal_pocket_card(self.deck.pop_pocket())
            self.table.next_active_player()
        self.table.set_actor(self.table.bigposition)
        self.table.next_active_player()
        self.currentactions = copy(self.defaultactions)
        self.currentactions.remove("check")
        self.state_change()

    def action(self, details):
        actiontype = details['type']
        seat = details['seat']
        amount = details['amount']
        success = False
        #first check that it's the current actors turn
        if seat != self.table.get_actor_as_seat():
            return False
        
        if actiontype == 'fold':
            self.table.remove_by_seat(seat)
            success = True
        elif actiontype == 'call':
            pass
        elif actiontype == 'bet':
            self.bet(amount)
            success = True #need to make sure we're not pulling too much
        elif actiontype == "check":
            pass

        if success:
            self.table.next_active_player()
            return True
        return False


    def hand_status(self):
        return {
            "board":self.board.as_dict(),
            "table": self.table.as_dict(),
            "actor": self.table.get_actor_as_player().as_dict(),
            "actions": self.currentactions,
            "min_bet":self.minbet,
            "call_amount": self.callamount,
            "main_pot": self.mainpot.as_dict(),
            "side_pots": self.sides,
            "table":self.table.as_dict(),
            "state": self.currentstate
        }