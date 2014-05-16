from copy import copy
from collections import Counter

from equalitymixin import CommonEqualityMixin
from card import Card

class CardGroup(CommonEqualityMixin):
    """docstring for CardGroup"""
    def __init__(self, cards=[]):
        super(CardGroup, self).__init__()
        self._cards = [copy(card) for card in cards]

    def __str__(self):
        return str(self._cards)

    def cards(self):
        return [copy(card) for card in self._cards]

    def _cards_by_number(self):
        local_cards = self.cards()
        number_dict = {}
        for card in local_cards:
            if card.number not in number_dict:
                number_dict[card.number] = []
            number_dict[card.number].append(card)
        return number_dict

    def high_cards(self, remove_cards=[], mx=5):
        if mx > 5:
            mx = 5
        local_cards = self.cards()
        for card in remove_cards:
            local_cards.pop(card)
        return sorted([card.as_tuple() for card in local_cards], reverse=True)[:5]

    def is_pair(self):
        groups = self._cards_by_number()
        for card_num, cards in groups.items():
            if len(cards) <= 1:
                del(groups[card_num])
        print groups




class PocketCardGroup(CardGroup):
    """docstring for PocketCardGroup"""
    def __init__(self, cards=[]):
        super(PocketCardGroup, self).__init__(cards)

if __name__ == '__main__':
    x = PocketCardGroup([
            Card(14,"Diamonds"), 
            Card(14,"Clubs"), 
            Card(13,"Diamonds"), 
            Card(14,"Hearts"), 
            Card(14,"Spades"), 
            Card(12, "Hearts")
        ])
    print x.cards()
    print x.high_cards()
    print x.is_pair()
        