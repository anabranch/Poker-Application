from lib.card import Card
from lib.cardgroup import CardGroup
from lib.deck import Deck
from random import sample

class TestCardGroup(object):
    def setUp(self):
        # Straight flush with ace
        self.g1 = CardGroup([Card(c, "Diamonds") for c in range(2,6)])
        self.g1.add_card(Card(14,"Diamonds"))
        self.g1.add_card(Card(14, "Clubs"))
        self.g1.add_card(Card(14, "Hearts"))
        # Straight flush no ace
        self.g2 = CardGroup([Card(c, "Spades") for c in range(2,7)])
        self.g2.add_card(Card(5, "Diamonds"))
        self.g2.add_card(Card(10, "Clubs"))
        # straight
        self.g3 = CardGroup()
        self.g3.add_card(Card(2, "Diamonds"))
        self.g3.add_card(Card(4, "Spades"))
        self.g3.add_card(Card(3, "Hearts"))
        self.g3.add_card(Card(6, "Clubs"))
        self.g3.add_card(Card(5, "Diamonds"))
        self.g3.add_card(Card(5, "Clubs"))
        self.g3.add_card(Card(2, "Clubs"))

    def test_is_straight(self):
        assert self.g1.is_straight() == True
        assert self.g1.straight_details() == Card(5, "Diamonds")
        assert self.g2.is_straight() == True
        assert self.g2.straight_details() == Card(6, "Spades")
        assert self.g3.is_straight() == True
        assert self.g3.straight_details() == Card(6, "Clubs")

    def test_is_flush(self):
        assert self.g1.is_flush() == True
        assert self.g1.flush_details() == Card(14, "Diamonds")
        assert self.g2.is_flush() == True
        assert self.g2.flush_details() == Card(6, "Spades")
        assert self.g3.is_flush() == False
        
    def test_is_straight_flush(self):
        assert self.g1.is_straight_flush() == True
        assert self.g1.straight_flush_details() == Card(5, "Diamonds")
        assert self.g2.is_straight_flush() == True
        assert self.g2.straight_flush_details() == Card(6, "Spades")
        assert self.g3.is_straight_flush() == False
