from lib.baseclasses.generics import Card

class TestCard(object):
    def setUp(self):
        self.d2 = Card(2,"Diamonds")
        self.da = Card(14,"Diamonds")

    def test_is_ace(self):
        assert self.da.is_ace == True
        assert self.d2.is_ace == False

    def test_as_tuple(self):
        assert (2,0,"Diamonds") == self.d2.as_tuple()

    def test_as_dict(self):
        assert {"number":2,"suit_rank":0,"suit":"Diamonds"} == self.d2.as_dict()

    def test_wrong_number(self):
        try:
            Card(15, "Spades")
            assert False
        except TypeError:
            assert True

    def test_wrong_suit(self):
        try:
            Card(13, "sdf")
            assert False
        except TypeError:
            assert True