from baseclasses.statedobject import StatedObject

class Table(StatedObject):
    """docstring for Table"""
    def __init__(self):
        super(Table, self).__init__()
        self.state = [
            "game",
            "pregame"
        ]
        self.positions = dict([(x,None) for x in range(0,13)])

    def seat_player(self, seat_number, player):
        self.positions[seat_number] = player