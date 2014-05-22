from lib.player import Player
from lib.card import Card

d2 = Card(2,"Diamonds")
d3 = Card(3,"Diamonds")
da = Card(14,"Diamonds")
class TestPlayer:
    def setUp(self):
        self.p = Player(1234, "Bill")

    def test_name(self):
        assert self.p.name == "Bill"

    def test_identifier(self):
        assert self.p.identifier == 1234

    def test_pocket(self):
        self.p.dealpocket(d2)
        assert len(self.p.pocket.cards) == 1
        assert self.p.pocket.cards == [d2]
        self.p.dealpocket(da)
        assert len(self.p.pocket.cards) == 2
        assert self.p.pocket.cards == [d2, da]
