from lib.tables import PokerHandTable

class TestPokerHand:
    def setUp(self):
        self.table = PokerHandTable()
        self.table.sit(2, "x")

    def test_sit(self):
        assert len(self.table.active) == 1
        assert len(self.table.passive) == 1

    def test_getup(self):
        self.table.getup(2)
        assert len(self.table.active) == 0
        assert len(self.table.passive) == 0