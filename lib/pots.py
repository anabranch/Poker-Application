from chips import PotChips

class BettingController(object):
    """docstring for BettingController"""
    def __init__(self):
        super(BettingController, self).__init__()
        self.main = PotChips()
        self.minbet = 0
        self.pots = []

    def set_min_bet(self, amount):
        self.minbet = amount
        
    def action(self, details):
        actiontype = details['type']
        amount = details['amount']