from baseclasses.generics import Table


class PokerHandTable(Table):
    """docstring for PokerHandTable"""
    def __init__(self):
        super(PokerHandTable, self).__init__()
        self.smallposition = 0
        self.bigposition = 0

    def assign_blinds(self):
        self.smallposition = self.next_active_seat()
        self.bigposition = self.next_active_seat()
        self.set_actor(self.smallposition)

    def as_dict(self):
        return {
            "small": self.smallposition,
            "big": self.bigposition,
            "button": self.dealerposition,
            "current_actor": self.currentactor,
            "active_players": [(s, p.as_dict()) for s, p in self.active.items()]
        }
