from copy import copy

from lib.card import Card
from lib.cardgroups import DeckCardGroup, ValuedCardGroup, PocketCardGroup, BoardCardGroup

d2 = Card(2,"Diamonds")
da = Card(14,"Diamonds")
sa = Card(14,"Spades")
s13 = Card(13,"Spades")
d13 = Card(13,"Diamonds")
c13 = Card(13,"Clubs")
h13 = Card(13, "Hearts")
d12 = Card(12,"Diamonds")

class TestDeck:
    def setUp(self):
        self.d = DeckCardGroup()

    def test_length(self):
        assert len(self.d.cards) == 52

    def test_shuffle(self):
        before = self.d.local_card_copy()
        self.d.shuffle()
        after = self.d.local_card_copy()
        assert before != after
        self.d.shuffle()
        print after
        print self.d.cards
        assert after == self.d.cards

    def test_shuffle_and_state(self):
        assert self.d.state == "unshuffled"
        self.d.shuffle()
        assert self.d.state == "shuffled"

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