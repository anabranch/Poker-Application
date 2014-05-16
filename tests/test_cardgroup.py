from lib.card import Card
from lib.cardgroup import CardGroup
from lib.deck import Deck
from random import sample

class TestCardGroup(object):
    def setUp(self):
        # # Straight flush with ace
        self.g1_raw = [Card(c, "Diamonds") for c in range(2,6)]
        self.g1_raw.append(Card(14,"Diamonds"))
        self.g1_raw.append(Card(14, "Clubs"))
        self.g1_raw.append(Card(14, "Hearts"))
        self.g1 = CardGroup(self.g1_raw)

        # Straight flush no ace
        self.g2_raw = [Card(c, "Spades") for c in range(2,7)]
        self.g2_raw.append(Card(5, "Diamonds"))
        self.g2_raw.append(Card(10, "Clubs"))
        self.g2 = CardGroup(self.g2_raw)
        # straight
        self.g3_raw = [Card(2, "Diamonds"), 
            Card(4, "Spades"), 
            Card(3, "Hearts"), 
            Card(6, "Clubs"), 
            Card(5, "Diamonds"), 
            Card(5, "Clubs"), 
            Card(2, "Clubs")]
        self.g3 = CardGroup(self.g3_raw)

    def test_copying(self):
        n = False
        for x, y, z in zip(self.g3_raw, self.g3._cards, self.g3.cards()):
            print id(x), id(y), id(z)
            if id(x) == id(y) or id(y) == id(z) or id(x) == id(z):
                n = True

        assert n == False

    def test_length(self):
        print self.g3_raw
        print self.g3._cards
        print self.g3.cards()
        assert len(self.g3_raw) == len(self.g3.cards())

    def test_add_card(self):
        c = Card(7, "Clubs")
        self.g1_raw.append(c)
        self.g1.add_card(c)
        print self.g1
        print self.g1_raw
        for x, y in zip(self.g1_raw, self.g1.cards()):
            assert x == y

    def test_get_card(self):
        assert Card(14,"Diamonds") == self.g1.get_card(14,"Diamonds")

    def test_g1_is_straight(self):
        assert self.g1.is_straight() == True
        assert self.g1.straight_details() == Card(5, "Diamonds")
    
    # def test_g2_is_straight(self):
    #     assert self.g2.is_straight() == True
    #     assert self.g2.straight_details() == Card(6, "Spades")

    # def test_g3_is_straight(self):
    #     assert self.g3.is_straight() == True
    #     assert self.g3.straight_details() == Card(6, "Clubs")

    def test_g1_is_flush(self):
        assert self.g1.is_flush() == True
        assert self.g1.flush_details() == Card(14, "Diamonds")

    def test_g2_is_flush(self):
        assert self.g2.is_flush() == True
        assert self.g2.flush_details() == Card(6, "Spades")

    def test_g3_is_flush(self):
        assert self.g3.is_flush() == False
        
    # # def test_is_g1_straight_flush(self):
    # #     assert self.g1.is_straight_flush() == True
    # #     assert self.g1.straight_flush_details() == Card(5, "Diamonds")

    # # def test_is_g2_straight_flush(self):
    # #     assert self.g2.is_straight_flush() == True
    # #     assert self.g2.straight_flush_details() == Card(6, "Spades")

    # # def test_is_g3_straight_flush(self):
    # #     assert self.g3.is_straight_flush() == False
