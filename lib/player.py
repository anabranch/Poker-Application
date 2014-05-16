from equalitymixin import CommonEqualityMixin

class Hand(CommonEqualityMixin):
    """docstring for Hand"""
    def __init__(self, name):
        super(Hand, self).__init__()
        self.name = name
        self.is_in_game = False
    
    def pocket_cards(self, cg):
        #this will import a card group