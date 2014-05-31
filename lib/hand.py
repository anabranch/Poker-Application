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
        self.bettingstates = [
            "riverbetting",
            "turnbetting",
            "flopbetting",
            "preflopbetting"
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

    def reset_after_betting(self):
        self.state_change()
        self.bet.reset_after_betting()
        self.table.set_actor()
        self.table.next_active_player()

    def action(self, details):
        if self.currentstate not in self.bettingstates:
            return False

        action = details['action']
        seat = details['seat']
        amount = details['amount']
        success = False
        if seat != self.table.get_actor_as_seat():
            return success
        if action not in self.bet.get_actions():
            return success

        if action == "fold":
            if self.bet.fold():
                success = True

        elif action == "call":
            if self.bet.call(amount):
                success = True

        elif action == "check":
            if self.bet.check():
                success = True

        elif action == "bet":
            if self.bet.bet(amount):
                success = True

        if self.table.get_actor_as_seat() == self.bet.raiseposition:
            self.reset_after_betting()

        # if no one in the game, go to showdown
        return success


    def hand_status(self):
        if self.currentstate not in self.bettingstates:
            return {
                "board":self.board.as_dict(),
                "table": self.table.as_dict(),
                "actor": None,
                "bet":self.bet.as_dict(False),
                "state": self.currentstate
            }
        return {
            "board":self.board.as_dict(),
            "table": self.table.as_dict(),
            "actor": self.table.get_actor_as_player().as_dict(),
            "bet":self.bet.as_dict(),
            "state": self.currentstate
        }