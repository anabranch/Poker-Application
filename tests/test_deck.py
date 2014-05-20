from copy import copy

from lib.cardgroups import Deck

class TestDeck(object):
    def setUp(self):
        self.d = Deck()

    def test_length(self):
        assert len(self.d.cards) == 52

    def test_shuffle(self):
        before = self.d._local_card_copy()
        self.d.shuffle()
        after = self.d._local_card_copy()
        assert before != after
        self.d.shuffle()
        print after
        print self.d.cards
        assert after == self.d.cards

    def test_shuffle_and_state(self):
        assert self.d._state == "Unshuffled"
        assert self.d._shuffled_state() == False
        self.d.shuffle()
        assert self.d._shuffled_state() == True
        assert self.d._state == "Shuffled"