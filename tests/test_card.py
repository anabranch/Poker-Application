from lib.card import Card

class TestCard(object):
    def setUp(self):
        self.d2 = Card(2,"Diamonds")
        self.da = Card(14,"Diamonds")

    def test_is_ace(self):
        assert self.da.is_ace == True
        assert self.d2.is_ace == False