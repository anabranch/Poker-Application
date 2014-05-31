from chips import PotChips

class PotController(object):
    """docstring for PotController"""
    def __init__(self):
        super(PotController, self).__init__()
        self.main = PotChips()
        self.pots = []