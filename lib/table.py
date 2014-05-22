from player import Player

class Table(object):
    """docstring for Table"""
    def __init__(self):
        super(Table, self).__init__()
        self.positions = dict([(x,None) for x in range(0,13)])

    def sit_player(self, seat_number, player):
        self.positions[seat_number] = player
