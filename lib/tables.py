from random import choice

from baseclasses.generics import StatedObject

class Table(StatedObject):
    """docstring for Table"""
    def __init__(self):
        super(Table, self).__init__()
        self.states = ["game"]
        self.positions = dict([(x,None) for x in range(1,13)])
        self.occupiedseats = []
        self.activeseats = []
        self.dealerposition = 0
        self.currentposition = 0

    def sit(self, seatnumber, player):
        if not self.positions[seatnumber]:
            self.positions[seatnumber] = player
            self.occupiedseats.append(seatnumber)
            self.activate_seat(seatnumber)

    def getup(self, seatnumber):
        self.positions[seatnumber] = None
        self.occupiedseats.remove(seatnumber)
        self.deactivate_seat(seatnumber)

    def activate_seat(self, seatnumber):
        if self.currentstate != "game":
            self.activeseats.append(seatnumber)

    def deactivate_seat(self, seatnumber):
        self.activeseats.remove(seatnumber)

    def set_position_to_dealer(self):
        self.currentposition = self.dealerposition

    def next_active_seat(self, position=0):
        if len(self.activeseats) == 0 or self.dealerposition == 0:
            return # verified that there are people at the table

        if not self.currentposition: #no previous position
            self.currentposition = self.dealerposition
            if self.currentposition in self.activeseats:
                return self.currentposition
        
        if not position:
            position = self.currentposition

        if position == 12:
            position = 0

        position += 1
        while True:
            if position in self.activeseats:
                self.currentposition = position
                return self.currentposition
            else:
                position += 1
                if position == 12:
                    position = 0


    def set_button(self, button=0):
        if not button:
            self.dealerposition = choice(self.positions.keys())
        else:
            if button in self.activeseats:
                self.dealerposition = button
                self.set_position_to_dealer()


class PokerHandTable(Table):
    """docstring for PokerHandTable"""
    def __init__(self):
        super(PokerHandTable, self).__init__()
        self.smallposition = 0
        self.bigposition = 0

    def assign_blinds(self):
        self.smallposition = self.next_active_seat()
        self.bigposition = self.next_active_seat()        
        self.set_position_to_dealer()

if __name__ == '__main__':
    def debug():
        # print t.positions
        # print t.occupiedseats
        print t.dealerposition
        print t.smallposition
        print t.bigposition
        print t.currentposition
    t = PokerHandTable()
    t.sit(2,"x")
    t.sit(3,"u")
    t.sit(4,"q")
    t.sit(9,"y")
    t.set_button(2)
    t.deactivate_seat(3)
    t.assign_blinds()
    debug()