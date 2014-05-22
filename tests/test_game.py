from lib.hand import PokerHand

class TestPokerHand:
    def setUp(self):
        self.g = PokerHand()

    def test_position_count(self):
        print self.g.positions
        print len(self.g.positions)
        assert len(self.g.positions) == 12