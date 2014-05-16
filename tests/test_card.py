from lib.card import Card

class TestCard(object):
    def setUp(self):
        self.c = Card(2,"Diamond")
        self.ace = Card(14,"Diamond")

    def test_is_ace(self):
        assert self.ace.is_ace == True
        assert self.c.is_ace == False

    def test_as_tuple(self):
        assert self.ace.as_tuple() == (14, "Diamond")

    def test_string(self):
        assert str(self.c) == "2-Diamond"
        