from lib.hand import PokerHand
from lib.player import Player

p1 = Player(1234, "Bill")
p2 = Player(123, "Bill")
p3 = Player(1323, "Bill")
p4 = Player(1243, "Bill")
p5 = Player(1213, "Bill")

class TestPokerHand:
    def setUp(self):
        self.g = PokerHand()



