from baseclasses.generics import StatedObject
from cardgroups import DeckCardGroup, BoardCardGroup, BurnCardGroup
from betting import BettingController

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

    def action(self, details):
        action = details['action']
        seat = details['seat']
        amount = details['amount']
        success = False
        if seat != self.table.get_actor_as_seat():
            return False
        if action not in self.bet.get_actions():
            return False
        print self.bet.raiseposition
        print seat

        if action == "fold":
            if self.bet.fold():
                return True

        elif action == "call":
            if self.bet.call(amount):
                return True

        elif action == "check":
            if self.bet.check():
                return True

        elif action == "bet":
            if self.bet.bet(amount):
                return True

        return False


    def hand_status(self):
        return {
            "board":self.board.as_dict(),
            "table": self.table.as_dict(),
            "actor": self.table.get_actor_as_player().as_dict(),
            "bet_controller":self.bet.as_dict(),
            "state": self.currentstate
        }