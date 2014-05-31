from baseclasses.generics import Table
from random import choice

class PokerHandTable(Table):
    """docstring for PokerHandTable"""
    def __init__(self):
        super(PokerHandTable, self).__init__()
        self.smallposition = 0
        self.bigposition = 0

    def assign_blinds(self):
        self.smallposition = self.next_active_seat()
        self.bigposition = self.next_active_seat()        
        self.set_actor_to_dealer()