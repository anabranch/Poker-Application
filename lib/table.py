from baseclasses.generics import Table

class PokerHandTable(Table):
    """The PokerHandTable is basically a reflection of who is
    playing in the game and what their "role" in the game is 
    (big blind, dealer, small blind, etc)
    The PokerHandTable tells us who is active in the hand, who
    is currently acting and who is next up to bet. It is naive of 
    all betting information. It basically is responsible for managing
    the players in the hand."""
    def __init__(self):
        super(PokerHandTable, self).__init__()
        self.smallposition = 0
        self.bigposition = 0

    def assign_blinds(self):
        """Assigns the blinds to the active players"""
        self.smallposition = self.next_active_seat()
        self.bigposition = self.next_active_seat()
        self.set_actor(self.smallposition)

    def as_dict(self):
        """Returns relevant information as a dictionary"""
        return {
            "small": self.smallposition,
            "big": self.bigposition,
            "button": self.dealerposition,
            "current_actor": self.currentactor,
            "active_players": dict([(s, p.as_dict()) for s, p in self.active.items()])
        }
