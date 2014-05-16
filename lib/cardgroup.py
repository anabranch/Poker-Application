from copy import copy
from collections import Counter

from equalitymixin import CommonEqualityMixin
from card import Card

class CardGroup(CommonEqualityMixin):
    """docstring for CardGroup"""
    def __init__(self, cards=[]):
        super(CardGroup, self).__init__()
        self.cards = cards

    def __str__(self):
        return str(self.cards)

    def _local_card_copy(self):
        return [copy(card) for card in self.cards]

    def _cards_by_number(self):
        local_cards = self._local_card_copy()
        number_dict = {}
        for card in local_cards:
            if card.number not in number_dict:
                number_dict[card.number] = []
            number_dict[card.number].append(card)
        return number_dict

    def high_cards(self, remove_cards=[], mx=5):
        if mx > 5:
            mx = 5
        local_cards = self._local_card_copy()
        for card in remove_cards:
            local_cards.pop(local_cards.index(card))
        # need to get this to return cards not a tuple
        return sorted([card.as_tuple() for card in local_cards], reverse=True)[:mx]

    def pairs(self):
        pairs = []
        pair_value = 0
        groups = self._cards_by_number()
        for card_num, cards in groups.items():
            if len(cards) <= 1:
                del(groups[card_num])
        for k, v in groups.items():
            if k > pair_value:
                pair_value = k
                pairs = v[:2]
        if pairs:
            return {"pair": pairs, "high_cards":self.high_cards(pairs,3)}
        return {}

    def trips(self):
        trips = []
        trip_value = 0
        groups = self._cards_by_number()
        for card_num, cards in groups.items():
            if len(cards) <= 2:
                del(groups[card_num])
        for k, v in groups.items():
            if k > trip_value:
                trip_value = k
                trips = v[:3]
        if trips:
            return {"trip": trips, "high_cards":self.high_cards(trips,2)}
        return {}

    def quads(self):
        quads = []
        quad_value = 0
        groups = self._cards_by_number()
        for card_num, cards in groups.items():
            if len(cards) <= 3:
                del(groups[card_num])
        for k, v in groups.items():
            if k > quad_value:
                quad_value = k
                quads = v[:4]
        if quads:
            return {"quad": quads, "high_cards":self.high_cards(quads,1)}
        return {}

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
    print x.cards
    print x.high_cards()
    print x.pairs()
    print x.trips()
    print x.quads()
        