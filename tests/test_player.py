from lib.player import Player
from lib.baseclasses.generics import Card

d2 = Card(2,"Diamonds")
d3 = Card(3,"Diamonds")
da = Card(14,"Diamonds")
class TestPlayer:
    def setUp(self):
        self.p = Player(1234, "Bill")

    def test_name(self):
        assert self.p.name == "Bill"

    def test_uniqueid(self):
        assert self.p.uniqueid == 1234

    def test_pocket(self):
        self.p.deal_pocket_card(d2)
        assert len(self.p.pocket.cards) == 1
        assert self.p.pocket.cards == [d2]
        self.p.deal_pocket_card(da)
        assert len(self.p.pocket.cards) == 2
        assert self.p.pocket.cards == [d2, da]
