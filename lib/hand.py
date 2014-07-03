from baseclasses.generics import StatedObject
from cardgroups import DeckCardGroup, BoardCardGroup, BurnCardGroup
from betting import BettingController
from ranker import rank_hands

class PokerHand(StatedObject):
    """
    A PokerHand is initiated by a PokerGame
    It has its own table instance as well as player group. 
    All state changes are handled by the "state_change method for consistency.
    State transitions are handled automatically by the app => see poker hand tests
    """
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
        """Controls state"""
        super(PokerHand, self).state_change()

    def assign_button_blinds(self, dealerposition):
        """Assigns buttons by deferring to the hand's table"""
        self.table.set_button(dealerposition)
        self.table.assign_blinds()

    def pregame(self, dealerposition=0, bigblind=20, smallblind=10):
        """
        All of our pregame checks and assigments,
        setting blinds
        commiting chips
        setting the actor
        """
        self.state_change() # entered pregame
        self.bet.set_blinds(bigblind, smallblind) # set blind amounts
        self.assign_button_blinds(dealerposition) # assignments
        self.deck.shuffle()
        # CURRENT ACTOR SHOULD BE SMALL BLIND
        self.bet.commit_blinds()
        self.table.set_actor(self.table.smallposition) # reset back to smallblind
        self.state_change()

    def deal_pocket(self):
        """
        deals the pocket and sets the actor
        """
        small = self.table.smallposition
        for x in range(0, len(self.table.active)*2):
            self.table.get_actor_as_player().deal_pocket_card(self.deck.pop_pocket())
            self.table.next_active_player()
        self.table.set_actor(self.table.bigposition)
        self.table.next_active_player()
        self.state_change()

    def deal_flop(self):
        """
        deals the flop and sets the actor
        """
        self.burn.burn(self.deck.pop_burn())
        self.board.add_flop(self.deck.pop_flop())
        self.reset_before_betting()
        self.state_change()

    def deal_turn(self):
        """
        deals the turn and sets the actor
        """
        self.burn.burn(self.deck.pop_burn())
        self.board.add_turn(self.deck.pop_turn())
        self.reset_before_betting()
        self.state_change()

    def deal_river(self):
        """
        deals the river and sets the actor
        """
        self.burn.burn(self.deck.pop_burn())
        self.board.add_turn(self.deck.pop_river())
        self.reset_before_betting()
        self.state_change()

    def reset_before_betting(self):
        """
        Sets the actor and gets the next active player
        makes sure that the betting state is set as well
        """
        self.table.set_actor()
        self.table.next_active_player()
        self.bet.reset_before_betting()

    def reset_after_betting(self):
        """Resets everything after betting"""
        self.state_change()
        self.bet.reset_after_betting()

    def showdown(self):
        """Showdown will determine who wins the hand, it will defer
        to the ranking algorithm in order to decide who wins"""
        ranked = rank_hands(dict([(seat, (person.pocket.cards + self.board.cards)) \
            for seat, person in self.table.active.items()]))
        # print self.bet.pot.player_commit_amounts
        print "S"*70
        print ranked
        return False

    def action(self, details):
        """
        Records what action a player takes from our front-end
        application. Determines what they can and cannot do at that 
        given time.
        """
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
        """
        Returns the status of the hand, this should be polled
        so that the clients can know what they should be doing
        """
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