from copy import copy

from lib.baseclasses.generics import Card
from lib.cardgroups import DeckCardGroup, ValuedCardGroup, PocketCardGroup, BoardCardGroup, BurnCardGroup

d2 = Card(2,"Diamonds")
da = Card(14,"Diamonds")
sa = Card(14,"Spades")
d13 = Card(13,"Diamonds")
s10 = Card(10,"Spades")
s11 = Card(11,"Spades")
s12 = Card(12,"Spades")
s13 = Card(13,"Spades")
s14 = Card(14,"Spades")
c13 = Card(13,"Clubs")
h13 = Card(13, "Hearts")
d12 = Card(12,"Diamonds")

class TestDeck:
    def setUp(self):
        self.d = DeckCardGroup()

    def test_length(self):
        print self.d.cards
        assert len(self.d) == 52

    def test_pop_card(self):
        c = self.d._pop_card()
        print c
        assert s14 == c
        assert len(self.d) == 51

    def test_pop_burn(self):
        c = self.d._pop_card()
        print c
        assert s14 == c
        assert len(self.d) == 51

    def test_pop_flop(self):
        c = self.d.pop_flop()
        assert len(c) == 3
        assert s14 in c
        assert s13 in c
        assert s12 in c
        assert len(self.d) == 49

    def test_pop_turn(self):
        c = self.d.pop_turn()
        assert s14 == c
        assert len(self.d) == 51

    def test_pop_river(self):
        c = self.d.pop_river()
        assert s14 == c
        assert len(self.d) == 51

    def test_too_many_cards(self):
        try:
            self.d.add_card(s14)
            assert False
        except ValueError:
            assert True

    def test_shuffles(self):
        x = self.d.local_card_copy()
        self.d.shuffle()
        assert x[0] != self.d.cards[0]


class TestBoardCardGroup:
    def setUp(self):
        self.b = BoardCardGroup()

    def test_add_flop(self):
        cs = [s12,s13,s14]
        self.b.add_flop(cs)
        assert len(self.b) == 3

    def test_add_turn(self):
        cs = s14
        self.b.add_turn(cs)
        assert len(self.b) == 1

    def test_add_river(self):
        cs = s14
        self.b.add_river(cs)
        assert len(self.b) == 1
        
    def test_too_many(self):
        cs = [s12,s13,s14]
        self.b.add_flop(cs)
        self.b.add_turn(s11)
        self.b.add_river(s10)
        try:
            self.b.add_card(da)
            assert False
        except ValueError:
            assert True

class TestBurnCardGroup:
    def setUp(self):
        self.b = BurnCardGroup()

    def test_burn(self):
        self.b.burn(s14)
        assert len(self.b) == 1    

class TestPocketCardGroup:
    def setUp(self):
        self.p = PocketCardGroup()

    def test_add_card(self):
        self.p.add_card(s14)
        assert len(self.p) == 1
        self.p.add_card(d2)
        assert len(self.p) == 2

    def test_too_many(self):
        self.p.add_card(s14)
        assert len(self.p) == 1
        self.p.add_card(d2)
        assert len(self.p) == 2
        try:
            self.p.add_card(da)
            assert False
        except ValueError:
            assert True

class TestAddition:
    def setUp(self):
        self.p = PocketCardGroup()
        self.p.add_card(d2)
        self.p.add_card(da)
        self.b = BoardCardGroup()
        self.b.add_card(s13)
        self.b.add_card(d13)
        self.b.add_card(h13)
        self.b.add_card(c13)

    def test_addition(self):
        assert [d2,da,s13,d13,h13, c13] == self.p + self.b

    def test_addition_2(self):
        vals = ValuedCardGroup(self.p + self.b).best_hand()
        hand = vals['hand']
        kickers = vals['kickers']
        assert s13 in hand
        assert d13 in hand
        assert h13 in hand
        assert c13 in hand
        assert da in kickers
