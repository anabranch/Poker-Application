from card import Card

class Deck(object):
    """docstring for Deck"""
    def __init__(self):
        super(Deck, self).__init__()
        suits = ["Diamonds","Clubs","Hearts","Spades"]
        number = range(2,15)
        self.cards = []
        for suit in suits:
            for card in number:
                self.cards.append(Card(card, suit))