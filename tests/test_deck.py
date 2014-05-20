from copy import copy

from lib.cardgroups import DeckCardGroup

class TestDeck(object):
    def setUp(self):
        self.d = DeckCardGroup()

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
        assert self.d.state == "Unshuffled"
        self.d.shuffle()
        assert self.d.state == "Shuffled"