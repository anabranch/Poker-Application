from chips import PotChips

class BettingController(object):
    """docstring for BettingController"""
    def __init__(self, pokertable):
        super(BettingController, self).__init__()
        self.table = pokertable
        # action Controls
        self.defaultactions = ["check", "fold", "bet", "call"]
        self.currentactions = []

        # Static Pot Controls
        self.bigblind = 0
        self.smallblind = 0

        # Dynamic Pot Controls
        self.minraise = 0 # changes with each bet
        self.bettor = None

        #pots
        self.mainpot = PotChips()


    def set_blinds(self, bigblind, smallblind):
        self.bigblind = bigblind
        self.smallblind = smallblind

    def commit_to_pot(self, amount):
        p = self.table.get_actor_as_player()
        # this needs to be a contract that is all or nothing
        # we'll also need to do our split pot logic here
        p.stack.remove(amount)
        self.mainpot.add(amount)
        self.bettor = p
        self.minraise = amount
        self.table.next_active_player()

    def commit_blinds(self):
        self.commit_to_pot(self.smallblind)
        self.commit_to_pot(self.bigblind)
        self.table.set_actor(self.table.smallposition)


    def as_dict(self):
        return {
            "big_blind_amount": self.bigblind,
            "small_blind_amount": self.smallblind,
            "min_raise": self.minraise,
            "bettor": self.bettor.as_dict(),
            "pot": self.mainpot.as_dict()
        }