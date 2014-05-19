from copy import copy

from lib.deck import Deck

class TestDeck(object):
    def setUp(self):
        self.d = Deck()

    def test_length(self):
        assert len(self.d.cards) == 52

    def test_shuffle(self):
        before = self.d._local_card_copy()
        self.d._shuffle()
        after = self.d._local_card_copy()
        assert before != after
        self.d._shuffle()
        print after
        print self.d.cards
        assert after == self.d.cards