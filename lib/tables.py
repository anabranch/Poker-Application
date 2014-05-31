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






if __name__ == '__main__':
    def debug():
        # print t.positions
        # print t.occupiedseats
        print t.dealerposition
        print t.smallposition
        print t.bigposition
        print t.currentactor
    t = PokerHandTable()
    t.sit(2,"x")
    t.sit(3,"u")
    t.sit(4,"q")
    t.sit(9,"y")
    t.set_button(2)
    t.deactivate_seat(3)
    t.assign_blinds()
    debug()