from lib.tables import PokerHandTable

class TestPokerHand:
    def setUp(self):
        self.table = PokerHandTable()
        self.table.sit(2, "x")

    def test_sit(self):
        assert len(self.table.activeplayers) == 1
        assert len(self.table.occupiedseats) == 1
        assert len(self.table.activeseats) == 1

    def test_getup(self):
        self.table.getup(2)
        assert len(self.table.activeplayers) == 0
        assert len(self.table.occupiedseats) == 0
        assert len(self.table.activeseats) == 0


    # t = PokerHandTable()
    # t.sit(2,"x")
    # t.sit(3,"u")
    # t.sit(4,"q")
    # t.sit(9,"y")
    # t.set_button(2)
    # t.deactivate_seat(3)
    # t.assign_blinds()